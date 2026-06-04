"""Unit tests for the vending-machine inventory model.

These exercise the dispense/refill logic without a broker or GUI by swapping in
a fake MQTT client.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from vending_machine import VENDING_MACHINE  # noqa: E402


class FakeClient:
    """Stand-in for the MQTT client so tests need no running broker."""

    def __init__(self):
        self.published = []

    def publish(self, topic, payload):
        self.published.append((topic, payload))


def make_machine():
    machine = VENDING_MACHINE(connect=False)
    machine.client = FakeClient()
    return machine


def test_dispense_unavailable_returns_zero():
    machine = make_machine()
    machine.product = [[] for _ in machine.product]
    assert machine.Dispense("coke") == 0
    assert machine.client.published == []


def test_dispense_removes_one_unit_and_notifies():
    machine = make_machine()
    machine.product = [[] for _ in machine.product]
    machine.product[0] = ["coke", "coke"]
    assert machine.Dispense("coke") == 1
    assert machine.product[0] == ["coke"]
    assert machine.client.published[-1][0] == machine.topic


def test_dispense_empties_smallest_stack_first():
    machine = make_machine()
    machine.product = [[] for _ in machine.product]
    machine.product[0] = ["coke", "coke", "coke"]
    machine.product[1] = ["coke"]  # smallest non-empty stack
    machine.Dispense("coke")
    assert machine.product[1] == []  # the single-item stack was used first
    assert len(machine.product[0]) == 3


def test_refill_only_fills_an_empty_slot():
    machine = make_machine()
    machine.product[0] = []
    assert machine.Refill("lays", 5, 0, 0) == 1
    assert machine.product[0] == ["lays"] * 5
    assert machine.Refill("lays", 5, 0, 0) == 0  # already full -> rejected

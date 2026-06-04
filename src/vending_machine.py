#!/usr/bin/env python3
"""Vending-machine inventory model with MQTT transaction notifications.

The machine holds 25 slots (a 5x5 grid); each slot is a stack of identical
products. Dispensing and refilling publish a short message to an MQTT broker so
an external monitor can observe the machine's activity.
"""

import os
import random

import paho.mqtt.client as mqtt

# Broker host and topic are configurable via the environment so the simulator
# can target a remote broker instead of being hard-wired to localhost.
MQTT_BROKER = os.environ.get("MQTT_BROKER", "localhost")
MQTT_TOPIC = os.environ.get("MQTT_TOPIC", "host/vm")

COLUMNS = 5
STACK_SIZE = 5
SLOTS = 25


class VENDING_MACHINE(object):
    """Inventory of stacked products with MQTT notifications per transaction."""

    def __init__(self, broker=MQTT_BROKER, topic=MQTT_TOPIC, connect=True):
        """Build a machine with every slot randomly stocked.

        Args:
            broker:  MQTT broker host.
            topic:   MQTT topic to publish transactions to.
            connect: open the MQTT connection now (set False in tests).
        """
        self.posible_product = ['coke', 'jet', 'mm', 'takis', 'layslem',
                                'sponch', 'mmp', 'trident', 'snickers',
                                'lays', 'gummies', 'pepsi']
        self.product = [[random.choice(self.posible_product)] * STACK_SIZE
                        for _ in range(SLOTS)]
        self.topic = topic
        self.client = mqtt.Client("00")
        if connect:
            self.client.connect(broker)

    def Refill(self, product_refill, quantity_refill, row, column):
        """Refill an empty slot.

        Returns 1 if the slot was empty and got filled, 0 otherwise.
        """
        slot = row * COLUMNS + column
        if self.product[slot] == []:
            self.product[slot] = [product_refill for _ in range(quantity_refill)]
            self.client.publish(self.topic, "refill:" + product_refill)
            return 1
        return 0

    def Dispense(self, product_dispense):
        """Dispense one unit of a product.

        Returns 1 on success, 0 if the product is not available. When several
        slots hold the product, the smallest non-empty stack is emptied first so
        partially filled slots clear out before full ones.
        """
        matches = [i for i, stack in enumerate(self.product)
                   if stack and stack[0] == product_dispense]
        if not matches:
            return 0

        target = min(matches, key=lambda i: len(self.product[i]))
        del self.product[target][0]
        self.client.publish(self.topic, "dispense:" + product_dispense)
        return 1

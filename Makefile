.PHONY: run test lint clean

# Launch the GUI. The app expects to run from src/ (relative imports + Qt resources).
run:
	cd src && python3 display.py

# Unit tests for the inventory model (no broker or GUI required).
test:
	python3 -m pytest -q

# Static checks (unused names, undefined refs) on the hand-written model + tests.
lint:
	python3 -m pyflakes src/vending_machine.py tests

clean:
	rm -rf .pytest_cache
	find . -type d -name __pycache__ -prune -exec rm -rf {} +

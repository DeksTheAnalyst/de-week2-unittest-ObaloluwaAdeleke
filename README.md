Project Overview

This project simulates an Artificial Pancreas System that monitors blood glucose levels and automatically delivers insulin when necessary.
It demonstrates object-oriented programming and unit testing principles in Python.

Features

Simulates glucose response to meals and exercise

Predicts and executes correct system actions

Automatically delivers insulin above target range

Tracks total insulin delivered

Maintains glucose within safe limits (no crash below minimum)

Includes manual test file for real-time testing

Project Structure
de-week2-unittest-ObaloluwaAdeleke/
│
├── main/
│   └── artificial_pancreas.py        # Core system logic (OOP implementation)
│
├── tests/
│   └── test_artificial_pancreas.py   # Unit tests using pytest
│
├── manual_test.py                    # Script for manual testing via user input
│
├── README.md                         # Project documentation
└── requirements.txt                  # Dependencies (pytest)

Key Components
artificial_pancreas.py

Contains the ArtificialPancreasSystem class which models:

Glucose changes after meals and exercise

Predictive insulin delivery

Safe glucose thresholds and insulin tracking

test_artificial_pancreas.py

Implements pytest unit tests covering:

Glucose increase/decrease behavior

Correct action prediction (deliver_insulin, warn_low_glucose, maintain)

Total insulin tracking

Sequential events and safety limits

Invalid input handling

manual_test.py

Allows interactive testing from the command line:

from main.artificial_pancreas import ArtificialPancreasSystem

controller = ArtificialPancreasSystem(glucose_level=100)

controller.meal(40)
controller.exercise(20)

action, level = controller.predict_action()
print(f"Action: {action}, Glucose Level: {level}")


Run manualtest:

python manual_test.py

To execute all the tests with pytest, run:

python -m pytest tests\test_artificial_pancreas.py -v




Git Workflow Summary

Created repo: de-week2-unittest-ObaloluwaAdeleke

Initialized on main

Created feature branch: feature/week2-unittest

Opened Pull Request → feature/week2-unittest → main



This document and project was prepared by Obaloluwa Adeleke

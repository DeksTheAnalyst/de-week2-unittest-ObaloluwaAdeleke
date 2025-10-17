import pytest
from main.artificial_pancreas import ArtificialPancreasSystem


def test_glucose_increases_after_meal():
    system = ArtificialPancreasSystem(glucose_level=100)
    before = system.glucose_level
    system.meal(10)  # 10 carbs from the meal
    after = system.glucose_level
    assert after == before + 10 * system.GLUCOSE_PER_CARB

def test_glucose_decreases_after_exercise():
    system = ArtificialPancreasSystem(glucose_level=100)
    before = system.glucose_level
    system.exercise(20)  # 20 minutes of exercise
    after = system.glucose_level
    assert after == before - 20 * system.GLUCOSE_BURN_PER_MIN

def test_high_glucose_triggers_insulin():
    system = ArtificialPancreasSystem(glucose_level=120)  # 100 target + 10 tolerance = 110 threshold
    action, _ = system.predict_action()
    assert action == "deliver_insulin"

def test_low_glucose_triggers_warning():
    system = ArtificialPancreasSystem(glucose_level=85)  # below 90 (100 - 10 tolerance)
    action, _ = system.predict_action()
    assert action == "warn_low_glucose"

def test_normal_glucose_maintains_state():
    system = ArtificialPancreasSystem(glucose_level=100)  # within 90–110
    action, _ = system.predict_action()
    assert action == "maintain"

def test_glucose_never_drops_below_minimum():
    system = ArtificialPancreasSystem(glucose_level=120)
    system.exercise(500)  # a long workout without safeguard should try to drop it below 50 which is the minimum glucose level
    assert system.glucose_level >= system.MIN_GLUCOSE_LEVEL

def test_predict_action_increases_total_insulin_delivered():
    system = ArtificialPancreasSystem(130)  # high glucose
    action, _ = system.predict_action()
    
    assert action == "deliver_insulin"
    assert system.total_insulin_delivered > 0

def test_no_insulin_delivered_when_glucose_low():
    system = ArtificialPancreasSystem(glucose_level=70)
    initial_total = system.total_insulin_delivered
    action, _ = system.predict_action()
    assert action == "warn_low_glucose"   # updated expectation
    assert system.total_insulin_delivered == initial_total


def test_no_action_for_normal_glucose():
    system = ArtificialPancreasSystem(glucose_level=105)
    action, _ = system.predict_action()
    assert action == "maintain"    # updated expectation

def test_multiple_sequential_events():
    system = ArtificialPancreasSystem(glucose_level=100)
    
    system.meal(40)   # glucose rises by 40 * 0.5 = 20 → 120
    assert system.glucose_level == 120
    
    system.exercise(30)  # glucose drops by 30 * 0.3 = 9 → 111
    assert system.glucose_level == 111
    
    action, level = system.predict_action()
    assert action == "deliver_insulin"
    
    assert system.total_insulin_delivered > 0
    
    #Final glucose should be around the tolerance range
    assert 108 <= system.glucose_level <= 112

def test_negative_carbs():
    system = ArtificialPancreasSystem(glucose_level=100)
    with pytest.raises(ValueError):
        system.meal(-10)

def test_negative_exercise():
    system = ArtificialPancreasSystem(glucose_level=100)
    with pytest.raises(ValueError):
        system.exercise(-20)


def test_non_numeric_input():
    system = ArtificialPancreasSystem(glucose_level=100)
    with pytest.raises(TypeError):
        system.meal("forty")

#python -m pytest tests\test_artificial_pancreas.py -v
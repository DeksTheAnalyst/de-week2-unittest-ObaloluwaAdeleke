class ArtificialPancreasSystem:
    """A simplified model for data-driven glucose regulation."""

    GLUCOSE_PER_CARB = 0.5
    GLUCOSE_BURN_PER_MIN = 0.3
    MIN_GLUCOSE_LEVEL = 50

    def __init__(self,  glucose_level, insulin_sensitivity=1.0, target_glucose=100, tolerance=10):
        #self.patient_name = patient_name(It is currently making my tests not run, we'll address it later)
        self.glucose_level = glucose_level
        self.insulin_sensitivity = insulin_sensitivity
        self.target_glucose = target_glucose
        self.tolerance = tolerance
        self.total_insulin_delivered = 0.0
    
    def meal(self, carbs: float):
        """Simulate a meal event (input feature: carbs)."""
        if carbs < 0:
            raise ValueError("Carbs cannot be negative.")
        self.glucose_level += carbs * self.GLUCOSE_PER_CARB

    def exercise(self, duration: float):
        """Simulate physical activity (input feature: duration)."""
        if duration < 0:
            raise ValueError("Exercise duration cannot be negative.")
        self.glucose_level -= duration * self.GLUCOSE_BURN_PER_MIN
        if self.glucose_level < self.MIN_GLUCOSE_LEVEL:
            self.glucose_level = self.MIN_GLUCOSE_LEVEL

    def predict_action(self):
        """Decide and apply the appropriate action."""
        if self.glucose_level > self.target_glucose + self.tolerance:
            # Too high → give insulin
            excess = self.glucose_level - self.target_glucose
            insulin_dose = excess * self.insulin_sensitivity * 0.1  # simple proportional dose
            self.glucose_level -= insulin_dose
            self.total_insulin_delivered += insulin_dose
            action = "deliver_insulin"

        elif self.glucose_level < self.target_glucose - self.tolerance:
            # Too low → warn
            action = "warn_low_glucose"

        else:
            # Stable range → maintain
            action = "maintain"

        return action, self.glucose_level

#f"{action} to {self.patient_name}", self.glucose_level(original code if I want to use patient name)

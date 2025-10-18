from main.artificial_pancreas import ArtificialPancreasSystem

#patient_name = input("Enter Your Name")

controller = ArtificialPancreasSystem(100)
controller.meal(40)
controller.exercise(20)
action, level = controller.predict_action()

print(f"Action: {action}, Glucose Level: {level}")

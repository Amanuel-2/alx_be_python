task = input("Enter your task: ")
priority = input("Priority (high/medium/low):").lower()
time_bound = input("Is it time-bound? (yes/no):").lower()

while priority not in ["high","medium","low"]:
    print("Invalid priority. Please enter high, medium, or low.")
    priority = input("Priority (high/medium/low): ").lower()
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task "
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task "
    case "low":
        reminder = f"Note: '{task}' is a low priority task "
    case _:
        reminder = f"'{task}' has an undefined priority."
    
if time_bound == "yes":
    reminder += "that requires immediate attention today!"
else:
    if priority == "low":
        reminder += ". consider competing it when you have free time."
    else:
        reminder += "."
print(reminder)
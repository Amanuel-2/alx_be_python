task = input("Enter your task: ").strip()
while not task:
    print("Task cannot be empty.")
    task = input("Enter your task: ").strip()

priority = input("Priority (high/medium/low): ").lower()
while priority not in ["high", "medium", "low"]:
    print("Invalid priority. Please enter high, medium, or low.")
    priority = input("Priority (high/medium/low): ").lower()

time_bound = input("Is it time-bound? (yes/no): ").lower()
while time_bound not in ["yes", "no"]:
    print("Please answer yes or no.")
    time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' is a task"

if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". This task is not time-bound, so complete it when appropriate."


print("\nReminder:", reminder)

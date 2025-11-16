# daily_reminder.py

# Prompt user for inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match case for priority message
match priority:
    case "high":
        priority_msg = "a high priority task"
    case "medium":
        priority_msg = "a medium priority task"
    case "low":
        priority_msg = "a low priority task"
    case _:
        priority_msg = "a task with unknown priority"

# Time sensitivity message
if time_bound == "yes":
    time_msg = "Immediate action is required today!"
else:
    time_msg = "You can complete it when you have free time."

# Final reminder message (ALX friendly)
print(f"Reminder: Your task '{task}' is {priority_msg}. {time_msg}")
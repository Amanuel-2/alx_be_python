# daily_reminder.py

# ---------------------------
# Input validation using loop
# ---------------------------

# Task input
while True:
    task = input("Enter your task: ").strip()
    if task:    # ensure not empty
        break
    print("Task cannot be empty. Please enter a task.")

# Priority input
while True:
    priority = input("Priority (high/medium/low): ").strip().lower()
    if priority in ("high", "medium", "low"):
        break
    print("Please enter a valid priority: high, medium, or low.")

# Time-bound input
while True:
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    if time_bound in ("yes", "no"):
        break
    print("Please answer only 'yes' or 'no'.")

# ---------------------------
# Match–Case for priority
# ---------------------------
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' is a task"  # safety fallback

# ---------------------------
# If-statement for time-bound
# ---------------------------
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# ---------------------------
# Final customized reminder
# ---------------------------
print("\nReminder:", reminder)

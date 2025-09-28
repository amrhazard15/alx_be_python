# daily_reminder.py

while True:
    task = input("Enter your task: ").strip()
    if task:
        break
    print("Please enter a non-empty task description.")

while True:
    priority = input("Priority (high/medium/low): ").strip().lower()
    if priority in ("high", "medium", "low"):
        break
    print("Invalid priority. Please type 'high', 'medium', or 'low'.")

while True:
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    if time_bound in ("yes", "no"):
        break
    print("Please answer 'yes' or 'no'.")

match priority:
    case "high":
        priority_text = "high"
    case "medium":
        priority_text = "medium"
    case "low":
        priority_text = "low"

if time_bound == "yes":

    print(f"Reminder: '{task}' is a {priority_text} priority task that requires immediate attention today!")
else:
    print(f"Note: '{task}' is a {priority_text} priority task. Consider completing it when you have free time.")

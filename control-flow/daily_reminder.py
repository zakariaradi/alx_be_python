def main():
    # Prompt user for task information
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower().strip()
    time_bound = input("Is it time-bound? (yes/no): ").lower().strip()
    
    # Process task using match case for priority
    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a high priority task. Focus on completing it soon.")
        
        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task that should be addressed today.")
            else:
                print(f"Note: '{task}' is a medium priority task. Plan to complete it in the coming days.")
        
        case "low":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a low priority task with a time constraint. Consider completing it today.")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        
        case _:
            print("Invalid priority level. Please enter high, medium, or low.")

if __name__ == "__main__":
    main()
    
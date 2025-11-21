from datetime import datetime, timedelta

def display_current_datetime():
    # Get current date and time
    current_date = datetime.now()

    # Format: YYYY-MM-DD HH:MM:SS
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

    return current_date  # return needed for part 2


def calculate_future_date(current_date, days_to_add):
    # Create future date using timedelta
    future_date = current_date + timedelta(days=days_to_add)

    # Format: YYYY-MM-DD
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")

    return future_date


def main():
    # Part 1: show current date/time
    current_date = display_current_datetime()

    # Part 2: calculate future date
    try:
        days = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Invalid input: please enter an integer.")
        return

    calculate_future_date(current_date, days)


if __name__ == "__main__":
    main()

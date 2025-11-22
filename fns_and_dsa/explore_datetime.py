from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time in a readable format."""
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date():
    """Calculate and display a future date based on user input."""
    # Prompt user for number of days
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    
    # Calculate the future date
    current_date = datetime.now()
    future_date = current_date + timedelta(days=number_of_days)
    
    # Print the future date
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

def main():
    # Part 1: Display current date and time
    display_current_datetime()
    
    # Part 2: Calculate future date
    calculate_future_date()

if __name__ == "__main__":
    main()
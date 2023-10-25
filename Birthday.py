import datetime

def get_day_of_week(birthday):
    try:
        # Parse the input date in the format YYYY-MM-DD
        birth_date = datetime.datetime.strptime(birthday, '%Y-%m-%d')
        
        # Get the day of the week (0 = Monday, 6 = Sunday)
        day_of_week = birth_date.strftime('%A')
        
        return day_of_week
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

# Get the birthday from the user
birthday = input("Enter your birthday (YYYY-MM-DD): ")

# Get the day of the week
day = get_day_of_week(birthday)

if day != "Invalid date format. Please use YYYY-MM-DD.":
    print(f"You were born on a {day}.")
else:
    print(day)


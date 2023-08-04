#달력 만들기

import calendar

def smartphone_calendar():
    print("Welcome to the Smartphone Calendar!")
    
    while True:
        try:
            year = int(input("Enter the year (e.g., 2023): "))
            month = int(input("Enter the month (1-12): "))
            
            if 1 <= month <= 12:
                cal = calendar.TextCalendar(calendar.SUNDAY)
                month_calendar = cal.formatmonth(year, month)
                print("\n" + month_calendar)
            else:
                print("Invalid month. Please enter a value between 1 and 12.")
        
        except ValueError:
            print("Invalid input. Please enter valid numeric values for year and month.")
        
        choice = input("Do you want to view another calendar? (y/n): ")
        if choice.lower() != 'y':
            print("Thank you for using the Smartphone Calendar. Goodbye!")
            break

if __name__ == "__main__":
    smartphone_calendar()

'''''
month = int(input("Enter the month (1-12): "))
year = int(input("Enter the year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    leap_year = True
else:
    leap_year = False

if month == 1:
    days = 31
elif month == 2:
    if leap_year:
        days = 29
    else:
        days = 28
elif month == 3:
    days = 31
elif month == 4:
    days = 30
elif month == 5:
    days = 31
elif month == 6:
    days = 30
elif month == 7:
    days = 31
elif month == 8:
    days = 31
elif month == 9:
    days = 30
elif month == 10:
    days = 31
elif month == 11:
    days = 30
elif month == 12:
    days = 31
else:
    days = "Invalid month"

if isinstance(days, int): 
    print(f"The month {month} of year {year} has {days} days.")
else:
    print(days) 

'''




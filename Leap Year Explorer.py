#task 1 Leap Year Checker: Write a Python prohram that prompts the user to input a year. The program should determine if the given year is the definition of a leap year: Every year
#that is exactly dvisible by 4 is a leap year, except for the years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400.

check_year = int(input("Enter the year you wish to know is a leap year or not:"))
if check_year % 4 == 0 and not check_year % 100 == 0 and not check_year % 400 == 0:
    print(check_year, "is a leap year.")
elif check_year % 4 == 0 and check_year % 100 == 0 and check_year % 400 == 0:
    print(check_year, "is a leap year.")    
elif check_year % 4 == 0 and check_year % 100 == 0 and not check_year % 400 == 0:
    print(check_year, "is a not a leap year.")
else:
    print(check_year, "is not a leap year.")
            
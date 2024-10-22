#Task 1 Code Correction: You are provided with a python script that uses conditional statements to tell if a number is positive, negative, or zero, but has some errors.
# Identify and fix them.
# Buggy Code:
#number = input("Enter a number: ")
#
#if number > 0:
#    print("The number is positive.")
#elif number == 0:
#    print("The number is zero.")
#else number < 0:
#    print("The number is negative.")

number = float(input("Enter a number: ")) #the input needs to be expressed as a numeric vaule, not necessarily a whole number, so we're converting the input from string to float 

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:                                     # removed the conditional for else. Else is a final statement, for when all other conditions have not been met, it shouldnt have a condition associated with it.
    print("The number is negative.")
    
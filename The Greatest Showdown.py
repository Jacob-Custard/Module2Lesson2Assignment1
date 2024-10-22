#Task 1 Identify the Greatest: Write a Python program that asks the user to enter three numbers. Your code should then identify and print out the largest number among the three.
number_a, number_b, number_c = float(input("Enter your first number: ")), float(input("Enter your second number: ")), float(input("Enter your final number: "))
if number_a >= number_b and number_a >= number_c:
    print(f"The largest number is {number_a}")
elif number_b >= number_a and number_b >= number_c:
    print(f"The largest number is {number_b}")
elif number_c >= number_a and number_c >= number_b:
    print(f"The largest number is {number_c}")

#Task 2 Identify the Smallest: Improve upon your code from task 1 to also determine the smallest number among the three and print it out. 
number_a, number_b, number_c = float(input("Enter your first number: ")), float(input("Enter your second number: ")), float(input("Enter your final number: "))
big_number = 0
small_number = 0
if number_a >= number_b and number_a >= number_c:
    big_number = float(number_a)
elif number_b >= number_a and number_b >= number_c:
    big_number = float(number_b)
elif number_c >= number_a and number_c >= number_b:
    big_number = float(number_c)
if number_a <= number_b and number_a <= number_c:
    small_number = float(number_a) 
elif number_b <= number_a and number_b <= number_c:
    small_number = float(number_b)
elif number_c <= number_a and number_c <= number_b:
    small_number = float(number_c)             

print ("Your 3 numbers are", number_a, number_b, "and", number_c)
print ("The largrest number of the group is", big_number, "and the smallest number in the group is", small_number,".")






# 08/29/2018
"""
Reversing the number of the user input.
"""

try:
    number = int(input("Enter number you want to reverse:  "))
    if number < 0:
        print("Negative number is not allowed.")
    else:
        reverse = ""
        while number != 0:
            counter = number % 10
            number = number // 10
            reverse += str(counter)  # convert the counter into a string to allow concatenate.
        print(f"The reverse number is: {reverse}")

except ValueError:
    print("Characters is not allowed.")


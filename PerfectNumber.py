# 08/30/2018
"""
Determine if the user inputs a Perfect number or not.
"""

number = int(input("Enter a number: "))
if number <= 0:
    print("Zero or Negative number is not allowed.")
else:
    sumOfDivisor = 0
    for counter in range(1, number):
        if (number % counter) == 0: # getting the sum of the all the divisor excluding itself
            sumOfDivisor += counter  
    if number == sumOfDivisor:  # comparing if user input and the sum of divisor is equal
        print(f"{number} is a Perfect Number.")
    else:
        print(f"{number} is not a Perfect Number.")

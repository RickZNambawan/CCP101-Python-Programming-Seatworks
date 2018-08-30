# 08/30/2018
"""
Get the prime number and compute the sum of all the prime numbers
from 1 up to the user input.
"""

number = int(input("Enter a number: "))
if number <= 0:
    print("Zero or Negative Number is not allowed.")
else:
    sumOfPrimeNumber = 0
    for counter in range(2, number):
        for anotherCounter in range(2, number):
            # if they are equal, get the prime number, stop the loop then go to the next loop
            if counter == anotherCounter:  
                sumOfPrimeNumber += counter
                break
            
            # if their remainder is 0, stop the loop. meaning it's not a prime number
            elif (counter % anotherCounter) == 0:
                break
    print(f"The sum of all the prime numbers from 1 to {number} is {sumOfPrimeNumber:,}.")

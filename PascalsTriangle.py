# 08-29-2018
"""
Using the Pascal's Triangle, ask the user to input any row below 25
and check the sum of all the row above the user input and also check
the sum of the next row.
"""

row = int(input("Enter a row: "))

if row > 25:  # erase this if statement to allow the user to input any row.
    print("Row 26 and above is not allowed.")
elif row < 0:
    print("Negative number is not allowed.")
else:
    sumAbove = 0
    for number in range(row):  # get the sum of all the row above except the user input.
        sumAbove += 2 ** number
        
    sumBelow = 0
    for anotherNumber in range(row + 2):  # get the sum of the specific row below the user input.
        sumBelow = 2 ** anotherNumber
        
    print(f"The sum above the row {row} is {sumAbove:,}. ", end="")
    print(f"The sum of the immediate row {row + 1} is {sumBelow:,}.")

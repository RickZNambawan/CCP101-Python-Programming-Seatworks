# 08/28/2018
# CHECKING IF USER INPUTS A PALINDROMIC NUMBER

number = int(input("Enter a number: "))
anotherNumber = number

if anotherNumber < 100:  # checking if the user inputs less than 3 digits.
    print("Invalid Input.")
else:
    anotherCounter = ""
    while anotherNumber != 0:
        counter = anotherNumber % 10
        anotherNumber = anotherNumber // 10
        anotherCounter += str(counter)  # converting int to str so that anotherCounter can concatenate counter.

# checking if user input is equal to anotherCounter
    if number == int(anotherCounter):  # convert str to int
        print("{} is a Palindrome Number.".format(number))
    else:
        print("{} is not a Palindrome Number.".format(number))

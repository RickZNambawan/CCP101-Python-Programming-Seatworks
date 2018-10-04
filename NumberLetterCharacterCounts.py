# 10/04/2018
# Identify how many numbers, letters, or special character in a string

string = input("Enter a word: ")

# create a list that will contain the appropriate elements later
number_list = []
letter_list = []
character_list = []

for index in range(len(string)):
    element = string[index]  # element (number, letter, character) on the word

    if element.isdigit():  # if the element in word is number then put that element to the number_list
        number_list.append(element)
    elif element.isalpha():  # if the element in word is letter then put that element to the letter_list
        letter_list.append(element)
    else:  # if the element in word is not a number or a letter, automatically it is a special character
        character_list.append(element)

# get the length (how many elements in the list) of every list then print
print(f"Number Counts: {len(number_list)}")
print(f"Letter Counts: {len(letter_list)}")
print(f"Special Character Counts: {len(character_list)}")


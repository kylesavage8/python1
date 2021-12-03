import random
import datetime
import os
import sys
import re


# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def my_functionname():
    # Get the user's name
    name = input("What is your name:")
    # Print the user's name
    print(f' Hello {name}')


def my_functionnumber():
    # Get the user's number
    number = int(input("What number do you want:"))
    number = number * number
    # Print the user's number by multiply that number by itself
    print(f'Your number is:', number)


def my_functionword():
    # Get the user's for any word
    word = input('What is your word:')
    count = len(word)
    # Print the user's word and counts how many letters are in that word
    print(f'Your word is {word}', count)


# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
# print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# Programming Assignment 3
# (1.) Text Art function
def text_art():
    textart = [['.', '.', '.', '.', '.', '.'],
               ['.', 'O', 'O', '.', '.', '.'],
               ['O', 'O', 'O', 'O', '.', '.'],
               ['O', 'O', 'O', 'O', 'O', '.'],
               ['.', 'O', 'O', 'O', 'O', 'O'],
               ['O', 'O', 'O', 'O', 'O', '.'],
               ['O', 'O', 'O', 'O', '.', '.'],
               ['.', 'O', 'O', '.', '.', '.'],
               ['.', '.', '.', '.', '.', '.']]
    # Make two for loops one for range of 9 to print a grid & the other with a range of 6 to print another grid
    for i in range(9):
        print("\n")
        for w in range(6):
            print(textart[i][w], end="")


# (2.) Coin Flip function
def coin_flip():
    num = 0
    # Create a variable c for choosing heads or tails
    c = 0
    while c != 2:
        # Ask the user to choose either heads 0 or tails 1
        answer = int(input("Either choose heads entering 0 or tails by entering 1:"))
        if answer == 0:
            print("User chose heads ")
        else:
            print("User chose tails")
        flip = random.choice([0, 1])

        if flip == 0:
            # Print coin landed on heads
            print("0 (Computer chose heads)")
        else:
            # Print coin landed on tails
            print("1 (Computer chose tails)")
        if answer == flip:
            # If the values are equal the user wins
            print("User Won!")
        else:
            # If the values are not equal the computer wins
            print("Computer Won!")
        num += 1
        # Ask the user if they want to end the game
        c = input("Enter 6 to exit the game?")
        if c == 6:
            num += 1
        else:
            print("Thanks for playing")
            exit()


# Programming Assignment 5
# Branching and Modules

def today():
    # Make tday = datetime.date.today
    tday = datetime.date.today()
    # Make timedelta  days=7
    tdelta = datetime.timedelta(days=7)
    # Print tday + tdelta that shows 7 days from today's date
    print(tday + tdelta)


def os_module():
    # Print to see what the current directory is
    print(os.getcwd())
    # Print to see what files are on the directory
    print(os.listdir())
    # Print the size of venv file which displays the byte size
    print(os.stat('venv').st_size)


def random_module():
    # Displays a range of a deck of cards from 1 to 20
    card_deck = list(range(1, 20))
    # Make the card deck select 6 random cards each time
    hand = random.sample(card_deck, k=6)
    print(hand)


# Programming Assignment 6
# String with branches

def strings1_accept():
    # In the terminal enter python main.py "then any written text"
    # Print to see what the name of the file is
    print(f"The name of the file is: {sys.argv[0]}")
    # Print to see how many arguments were passed
    print(f"There are {len(sys.argv) - 1} arguments passed")
    # Make the variable number_of_arguments start at index 1 and ending at the end of the list
    number_of_arguments = len(sys.argv[1:])
    # Set the index i = 1
    i = 1
    # Make a while loop setting number_of_arguments >= i
    while number_of_arguments >= i:
        print(f"Argument {i}: {sys.argv[i]}")
        i += 1


def strings1_manipulate():
    arg = sys.argv[1]
    # In the terminal enter python main.py "then any written text"
    if arg == "test":
        print("Strings1 Test")
    # In the terminal enter python main.py "then any written text"
    elif arg == "manipulate":
        print("Test is manipulated")
    # In the terminal enter python main.py "then input anything the function doesn't recognize"
    else:
        print("The argument is invalid")


def user_input():
    # Make the user input something
    user = input("User input: ")
    return user


def string2_reading(s):
    vowels = ["a", "e", "i", "o", "u"]
    # Make fs =  first string
    fs = []
    # Make a for loop setting i in range s
    for i in range(len(s)):
        if s[i][0].lower() in vowels:
            fs.append(f"{s[i]}yay")
        else:
            consonant = s[i][0]
            fs.append(f"{s[i][1:]}{consonant}ay")
    print(' '.join(fs).lower())


def user_input():
    user = input("User input: ")
    return user


def strings3_apostrophe(string):
    regexp = re.compile(r'\'')
    # Make a for loop setting i with range(len(string)
    for i in range(len(string)):
        # Make an if else statement checking if the word has an apostrophe else print the word
        if regexp.search(string[i]):
            break_sentence(string[i], "approved")
        else:
            break_sentence(string[i])


def break_sentence(word, contains_apostrophe="not approved"):
    # Make an if else statement if the word contains_apostrophe else print the rest of the words
    if contains_apostrophe == "approved":
        print(f"List the apostrophe word: {word}")
    else:
        print(word)


# Programming Assignment 7
# Regex branch

#if __name__ == '__main__':
    if os.access("regex.txt", os.F_OK):
        print("File is there.")
    # Make f open the regex.txt to read the file
    f = open("regex.txt", "r")
    getlines = f.readlines()
    # Make a for loop so le = line gets the line
    for le in getlines:
        locateitems = re.locateall(".$", le)
        # Make a nested for loop so i = "%"
        for i in locateitems:
            if i == "%":
                # Print the line
                print(f"le: {le}")
                # Print the final character in the previous line
                print(f"Final character is {i} in the previous print line")
    # Make a if statement to check if the regex.txt file is still there
    if os.access("regex.txt", os.F_OK):
        print("File regex.txt is there.")
    try:
        # Rename the text file to something else
        os.rename("regex.txt", "new_regex.txt")
        # Print the new text file
        print("Renamed regex.txt -> new_regex.txt")
        if os.access("regex.txt", os.F_OK):
            # Print to check if the original text file was properly removed
            print("File regex.txt was removed.")
    except:
        pass
    # Make an if statement to return the absolute path of the working directory
    if "Current computer accounts" in os.getcwd():
        print("Login name: ", re.split("\\\\", os.getcwd())[2])
        print("Current directory: ", re.split('\\\\', os.getcwd())[0])


# Programming Assignment 8
# Object-Oriented Programming branch

class Bird:
    # Make an function for the bird's name and species
    def __init__(self, name, species):
        self.name = name
        self.species = species

    # Make a speak function displaying what the bird's name is
    def speak(self):
        print(f"His/Her's name is {self.name}")

    # Make a species function displaying what type of bird species was chosen
    def bird_species(self):
        print(f"This bird's species is a {self.species}")


# Make a species_list for six different types of birds
species_list = ["pigeon", "woodpecker", "bluebird", "northern cardinal", "mousebird", "gannet"]


# Make a species(decision) function
def bird_species(decision):
    while True:
        # Create if elif statements making the user decide what species of bird they want
        if int(decision) == 1 or str(decision) == "pigeon":
            return "pigeon"
        elif int(decision) == 2 or str(decision) == "woodpecker":
            return "woodpecker"
        elif int(decision) == 3 or str(decision) == "bluebird":
            return "bluebird"
        elif int(decision) == 4 or str(decision) == "northern cardinal":
            return "northern cardinal"
        elif int(decision) == 5 or str(decision) == "mousebird":
            return "mousebird"
        elif int(decision) == 6 or str(decision) == "gannet":
            return "gannet"
        else:
            decision = input("Input the species number: ")


if __name__ == '__main__':
    # Print the name of the first bird
    b1_name = input("Bird ones name is: ")
    # Print the name of the second bird
    b2_name = input("Bird two's name is: ")
    # Print if the computer selects a species randomly for b1
    random_decision = input("Decision for computer to select a species randomly for b1 (y/n): ")
    # Make an if else statement for selected b1
    if random_decision.lower() == "y":
        b1 = Bird(b1_name, random.choice(species_list))
    else:
        # Print the species list
        print("Now print the species list:")
        for num, i in enumerate(species_list):
            print(num + 1, i)
        # Print a species or number
        selected_species = input("Input the species number: ")
        b1_species = bird_species(selected_species)
        b1 = Bird(b1_name, b1_species)
    # Print if the computer selects a species randomly for b2
    random_decision = input("Decision for computer to select a species randomly for b2 (y/n): ")
    # Make an if else statement for selected b2
    if random_decision.lower() == "y":
        b2 = Bird(b2_name, random.choice(species_list))
    else:
        print("Now print the species list:")
        for num, i in enumerate(species_list):
            print(f" {num + 1}", i)
        # Print a species or number
        selected_species = input("Input the species number: ")
        b2_species = bird_species(selected_species)
        b2 = Bird(b2_name, b2_species)

    # Print that two birds have been created
    print("Two birds have been created")
    # Print that you created the first bird
    print("First bird is:")
    b1.speak()
    b1.bird_species()
    # Print that you created the second bird
    print("Second bird is:")
    b2.speak()
    b2.bird_species()
    # Display both all the methods and attributes
    attribute = dir(Bird)
    methods = []
    attributes = []

    # Make a for loop displaying all the methods and attributes
    for i in attribute:
        if i.startswith("__"):
            attributes.append(i)
        else:
            methods.append(i)
    # Print the total attributes
    print(f"Total attributes are: {attributes}")
    # Print the total methods
    print(f"Total methods are: {methods}")


# if __name__ == '__main__':
# strings1_accept()
# strings1_manipulate()
# string2_reading(user_input().split(" "))
# strings3_apostrophe(user_input().split(" "))
# today()
# os_module()
# random_module()
# text_art()
# coin_flip()
# print_hi('PyCharm')
# my_functionname()
# my_functionnumber()
# my_functionword()

# Programming Assignment 4
# Tic-tac-toe Functions

# from random import randrange

# The function accepts one parameter containing the board's current status
# def display_board(board):
# print("+-------" * 3, "+", sep="")
# Make a for loop for the row with a range of 3
# for row in range(3):
# Print the row
# print("|       " * 3, "|", sep="")
# Make a for loop for the column with a range of 3
# for column in range(3):
# Print the column and the board
# print("|   " + str(board[row][column]) + "   ", end="")
# print("|")
# print("|       " * 3, "|", sep="")
# print("+-------" * 3, "+", sep="")

# The function accepts the board's current status, asks the user about their move,
# checks the input, and updates the board according to the user's decision
# def enter_move(board):
# If the move is false, enter the loop
# okay = False
# while not okay:
# e_move = input("Enter your move: ")
# Check if the user's input is valid
# okay = len(e_move) == 1 and e_move >= '1' and e_move <= '9'
# if not okay:
# Print invalid move, repeat move again
# print("Invalid move - repeat move!")
# continue
# The cell's number is from 0 to 8
# e_move = int(e_move) - 1
# Displays the cell's row
# row = e_move // 3
# Displays the cell's column
# column = e_move % 3
# Now check the picked box
# sign = board[row][column]
# okay = sign not in ['O', 'X']
# if not okay:
# Print field currently occupied
# print("Field currently occupied - repeat move!")
# continue
# Now set '0' at the picked box
# board[row][column] = 'O'

# The function browses the board and builds a list of all the free squares;
# the list consists of tuples, while each tuple is a pair of row and column numbers
# def make_list_of_free_fields(board):
# List is empty originally
# free = []
# Now iterate through the rows
# for row in range(3):
# Now iterate through the columns
# for column in range(3):
# Check if the cell is now free
# if board[row][column] not in ['O', 'X']:
# If cell is free, append new tuple to the list
# free.append((row, column))
# return free

# The function analyzes the board's status in order to check if
# the player using '0's or 'X's has won the game
# def victory_for(board, sign):
# Look for 'X'
# if sign == "X":
# If yes it is the computer's side
# who = 'computer'
# Then sign == 0
# elif sign == "O":
# If yes it is the user's side
# who = 'you'
# else:
# Now who = None
# who = None
# Make cross1 = cross2 = True for diagonals
# cross1 = cross2 = True
# rc = row column
# for rc in range(3):
# Now check the row for rc
# if board[rc][0] == sign and board[rc][1] == sign and board[rc][2] == sign:
# return who
# Now check the column for rc
# if board[0][rc] == sign and board[1][rc] == sign and board[2][rc] == sign:
# return who
# Now check the first diagonal
# if board[rc][rc] != sign:
# cross1 = False
# Now check the second diagonal
# if board[2 - rc][2 - rc] != sign:
# cross2 = False
# if cross1 or cross2:
# return who
# return None

# The function draws the computer's move and updates the board
# def draw_move(board):
# List of free fields
# free = make_list_of_free_fields(board)
# choose = len(free)
# Make a if statement to choose a place for 'X' and set accordingly
# if choose > 0:
# his = randrange(choose)
# row, column = free[this]
# board[row][column] = 'X'

# Now make an empty board
# board = [[3 * h + i + 1 for i in range(3)] for h in range(3)]
# Always make the computers first 'X' in the middle
# board[1][1] = 'X'
# free = make_list_of_free_fields(board)

# Now check who's turn it is now (humans turn or computers turn)
# hturn = True
# while len(free):
# display_board(board)
# if hturn:
# enter_move(board)
# success = victory_for(board, 'O')
# else:
# draw_move(board)
# victory = victory_for(board, 'X')
# if success != None:
# break
# hturn = not hturn
# free = make_list_of_free_fields(board)

# display_board(board)
# Make a if elif statement in the display_board(board) function to print who won or
# if it is a tie
# if success == 'you':
# print("You won!")
# elif success == 'computer':
# print("Computer won")
# else:
# print("Tie!")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

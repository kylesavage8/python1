import random


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
    # Make two for loops one for range of 9 to print a grid & the other with a range of 6mto print another grid
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    text_art()
    coin_flip()
    # print_hi('PyCharm')
    # my_functionname()
    # my_functionnumber()
    # my_functionword()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # text_art()
    # coin_flip()
    # print_hi('PyCharm')
    # my_functionname()
    # my_functionnumber()
    # my_functionword()

    # Programming Assignment 4
    # Tic-tac-toe Functions

    from random import randrange


    # The function accepts one parameter containing the board's current status
    def display_board(board):
        print("+-------" * 3, "+", sep="")
        # Make a for loop for the row with a range of 3
        for row in range(3):
            # Print the row
            print("|       " * 3, "|", sep="")
            # Make a for loop for the column with a range of 3
            for column in range(3):
                # Print the column and the board
                print("|   " + str(board[row][column]) + "   ", end="")
            print("|")
            print("|       " * 3, "|", sep="")
            print("+-------" * 3, "+", sep="")


    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision
    def enter_move(board):
        # If the move is false, enter the loop
        okay = False
        while not okay:
            e_move = input("Enter your move: ")
            # Check if the user's input is valid
            okay = len(e_move) == 1 and e_move >= '1' and e_move <= '9'
            if not okay:
                # Print invalid move, repeat move again
                print("Invalid move - repeat move!")
                continue
            # The cell's number is from 0 to 8
            e_move = int(e_move) - 1
            # Displays the cell's row
            row = e_move // 3
            # Displays the cell's column
            column = e_move % 3
            # Now check the picked box
            sign = board[row][column]
            okay = sign not in ['O', 'X']
            if not okay:
                # Print field currently occupied
                print("Field currently occupied - repeat move!")
                continue
        # Now set '0' at the picked box
        board[row][column] = 'O'


    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers
    def make_list_of_free_fields(board):
        # List is empty originally
        free = []
        # Now iterate through the rows
        for row in range(3):
            # Now iterate through the columns
            for column in range(3):
                # Check if the cell is now free
                if board[row][column] not in ['O', 'X']:
                    # If cell is free, append new tuple to the list
                    free.append((row, column))
        return free


    # The function analyzes the board's status in order to check if
    # the player using '0's or 'X's has won the game
    def victory_for(board, sign):
        # Look for 'X'
        if sign == "X":
            # If yes it is the computer's side
            who = 'computer'
        # Then sign == 0
        elif sign == "O":
            # If yes it is the user's side
            who = 'you'
        else:
            # Now who = None
            who = None
        # Make cross1 = cross2 = True for diagonals
        cross1 = cross2 = True
        # rc = row column
        for rc in range(3):
            # Now check the row for rc
            if board[rc][0] == sign and board[rc][1] == sign and board[rc][2] == sign:
                return who
            # Now check the column for rc
            if board[0][rc] == sign and board[1][rc] == sign and board[2][rc] == sign:
                return who
            # Now check the first diagonal
            if board[rc][rc] != sign:
                cross1 = False
            # Now check the second diagonal
            if board[2 - rc][2 - rc] != sign:
                cross2 = False
        if cross1 or cross2:
            return who
        return None


    # The function draws the computer's move and updates the board
    def draw_move(board):
        # List of free fields
        free = make_list_of_free_fields(board)
        choose = len(free)
        # Make a if statement to choose a place for 'X' and set accordingly
        if choose > 0:
            this = randrange(choose)
            row, column = free[this]
            board[row][column] = 'X'


    # Now make an empty board
    board = [[3 * h + i + 1 for i in range(3)] for h in range(3)]
    # Always make the computers first 'X' in the middle
    board[1][1] = 'X'
    free = make_list_of_free_fields(board)

    # Now check who's turn it is now (humans turn or computers turn)
    hturn = True
    while len(free):
        display_board(board)
        if hturn:
            enter_move(board)
            success = victory_for(board, 'O')
        else:
            draw_move(board)
            victory = victory_for(board, 'X')
        if success != None:
            break
        hturn = not hturn
        free = make_list_of_free_fields(board)

    display_board(board)
    # Make a if elif statement in the display_board(board) function to print who won or
    # if it is a tie
    if success == 'you':
        print("You won!")
    elif success == 'computer':
        print("Computer won")
    else:
        print("Tie!")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

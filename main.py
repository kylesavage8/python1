import random
import datetime
import os
import sys
import re

# Programming Assignment 6
# String with branches
# To run these two programs you have to write text into the terminal. This file is not run by the "Run" button,
# To run the strings1_accept() function follow these steps:
# Step 1: In the terminal enter python main.py then type any written text
# Step 2: Make sure the strings1_manipulate() function in main is commented out.
# To run the strings1_manipulate() function follow these steps:
# Step 1: In the terminal enter python main.py then type the word test
# Step 2: In the terminal enter python main.py then type the word manipulate
# Step 3: In the terminal enter python main.py then input anything the function doesn't recognize
# Step 4: Make sure the strings1_accept() function in main is commented out.


def strings1_accept():
    # In the terminal enter python main.py then type any written text
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
    # In the terminal enter python main.py then type the word test
    if arg == "test":
        print("Strings1 Test")
    # In the terminal enter python main.py then type the word manipulate
    elif arg == "manipulate":
        print("Test is manipulated")
    # In the terminal enter python main.py then input anything the function doesn't recognize
    else:
        print("The argument is invalid")


if __name__ == '__main__':
    strings1_accept()
    strings1_manipulate()
    #string2_reading(user_input().split(" "))
    #strings3_apostrophe(user_input().split(" "))
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

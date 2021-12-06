# Programming Assignment 4
# Tic-tac-toe Functions
import random
import datetime
import os
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

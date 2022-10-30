from random import randint#importing random lib


hboard = [[" "] * 8 for x in range(8)] #hidden board
gboard = [[" "] * 8 for i in range(8)] #board for guessing/shooting

def print_board(board):#function that visually draws the board in the console
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:#loop that is visualising all the rows and columns
        print (row_number, end="|")
        for column in row:
            print(column, end="|")
        row_number += 1
        print()

let_conv_to_num = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
} # letter convertation table for array indexes
def creatingships(board, count): # creating ships
    for ship in range(count):
        board[randint(0,7)][randint(0,7)] = "X" #random value for each ship coordinates

def gettinglocation():
    row = input("enter the row(1-8): ")
    while row not in "12345678":#showing mistake if written incorrect value
        print('select a valid one')
        row = input("enter the row(1-8): ")
    column = input("enter the column(A-H,caps please): ")
    while column not in "ABCDEFGH":#showing mistake if written incorrect value
        print('select a valid one')
        column = input("enter the column(A-H,caps please): ")
    return int(row) - 1, let_conv_to_num[column]

#checking if all ships are hitted
def shipshitting(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

if __name__ == "__main__":#used to execute some code only if the file was run directly, and not imported
    creatingships(hboard, 15)# game is creating up to x ships where x is value written after hboard
    turns = 32 #can be changed to any value
    while turns > 0:
        print('guess a ship location')
        print_board(gboard)
        row, column = gettinglocation()
        if gboard[row][column] == "-":
            print("already guessed")
        elif hboard[row][column] == "X":
            print("hitted")
            gboard[row][column] = "X" 
            turns -= 1  
        else:
            print("missed!")
            gboard[row][column] = "-"   
            turns -= 1     
        if shipshitting(gboard) == 5:#checking if 5 ships are hitted for winning
            print("you win, congrats")
            break
        print("You have " + str(turns) + " turns left")
        if turns == 0:#losing if 
            print("you losed,try again")
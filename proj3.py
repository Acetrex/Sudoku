# File: proj3.py
# Name: Alex Tran
# Date: 11/28/18
# Section: 05
# e-mail: ptran7@umbc.edu
# Description:
#       This program will be programming up a text-based version of the popular Sudoku \
#       puzzle game. The goal of the game is to place the digits from 1-9 in each cell \
#       of the board such that no two digits repeat in the same row, column, or 3x3 \
#       square (it's called a nonet!). The game is won if you are able to find this \
#       unique combination of digit placement, given some starting configuration of \
#       digits on the board.

## CONSTANTS ##

# play the puzzle

PLAY = "p"

# solve the puzzle

SOLVEPUZZLE = "s"

# does not solve the puzzle

NOTSOLVEPUZZLE = "n"

# the highest integer the user is able to input

MAXNUM = 9

# the lowest integer the user is able to input

MINNUM = 1

# nonet size

NONET = 3

## BREAKING GRID TO 3 X 3 PIECES

GRIDONE = 3

GRIDTWO = 6

GRIDTHREE = 9

# empty space in the puzzle:

EMPTYSPACE = "0"

# saving the puzzle

SAVE = "s"

# quit the game, Soduku

QUIT = "q"

# undo the previous step

UNDO = "u"

# check input to puzzle
PUZZLECHECK = "y"

# not valid checking what the user is inputting to the board
NOTPUZZLECHECK = "n"

# runs the number up to MAXSUDOKUNUM but not inclusive of MAXSUDOKUNUM 
MAXSUDOKUNUM = 10
## FUNCTIONS ##

# validationCheck():         Checks userValues entered to be in range of sudoku numbers
# Input:                     rows; the row value the user is wishing to insert a value to
#                            columns; the column value the user is wishing to insert an integer to
#                            integer; the users integer number to the space
# Output:                    returns True / False; if the number is not in range or if the number is in range

def validationCheck(num):
    while num > MAXNUM or num < MINNUM:
        print("That is out of range of sudoku number")
        num =  int(input("Enter a between number ("+str(MINNUM)+"-"+str(MAXNUM)+"): "))
    return(num)
        

# undo()                     reverse the previous input of the user through referring to a list
# Input:                     rowList; the row the user input their previous integer
#                            columnList; the column the user input their previous integer
#                            board; the board in order to remove the piece that was place
# Ouput:                     returns the board to the previous state

def undo(board,rowList,columnList):
    row = rowList[len(rowList) - 1]
    column = columnList[len(columnList) - 1]

    board[row-1][column-1] = EMPTYSPACE

    return(board)

# menuDisplay():             displays the menu and returns the user input of what user is wishing to do
# Input:                     None; prints a statement and ask for user input
# Output:                    returns user Choice; the command the user is asking to do
 
def menuDisplay():
    menuChoice =  input("play number ("+PLAY+") save ("+SAVE+"), undo ("+UNDO+"), quit ("+QUIT+"): ")
    print()
    
    #validates menuChoice
    while menuChoice != PLAY and menuChoice != UNDO and menuChoice != SAVE and menuChoice != QUIT:
        print("that is an invalid menu Choice")
        menuChoice =  input("play number("+PLAY+") save ("+SAVE+"), undo ("+UNDO+"), quit ("+QUIT+"): ")
        print()

    return(menuChoice)
# emptySpot():              finds the spot that is empty on the board
# Input:                    board; the board to check if there is a empty space
# Output:                   return True or False; if there are a coordinate that has an empty space then return True
#                           else return False
def emptySpot(board, cordList):
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == EMPTYSPACE:
                cordList[0] = row
                cordList[1] = column
                return 

# fullBoard()               determines if the board is full
# Input:                    None; the puzzleList is going to be in reference
# Output:                   returns True or False; if there is still an empty space on the board then return True
#                           if there is not a empty space anymore then return false
def fullBoard(board):
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == EMPTYSPACE:
                return True
    return False

### BULK OF THE PROGRAM ###
# solve():                   solves the board recursively before the user is filling the board with integers
# Input:                     None; the puzzle list is referenced
# Output:                    a filled and complete solved board in order to be used or compared to

def solve(board):
#    if EMPTYSPACE not in board:
#        return True
    # coordinatees for the zero
    cordList = [0,0]
    
    solveBoard = fullBoard(board)
    
    if solveBoard == False:
        return True
    
    emptySpot(board,cordList)

    row = cordList[0]
    column = cordList[1]
    # loops through the board and inputs a number where it is possible     
    for num in range(1, MAXSUDOKUNUM):
        
        # validates that num through sudoku rules
        validRow = checkRow(board, row, num)

        validCol = checkCol(board, column, num)

        validNonet = validInNonet(board,row,column, num)

        # the num is valid to be placed into the space
        if validRow == False and validCol == False and validNonet == False:
            
            board[row][column] = str(num)

            validInBoard = solve(board)
            # RECURSIVE CALL
            if validInBoard == True:
    
                return True
            
            # resets the space to an empty spot
            else:
                board[row][column] = EMPTYSPACE
        
    return False

#def checkRow()              checks the row if there is already the number in the row
# Input:                     board; the board
#                            row; the user row
#                            num; the user number that is wished to be inserted into that row
# Ouput:                     returns False: if false, then that means that the row is filled with that num in the row

def checkRow(board,rowChoice,num):
    
    for index in range(MAXNUM):
        # if the number is in the row
        if board[rowChoice][index] == str(num):
            return(True)
    return(False)

# checkCol()                 checks the column if there is already the number in the column
# Input:                     board; the board
#                            column; the user input of their column
# Ouput:                     returns False; if the number is invalid to be put in the space

def checkCol(board,columnChoice,num):
    
     for index in range(MAXNUM):
         # if the number is in the column
         if board[index][columnChoice] == str(num):
             return(True)
     return(False)

# def validInNonet()           checks if the number of the user can be inserted inside the nonet
# Input:                     row; the row in reference to the nonet
#                            column; the column in reference to the nonet
#                            integer; the number in reference to the nonet
# Output:                    returns True or False; if the number is not able to be inserted into the nonet or if it is

def validInNonet(board,rowChoice,columnChoice,num):
    # finds the new row
    row = rowChoice % NONET
    
    newRow = rowChoice - row
    # finds the new column
    column = columnChoice % NONET

    newColumn = columnChoice - column
    
    # checks if the nonet has the number
    for x in range(newRow, newRow + NONET):
        for y in range(newColumn, newColumn+ NONET):
            # if the number is in the Nonet
            if board[x][y] == str(num):
                return(True)
    # if there is no problem with the num in the nonet
    return(False)

# boardDeepCopy():           develops a deep copy of the board to update per new integer on the puzzle
# Input:                     board; original board
# Output:                    returns a board that will be use to update and change

def boardDeepCopy(board):
    deepBoard = []
    for row in range(len(board)):
        deepRow = []
        
        for column in range(len(board[row])):
            
            deepRow.append(board[row][column])
            
        deepBoard.append(deepRow)
        
    return(deepBoard)
    
# prettyPrint() prints the board with row and column labels,
#               and spaces the board out so that it looks nice
# Input:        board;   the square 2d game board (of integers) to print
# Output:       None;    prints the board in a pretty way

def prettyPrint(board):
    # print column headings and top border
    print("\n    1 2 3 | 4 5 6 | 7 8 9 ")
    print("  +-------+-------+-------+")
    for i in range(len(board)):
        # convert "0" cells to underscores  (DEEP COPY!!!)
        boardRow = list(board[i])
        for j in range(len(boardRow)):
            if boardRow[j] == EMPTYSPACE:
                boardRow[j] = "_"
        # fill in the row with the numbers from the board                                                                                                        
        print( "{} | {} {} {} | {} {} {} | {} {} {} |".format(i + 1,
                boardRow[0], boardRow[1], boardRow[2],
                boardRow[3], boardRow[4], boardRow[5],
                boardRow[6], boardRow[7], boardRow[8]) )
        # the middle and last borders of the board
        if (i + 1) % 3 == 0:
            print("  +-------+-------+-------+")
            
# savePuzzle() writes the contents a sudoku puzzle out
#              to a file in comma separated format
# Input:       board;    the square 2d puzzle (of integers) to write to a file
#              fileName; the name of the file to use for writing to
def savePuzzle(board, fileName):
    ofp = open(fileName, "w")
    for i in range(len(board)):
        rowStr = ""
        for j in range(len(board[i])):
            rowStr += str(board[i][j]) + ","
        # don't write the last comma to the file
        ofp.write(rowStr[ : len(rowStr)-1] + "\n")
    ofp.close()
    
def main():

    # asks user which puzzle they want to play
    puzzleChoice = input("Enter the filename of the sudoku puzzle: ")

    puzzleFile = open(puzzleChoice)
    
    puzzleLines = puzzleFile.readlines()
    
    puzzleFile.close()

    # creates a 2D list from the puzzle file
    
    puzzleList = []
    
    for index in range(len(puzzleLines)):
        rows = puzzleLines[index].strip()
        newRows = rows.split(",")

        puzzleList.append(newRows)
    
    puzzleBoard = boardDeepCopy(puzzleList)
    
    if solve(puzzleList):

        prettyPrint(puzzleBoard)
        
    userChoice = input("play ("+PLAY+") or solve ("+SOLVEPUZZLE+")? ")
    
    # validates userChoice
    while userChoice != PLAY and userChoice != SOLVEPUZZLE:
        
        print("That is not a choice")
        
        userChoice = input("play ("+PLAY+") or solve ("+SOLVEPUZZLE+")? ")
        
    # user choice is to see the solved sudoku board
    if userChoice == SOLVEPUZZLE:

            prettyPrint(puzzleList)
        
    # user choice is to play the sudoku puzzle
    elif userChoice == PLAY:
        rowMove = []
        
        colMove = []
        
        moveList = []

        piecePlace = []
        
        menuChoice = ""
        
        gameRunning = True
        
        menuOption = ""
        
        solutionSwitch = ""

        win = False
    
        
        # if the user wants to check if the input is correct
        solutionCheck = input("correctness checking? ("+PUZZLECHECK+"/"+NOTPUZZLECHECK+"): ")
        
        # input validation of solution checking choice
        while solutionCheck != PUZZLECHECK and solutionCheck != NOTPUZZLECHECK:
            print("that is an invalid answer")
            solutionCheck = input("correctness checking? ("+PUZZLECHECK+"/"+NOTPUZZLECHECK+"): ")
        # user does want to check their input  value to the board
        if solutionCheck == PUZZLECHECK:
            solutionSwitch = True
        # user does not want to check their input value to the board
        elif solutionCheck == NOTPUZZLECHECK:
            solutionSwitch = False
            
        while menuChoice != QUIT and win == False:
                
            fullSudokuBoard = fullBoard(puzzleBoard)

            for row in range(len(puzzleBoard)):
                for column in range(len(puzzleBoard[row])):
                    if puzzleBoard[row][column] == puzzleList[row][column] and fullSudokuBoard == False:
                        win = True
                        menuOption = "j"

            if win == False:
                prettyPrint(puzzleBoard)
                menuOption = menuDisplay()
                
            if menuOption == PLAY:
                rowChoice = int(input("Enter a row number ("+str(MINNUM)+"-"+str(MAXNUM)+"): "))
                # returned valid num in range of rows
                rowNum = validationCheck(rowChoice)
                
                colChoice =  int(input("Enter a column number ("+str(MINNUM)+"-"+str(MAXNUM)+"): "))
                # returned valid num in range of column
                colNum = validationCheck(colChoice)
                
                numChoice =  int(input("Enter a number to put in cell ("+str(rowNum)+","+str(colNum)+"): "))                    
                
                # return valid num in range of integer in range of soduku numbers
                validNum  = validationCheck(numChoice)
                
                # checks if the number is not in row
                validRow = checkRow(puzzleBoard,rowNum-1,validNum)
                
                # checks if the number is not in column
                validCol = checkCol(puzzleBoard,colNum-1,validNum)

                # checks if the number is not in nonet
                validNonet = validInNonet(puzzleBoard,rowNum-1,colNum-1,validNum)

                if solutionSwitch == True:
                        
                    puzzleBoard[rowNum-1][colNum-1] = str(validNum)
                        
                    if puzzleList[rowNum-1][colNum-1] != puzzleBoard[rowNum-1][colNum-1]:

                        print("OOPS!", str(validNum),"does not belong in position("+str(rowNum)+","+str(colNum)+")!")
            
                        puzzleBoard[rowNum-1][colNum-1] = EMPTYSPACE
                            
                    elif puzzleList[rowNum-1][colNum-1] == puzzleBoard[rowNum-1][colNum-1]:
                        
                        puzzleBoard[rowNum-1][colNum-1] = validNum
                        
                        rowMove.append(rowNum)

                        colMove.append(colNum)

                        piecePlace.append(validNum)
                            
                else:
                    # a number is in the space
                    if puzzleBoard[rowNum-1][colNum-1] != EMPTYSPACE:
                            
                        numIns = puzzleBoard[rowNum-1][colNum-1]
                        print()
                        print(numIns,"is in the space already")
                    else:
                        print()
                        # if the num is in row
                        if validRow == True:
                            
                            print("The number",validNum,"is already in that row")
                        
                        # if the num is in column    
                        if validCol == True:
                        
                            print("The number",validNum,"is already in that column")
                        
                        # if the num is in the nonet
                        if validNonet == True:
                        
                            print("The number",validNum,"is already in that square")
                            
                        # only inputs the value to the board if sudoku conditions are false; the value does not interfere with the rules
                        if validRow == False and validCol == False and validNonet == False \
                           and puzzleBoard[rowNum-1][colNum-1] == str(0):
                        
                            rowMove.append(rowNum)
                        
                            colMove.append(colNum)
                        
                            piecePlace.append(validNum)
                            
                            puzzleBoard[rowNum-1][colNum-1] = validNum
                        
            # user wants to save their    
            elif menuOption == SAVE:
                # save board to a new file name
                saveFileName = input("Enter the filename you want to save to: ")
                savePuzzle(puzzleBoard,saveFileName)
            # user chooses to remove their piece from the board
            elif menuOption == UNDO:
                # if the there is no move to undo
                if len(rowMove) == 0 and len(colMove) == 0:
                    print("There is no moves to undo!")
                # undo the previous move
                else:
                    print("Removed the,",piecePlace[len(piecePlace)-1],"you played at position(",rowMove[len(rowMove)-1],",",colMove[len(colMove)-1],")")
                        
                    puzzleBoard = undo(puzzleBoard, rowMove, colMove)
                        
                    rowMove.remove(rowMove[len(rowMove)-1])
                        
                    colMove.remove(colMove[len(colMove)-1])
                              
                    piecePlace.remove(piecePlace[len(piecePlace)-1])
                        
            # if choice is QUIT, then it exits the loop of playing the sudoku puzzle
            elif menuOption == QUIT:
                menuChoice = QUIT
                                
        # prints out the board at the current state
        if menuChoice == QUIT:
            print("Good bye! Here is your final Board: ")
            prettyPrint(puzzleBoard)
        
        # if the user wins
        if win == True:
            prettyPrint(puzzleBoard)
            print("You win!", "\n")
        
main()

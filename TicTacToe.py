# This is a tic tac toe game

# Insert letter function
def insertLetter(letter, pos):
    board[pos] = letter

# Check if the space is available
def spaceIsFree(pos):
    return board[pos] == ' '

# Prints out board in a text format
def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

# Checks these conditions to find winner
def isWinner(brd, full):
    return (brd[7] == full and brd[8] == full and brd[9] == full) or (
                brd[4] == full and brd[5] == full and brd[6] == full) or (
                       brd[1] == full and brd[2] == full and brd[3] == full) or (
                       brd[1] == full and brd[4] == full and brd[7] == full) or (
                       brd[2] == full and brd[5] == full and brd[8] == full) or (
                       brd[3] == full and brd[6] == full and brd[9] == full) or (
                       brd[1] == full and brd[5] == full and brd[9] == full) or (
                       brd[3] == full and brd[5] == full and brd[7] == full)

# Player function
def playerMove():
    run = True
    while run:
        move = input('Please choose a position from 1-9: ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('This space is occupied')
            else:
                print('Please enter a number in the range 1-9: ')
        except:
            print('Please enter a number')

# Computer opponent
def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for ltr in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = ltr
            if isWinner(boardCopy, ltr):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move

# Choose a random number for the AI
def selectRandom(lst):
    import random
    ln = len(lst)
    r = random.randrange(0, ln)
    return lst[r]

# Check if board is full
def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

# Main function of playing the game
def main():
    printBoard(board)
    while not (isBoardFull(board)):
        if not (isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('O\'s won this time')
            break

        if not (isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Tie Game')
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position', move, ' ')
                printBoard(board)
        else:
            print('X\'s won this time')
            break

# The ability to replay
def replay():
    playAgain = input('Would you like to play again? Y or N: ')
    if playAgain == 'Y':
        main()
        replay()
    else:
        print('Thank you for playing')

# Start the game
print('Welcome to tic tac toe')
play = input('Would you like to start? Y or N: ')
if play == 'Y':
    board = [' ' for x in range(10)]
    main()
    # Reset the board and ask to replay
    board = [' ' for x in range(10)]
    replay()
else:
    print('Come Again!')

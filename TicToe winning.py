theBoard = {'A1': ' ', 'B1': ' ', 'C1': ' ',
            'A2': ' ', 'B2': ' ', 'C2': ' ',
            'A3': ' ', 'B3': ' ', 'C3': ' '}

def printBoard(board):
    print(board['A1'] + '|' + board['B1'] + '|' + board['C1'])
    print('-+-+-')
    print(board['A2'] + '|' + board['B2'] + '|' + board['C2'])
    print('-+-+-')
    print(board['A3'] + '|' + board['B3'] + '|' + board['C3'])
printBoard(theBoard)


chance = 0
turn = 'X'
win = False
while chance <9 and win == False :
    print("Your Turn Mr." + turn + " .Move to which space   ")
    move = input()
    theBoard[move] = turn
    chance = chance +1
    if turn == 'X':
        turn = "O"
    else:
        turn = 'X'

    printBoard(theBoard)

    for i in range(1,4):
        if(i==1):
            if theBoard['A' + str(i)] == theBoard['B' + str(i+1)] == theBoard['C' + str(i+2)] == "X"  :
                print("Mr.X wins")
                win = True
                break
            elif theBoard['A' + str(i)] == theBoard['B' + str(i+1)] == theBoard['C' + str(i+2)] == "O":
                print("Mr.O wins")
                win = True
                break

        if theBoard['A'+str(i)] == theBoard['B'+str(i)] == theBoard['C'+str(i)] == "X" :
            print("Mr.X wins"  )
            win = True
            break
        elif theBoard['A'+str(i)] == theBoard['B'+str(i)] == theBoard['C'+str(i)] == "O":
            print("Mr.O Wins")
            win = True
            break

import random

global playerX ,playerO,chance,theBoard
theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}
playerGod ='X'
playerHuman = 'O'
chance = 1

def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


def win(sign):
    return ((theBoard['1'] == sign and theBoard['2'] == sign and theBoard['3'] == sign) or \
    (theBoard['4'] == theBoard['5'] == theBoard['6'] == sign) or \
    (theBoard['7'] == theBoard['8'] == theBoard['9'] == sign) or \
    (theBoard['1'] == theBoard['4'] == theBoard['7'] == sign) or \
    (theBoard['2'] == theBoard['5'] == theBoard['8'] == sign) or \
    (theBoard['3'] == theBoard['6'] == theBoard['9'] == sign) or \
    (theBoard['1'] == theBoard['5'] == theBoard['9'] == sign) or \
    (theBoard['3'] == theBoard['5'] == theBoard['7'] == sign))


def firstchance():
    if random.randint(0,9) == 0:
        return playerHuman
    else:
        return  playerGod

def play(turn,chance):
    global player

    if player == playerHuman:
        print("Where do you want to put your ", player ," sign Mr. Human")
        move = input()
        theBoard[move] = playerHuman
        printBoard(theBoard)
        player=playerGod
        if win(player) == True:
         print("You won Mr.Human")
         return True
        else:
            player = playerGod
            return False

    elif player == playerGod:

        if chance == 1:
            theBoard['1'] = playerGod
            printBoard(theBoard)
            player = playerHuman
            return False

        elif chance == 2:

        player = playerHuman
        return False

def checkcenter():
    return (theBoard[5]== 'O')

def checkcorner():

#Game starts From here


player = playerHuman
print("Mr.",firstchance(), "will go First")
if(firstchance() == 'X'):
    player = playerGod
while (chance < 9):

    if play(player,chance) == True:
        break
    chance = chance + 1









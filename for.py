theBoard = {'1': '1', '2': '1', '3': '1',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}


def win(sign):
    return ((theBoard['1'] == sign and theBoard['2'] == sign and theBoard['3'] == sign) or \
    (theBoard['4'] == theBoard['5'] == theBoard['6'] == sign) or \
    (theBoard['7'] == theBoard['8'] == theBoard['9'] == sign) or \
    (theBoard['1'] == theBoard['4'] == theBoard['7'] == sign) or \
    (theBoard['2'] == theBoard['5'] == theBoard['8'] == sign) or \
    (theBoard['3'] == theBoard['6'] == theBoard['9'] == sign) or \
    (theBoard['1'] == theBoard['5'] == theBoard['9'] == sign) or \
    (theBoard['3'] == theBoard['5'] == theBoard['7'] == sign))

#result = win('1')
print(win('1'))
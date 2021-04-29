


board = [1,2,3,4,5,6,7,8,9]

def drawboard(board):
    for index, item in enumerate(board[0:len(board)],start=1):
        print(item,end=' | ' if index %3 else '\n')


def getplayermarkerchoice():
    choice_made =False
    while not choice_made:
        marker=input("Enter X or O for marker choice: ")
        if marker =='X' or marker=='O':
            choice_made = True
    return marker        


import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'X'
    else:
        return 'O'

def setmarker(board, marker, position):
    board[position] = marker


#getplayermarkerchoice()

def checkwinstatus(marker):
    return (board[0]== marker and board[1]==marker and board[2] == marker) or (board[3]== marker and board[4]==marker and board[5] == marker) or (board[6]== marker and board[7]==marker and board[8] == marker) or (board[0]== marker and board[4]==marker and board[8]==marker) or (board[2]== marker and board[5]==marker and board[6]==marker) or (board[2]== marker and board[6]==marker and board[9]==marker) or (board[0]== marker and board[3]==marker and board[6]==marker) or (board[1]== marker and board[4]==marker and board[7]==marker)


def playgame():
    print('Welcome to Tic Tac Game')
    moves = 0
    board = [1,2,3,4,5,6,7,8,9]
    player1 = getplayermarkerchoice()
    player2 = 'O' if player1 == 'X' else 'X'

    print(player1)
    print(player2)

    choice = input('Are you ready to play the game? Y or N :')
    print(choice)
    if(choice.lower()=='y'):
        game_on=True
    else:
        game_on=False    
    

    player = choose_first()

    while game_on:
        drawboard(board)
        if 
        game_on=False


playgame()

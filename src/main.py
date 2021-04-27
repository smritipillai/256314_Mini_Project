#Tic Tac Toe Game

''' Defining a dictionary to save the moves made by the players,
    to prevent repetition of the same moves '''

board = { 1: ' ' , 2: ' ' , 3: ' ' ,
          4: ' ' , 5: ' ' , 6: ' ' ,
          7: ' ' , 8: ' ' , 9: ' ' }

def resetBoard():
    board = { 1: ' ' , 2: ' ' , 3: ' ' ,
              4: ' ' , 5: ' ' , 6: ' ' ,
              7: ' ' , 8: ' ' , 9: ' ' }

''' We make a call to this function after everytime the player makes a move, to keep the players updated '''
def boardStatus(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])

keys = []

for i in board:
    keys.append(i)

# main function has the logic 
def main():

    print("Let the game begin!")
    resetBoard()
    turn = 'X'
    count = 0


    for i in range(10):
        print("-------------------------------")
        boardStatus(board)
        print("-------------------------------")
        print("It's " + turn + " turn. Enter a postion!")
        move = input()        

        if board[move] == ' ':
            board[move] = turn
            count += 1
        else:
            print("It's already used number. Enter another postion!")
            continue

        

if __name__ == "__main__":
    main()
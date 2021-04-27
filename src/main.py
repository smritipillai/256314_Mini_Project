#Tic Tac Toe Game

''' Defining a dictionary to save the moves made by the players,
    to prevent repetition of the same moves '''

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

        # Check if any of the players has won the game yet. 
        if count >= 5:
            if board[1] == board[2] == board[3] != ' ': # across the top
                print("-------------------------------")
                boardStatus(board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****") 
                print("-------------------------------")               
                break
            elif board[4] == board[5] == board[6] != ' ': # across the middle
                print("-------------------------------")
                boardStatus(board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                print("-------------------------------")
                break
            elif board[7] == board[8] == board[9] != ' ': # across the bottom
                print("-------------------------------")
                boardStatus(board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                print("-------------------------------")
                break
            elif board[1] == board[4] == board[7] != ' ': # down the left side
                boardStatus(board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif board[2] == board[5] == board[8] != ' ': # down the middle
                print("-------------------------------")
                boardStatus(board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                print("-------------------------------")
                break
            elif board[3] == board[6] == board[9] != ' ': # down the right side
                print("-------------------------------")
                boardStatus(board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                print("-------------------------------")
                break 
            elif board[7] == board[5] == board[3] != ' ': # diagonal
                print("-------------------------------")
                boardStatus(board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                print("-------------------------------")
                break
            elif board[1] == board[5] == board[9] != ' ': # diagonal
                print("-------------------------------")
                boardStatus(board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                print("-------------------------------")
                break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("-------------------------------")
            print("\nGame Over.\n")                
            print("It's a Tie!!")
            print("-------------------------------")

        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Now we will ask if player wants to play again or not.
    again = input("Do want to play Again?(y/n)")
    if again == 'Y' or again == 'y':  
        resetBoard()
        main()

if __name__ == "__main__":
    main()
'''An TIC TAC TOE GAME IMPLEMENTATION MADE BY ME ITSELF.'''

# Import the random module to generate random numbers
import random

# Function to add three numbers
def sum_three(a, b, c):
    return a + b + c

# Function to print the indices of the board
#------------------------------------------
# another way to write below statement.
# def print_board_indices():
#     print(f'----------')
#     print(f'0 | 1 | 2 ')
#     print(f'--|---|---')
#     print(f'3 | 4 | 5 ')
#     print(f'--|---|---')
#     print(f'6 | 7 | 8 ')
#     print(f'----------')

def print_board_indices():
    print('----------')
    for i in range(3):
        print(f'{3*i} | {3*i + 1} | {3*i + 2} ')
        if i < 2:
            print('--|---|---')
    print('----------')

# Function to print the current state of the board
#------------------------------------------
# another way to write below statement.

# for i in range(9):
#     if xState[i]:
#         board[i] = 'X'
#     elif oState[i]:
#         board[i] = 'O'
# for i in range(3):
#     row = board[i * 3 : (i + 1) * 3]
#     print(" | " + " | ".join(row) + " |")
def print_board(xState, oState):
    # Create a list representing the board
    board = ['X' if xState[i] else 'O' if oState[i] else ' ' for i in range(9)]
    for i in range(3):
        print(" | " + " | ".join(board[i * 3 : (i + 1) * 3]) + " | ")
    print('----------')

# Function to take the user's choice of 'X' or 'O'
def take_options():
    user_input = input('Choose the option you want to take, X or O: ').upper()
    if user_input == 'X' or user_input == 'O':
        print(f'Your chosen option is {user_input}')
        print('Your chance')
        return user_input
    else:
        print('Invalid option. Please choose X or O.')
        return take_options()

# Function to check if there is a winner or a tie
def check_win(xstate, ostate):
    # List of winning combinations
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [2, 4, 6], [0, 4, 8]]
    
    # Check for a win
    for win in wins:
        if sum_three(xstate[win[0]], xstate[win[1]], xstate[win[2]]) == 3:
            print('X won the match.')
            return 1
        elif sum_three(ostate[win[0]], ostate[win[1]], ostate[win[2]]) == 3:
            print('O won the match.')
            return 0
    
    # Check for a tie
    if all(xstate[i] or ostate[i] for i in range(9)):
        print('It was a tie. The match is over.')
        return -1
    
    return -1  # continue the game

# Function for the computer to make a move
def computer_move(xState, oState):
    # List of available moves
    available_moves = [i for i in range(9) if not xState[i] and not oState[i]]
    
    # Return a random available move
    computer_choice = random.choice(available_moves) if available_moves else None
    if computer_choice is not None:
        print(f"Computer chooses position {computer_choice}.")
    else:
        print("No available moves for the computer.")
    
    return computer_choice

# Function to ask if the user wants to play another round
def play_one_more_time():
    play_again = input('The match is over. Do you want to play another round? (yes/no) ')
    return play_again.lower() == 'yes'

# Main part of the program
if __name__ == "__main__":
    # Initialize the states of 'X' and 'O'
    xState = [0] * 9
    oState = [0] * 9
    
    # Take the user's choice of 'X' or 'O'
    user_option = take_options()
    
    # Initialize the turn based on the user's choice
    turn = 1 if user_option == 'X' else 0
    
    print('Welcome to Tic Tac Toe.')
    print_board_indices()
    
    # Game loop
    while True:
        print_board(xState, oState)
        win_status = check_win(xState, oState)
        
        if turn == 1:  # user's turn
            print("Your Chance or user's chance.")
            while True:
                try:
                    value = int(input("Please enter a value (0-8): "))
                    if 0 <= value <= 8 and not xState[value] and not oState[value]:
                        break
                    else:
                        print("Invalid position. Please choose an empty position between 0 and 8.")
                except ValueError:
                    print("That's not a valid number. Please try again.")
            xState[value] = 1 if user_option == 'X' else 0
            oState[value] = 1 if user_option == 'O' else 0
        else:  # computer's turn
            print("computer's turn")
            value = computer_move(xState, oState)
            if value is None:  # no available moves left
                break
            xState[value] = 1 if user_option == 'O' else 0
            oState[value] = 1 if user_option == 'X' else 0
        
        win_status = check_win(xState, oState)
        
        if win_status != -1:  # game over
            print('Match over')
            print_board(xState, oState)
            
            if win_status == -1 and play_one_more_time():  # ask for another round if it's a tie
                # Reset the game state
                xState = [0] * 9
                oState = [0] * 9
                turn = 1 if user_option == 'X' else 0
                print('\nNew Round:')
                print_board_indices()
                continue  # continue to the next round
            elif win_status != -1 and play_one_more_time():  # ask for another round in other cases
                # Reset the game state
                xState = [0] * 9
                oState = [0] * 9
                turn = 1 if user_option == 'X' else 0
                print('\nNew Round:')
                print_board_indices()
                continue  # continue to the next round
            else:
                break  # end the program if the user doesn't want to play again
        
        turn = 1 - turn  # switch turns
    
    print('Thanks for playing!')
    print_board_indices()
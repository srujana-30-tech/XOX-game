import random

board = [" " for _ in range(9)]

def print_board():
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        print("-" * 5)

def check_winner(player):
    win_positions = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a,b,c in win_positions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def is_draw():
    return " " not in board

def player_move():
    move = int(input("Enter your move (1-9): ")) - 1
    if move < 0 or move > 8 or board[move] != " ":
        print("Invalid move. Try again.")
        return player_move()
    board[move] = "X"

def computer_move():
    empty_positions = [i for i in range(9) if board[i] == " "]
    move = random.choice(empty_positions)
    board[move] = "O"
    print(f"Computer chose position {move+1}")

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("Positions are numbered 1 to 9\n")
    print_board()

    while True:
        player_move()
        print_board()

        if check_winner("X"):
            print("You win!")
            break
        if is_draw():
            print("It's a draw!")
            break

        computer_move()
        print_board()

        if check_winner("O"):
            print("Computer wins!")
            break
        if is_draw():
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()

    

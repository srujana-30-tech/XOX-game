# 🎮 Tic-Tac-Toe Game in Python

## 📌 Description

This is a simple **Tic-Tac-Toe game** developed using Python. The player plays against the computer on a 3×3 board.

The player uses **X**, while the computer uses **O**. The computer randomly selects an available position for its move.

The game continues until either the player wins, the computer wins, or the game ends in a draw.

## ✨ Features

* 🎮 Player vs Computer gameplay
* ❌ Player uses `X`
* ⭕ Computer uses `O`
* 🎲 Computer makes random moves
* 🏆 Automatically checks for a winner
* 🤝 Detects draw situations
* ⚠️ Validates player moves
* 🔢 Positions are numbered from 1 to 9
* 💻 Simple command-line interface

## 🛠️ Technologies Used

* **Python 3**
* **random module**

## 📂 Project Structure

```text
Tic-Tac-Toe/
│
├── tic_tac_toe.py
└── README.md
```

## ▶️ How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

Check the installation using:

```bash
python --version
```

### 2. Run the Program

Open the terminal or command prompt in the project folder and run:

```bash
python tic_tac_toe.py
```

## 🎯 How to Play

The game uses the following position numbers:

```text
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

Enter the number of the position where you want to place your `X`.

For example:

```text
Enter your move (1-9): 5
```

The computer will then randomly select an empty position and place `O`.

## 🧠 How the Program Works

### 1. Board Creation

The game creates a list containing 9 empty spaces:

```python
board = [" " for _ in range(9)]
```

Each element represents one position on the Tic-Tac-Toe board.

### 2. Displaying the Board

The `print_board()` function displays the board in a 3×3 format.

```python
def print_board():
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        print("-" * 5)
```

### 3. Checking the Winner

The `check_winner()` function checks all possible winning combinations.

There are 8 possible winning combinations:

* 3 rows
* 3 columns
* 2 diagonals

Example:

```text
X | X | X
---------
  | O |
---------
O |   | O
```

Here, `X` wins because all three positions in the first row contain `X`.

### 4. Checking for a Draw

The `is_draw()` function checks whether there are no empty spaces remaining on the board.

```python
def is_draw():
    return " " not in board
```

If the board is full and nobody has won, the game ends in a draw.

### 5. Player Move

The `player_move()` function asks the player to enter a position between 1 and 9.

It also checks whether:

* The position is valid.
* The position is not already occupied.

The player's symbol is `X`.

### 6. Computer Move

The `computer_move()` function finds all empty positions and randomly chooses one.

```python
empty_positions = [i for i in range(9) if board[i] == " "]
move = random.choice(empty_positions)
```

The computer then places `O` in the selected position.

### 7. Main Game Loop

The `play_game()` function controls the complete game.

The sequence is:

```text
Player Move
     ↓
Check Player Winner
     ↓
Check Draw
     ↓
Computer Move
     ↓
Check Computer Winner
     ↓
Check Draw
     ↓
Repeat
```

## 📋 Example Gameplay

```text
Welcome to Tic-Tac-Toe!
Positions are numbered 1 to 9

 | | 
-----
 | | 
-----
 | | 
-----

Enter your move (1-9): 5

 | | 
-----
 |X| 
-----
 | | 
-----

Computer chose position 1

O| | 
-----
 |X| 
-----
 | | 
-----
```

The game continues until a player wins or the board becomes full.

## ⚠️ Invalid Moves

If the player enters an invalid position or chooses an occupied position, the program displays:

```text
Invalid move. Try again.
```

The player is then asked to enter another position.

## 🏆 Winning Conditions

A player wins when they get three of their symbols in:

### Row

```text
X | X | X
---------
  |   |
---------
  |   |
```

### Column

```text
X |   |
---------
X |   |
---------
X |   |
```

### Diagonal

```text
X |   |
---------
  | X |
---------
  |   | X
```

## 📚 Python Concepts Used

This project demonstrates the following Python concepts:

* Lists
* Functions
* `for` loops
* `while` loops
* `if` conditions
* Tuples
* List comprehensions
* User input
* Type conversion using `int()`
* Recursion for retrying invalid moves
* The `random` module
* String formatting using f-strings
* Main program execution using:

```python
if __name__ == "__main__":
```

## 🚀 Future Improvements

The game can be improved by adding:

* Difficulty levels
* Smart AI using the Minimax algorithm
* Two-player mode
* Score tracking
* Replay option
* Better board design
* Input error handling for non-numeric values
* Player name selection

## 👩‍💻 Author

**Srujana Pujar**

## 📄 License

This project is created for **educational and learning purposes**.

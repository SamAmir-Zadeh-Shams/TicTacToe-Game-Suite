# TicTacToe Game Suite (Python Tkinter)

## Overview

This project is a multi-mode TicTacToe game built using Python and Tkinter. It includes three different gameplay modes ranging from basic two-player gameplay to advanced AI-driven matches.

## Game Modes

### 1. Classic TicTacToe

* Two-player local mode (X vs O)
* Turn-based gameplay
* Win/draw detection system

### 2. Random AI Mode

* Player vs computer
* Computer selects random available moves
* Option to play as X or O

### 3. Advanced AI Mode

* Player vs intelligent computer opponent
* AI prioritizes:

  * Winning moves
  * Blocking opponent wins
  * Center control
  * Corner strategy
  * Random fallback moves
* More challenging gameplay experience

## Features

* Interactive GUI built with Tkinter
* Real-time game state updates
* Win detection using predefined winning combinations
* Multiple difficulty levels
* AI decision-making logic
* Automatic game termination on win/draw

## AI Strategy (Advanced Mode)

The AI follows a priority system:

1. Check for winning move
2. Block opponent’s winning move
3. Take center if available
4. Take a corner if available
5. Otherwise choose a random available move

## Technologies Used

* Python
* Tkinter (GUI)
* Random module (AI move selection)
* Event-driven programming

## How to Run

1. Ensure Python 3.x is installed
2. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/tictactoe-game-suite.git
   ```
3. Navigate to the project folder:

   ```bash
   cd tictactoe-game-suite
   ```
4. Run the program:

   ```bash
   python main.py
   ```

## How to Play

* Launch the program
* Choose a game mode
* Select whether to play as X or O (where applicable)
* Click squares to make moves
* First to align 3 symbols wins

## Future Improvements

* Add minimax AI
* Improve UI design and animations
* Add score tracking system
* Add difficulty selection slider

## Author

Sam Amir-Zadeh-Shams

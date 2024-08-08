# BreakoutGamePY

## Overview

A recreation of breakout game with python, using turtle, tkinter and pillow together. This is done in an OOP approach. It's a game where the player controls the paddle to hit a ball to destroy bricks, without letting the ball fall below the paddle. 

## Features

- Paddle, ball and bricks for a simple Breakout Game
- Level Selection: 3 levels with different appearances and brick generation

## Prerequisites

To run this application, you need to have Python 3.x installed on your computer. You can download Python from [python.org](https://www.python.org/downloads/).

You also need to install the packages pillow and customtkinter. You can do this by installing them separately or by:

```shell
pip install -r requirements.txt
```


## How to Run

1. **Clone the Repository**: 
   - Open your terminal or command prompt.
   - Navigate to the directory where you want to clone the repository.
   - Run the following command:
     ```shell
     git clone https://github.com/nfalck/BreakoutGamePY.git
     ```

2. **Navigate to the Project Folder**:
   - Change the directory to the project folder:
     ```shell
     cd BreakoutGamePY
     ```

3. **Install Dependencies**:
   - The application uses the tkinter library, which is included with Python.
   
4. **Run the Game**:
   - Execute the following command to start the application:
     ```shell
     python main.py
     ```

5. **Gameplay**:
   - Click on 'Start Game' to get to the level selection.
   - Select the level you want to play and click 'Start Game'.
   - When the bricks have finished loading, you are prompted to press space to start playing.
   - Move paddle with left and right key
   - When game ends, you can go to level selection with 'Main Menu' button or quit the application entirely with the 'Quit' button.


6. **Game rules**:
   - Each level begins with 5 lives
   - Prevent the ball from falling below the paddle, otherwise you lose a life
   - When all 5 lives are lost, it's game over.
   - You finish the level when you have hit all the bricks. 

## Future Improvements

- Improve the GUI
- Add sound effects
- Add powerups for harder gameplay
- Fix timing issue: when long pressing right/left keys, the ball moves slower



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments
- Used a post by [Compucademy.net](https://compucademy.net/python-turtle-graphics-and-tkinter-gui-programming/) to learn how to integrate turtle with tkinter.
- Used bricks, balls (recolored) and paddles (recolored) from [Jamie Cross](https://jamiecross.itch.io/breakout-brick-breaker-game-tile-set-free).
- The game backgrounds are from [Free Game Assets](https://free-game-assets.itch.io/free-city-backgrounds-pixel-art).
# Press it!

## Project Description
**Press It** is a fast-paced arcade-style game where players must press keys corresponding to falling balls of specific colors before they hit the paddles. The game tests reflexes and accuracy, challenging players to achieve high scores while avoiding penalties for missed or incorrect inputs. Player can press the exit button when they are satisfied with their score.

### Features:
- **Dynamic Gameplay**: Balls fall faster and spawn more frequently as the score increases.
- **Interactive Controls**: Players press 'a', 's', or 'd' keys to match falling balls with their corresponding paddles.
- **Score Tracking**: Displays real-time score and updates the high score at the end of the game.
- **Visual Feedback**: Bouncing balls turn white to indicate successful hits.
- **Difficulty Adjustment**: Speed and spawn rate dynamically adapt to the player's score.
- **leaderboard system**: Keep tracks of the high score and displays.

### INSTALLATION:
1. **Prerequisites**:
- Install the `turtle` library (pre-installed with Python).
2. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/press-it-game.git
   cd press-it-game
3. **Run the game!**:
    python main.py


# Purpose of the classes
- **ScreenHandler**
    Purpose: To manage game's user interface, welcome screen, game area, end screen.
    Interactions: 
    - Initialize the game by invoking the Game class.
    - Display interactive buttons from Button class.
    - Update the screen based on the events and user inputs.
- **Game**
    Purpose: The game core logic, ball spawning, paddle interactions, score management.
    Interactions: 
    - Spawn the ball object from Ball class.
    - Manage the paddles to the corresponding keys from Paddle class.
    - Check the state of the game with ScreenHandler class.
- **Button**
    Purpose: Represents the buttons within the game, for user navigation.
    Interactions: 
    - Drawn on the screen by ScreenHandler class.
    - Detect user actions: starting exiting, and restarting.
- **Paddle**
    Purpose: Represents the paddle at the bottom of the screen with fixed specific color.
    Interactions: 
    - Positioned by Game class on the x's coordinates.
    - Interact with the Ball class to detect the successful hit, granting a score.
- **Ball**
    Purpose: Represents the falling balls that player must react and interact by pressing the correct keys.
    Interactions: 
    - Spawned by the Game class.
    - Move downward according to the player score by Game class
    - Detects the proximity location to the paddle to determine if the hit was successful.
# Modifications
- **Ball class**:
Modified to represent the falling object for the specific 
('a', 's', 'd').
- **Paddle class**:
Modified to look simpler
- **Button class**:
Created to manage the "START", "EXIT", and "RESTART", to facilitate game navigation.
- **Game class**:
Developed to check the current game state, also balls spawning, score tracking, and input handling, for the smooth interaction of the balls and the paddles.
- **ScreenHandler class**:
Implemented to manges the screens: start, end, and game area. In addition, displaying instructions, scores, and button for interface.

In conclusion, I implemented the keyboard and mouse interactions for detecting keys and buttons, and scoring system. Introduce the mechanic to increase the ball speed and decrease the spawn interval for difficulty purpose.

# Testing
- **Functionality**: each class and method work as intended
- **User Experience**: have buttons to aids the simplicity of the game play, also simple colors and instructions.
- **Bugs**: If you die too fast it could cause the screen to go white, which is not really a problem since it can only happen if the user intended to spam it which would end the game(not associate with the gameplay), also it is needed to be a extremely fast spam.

# Rating
- **90**
It features multiple ball objects that interact with paddles, requiring players to press corresponding keys as balls approach specific paddles. This complexity surpasses a basic pong game but it doesn't reach the 100 level, which includes advanced simulations like inelastic collisions or complex chain reactions.

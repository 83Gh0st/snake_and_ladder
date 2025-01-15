# Snake and Ladder Game

This Snake and Ladder game is a graphical version built using Python's Tkinter library. It supports 2-4 players and offers an interactive and visually appealing gameplay experience. The game includes snakes, ladders, customizable tokens, and an animated dice roll.

## Features
- **Graphical User Interface (GUI):** Built with Tkinter, featuring a visually appealing board.
- **Customizable Players:** Allows between 2 to 4 players with names and token shapes/colors.
- **Interactive Gameplay:** Players roll dice to move, encountering snakes and ladders.
- **Animated Dice Roll:** Simulates a dice roll for a more engaging experience.
- **Restart Option:** Players can reset the game at any time.
- **Quit Option:** Exit the game smoothly.

---

## Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/83Gh0st/snake-and-ladder
    cd snake-and-ladder
    ```

2. **Install Python (if not installed):**
    Ensure you have Python 3.7 or later installed. You can download it from [python.org](https://www.python.org/downloads/).

3. **Run the Game:**
    ```bash
    python a.py
    ```

---

## Game Rules

1. **Snakes:** Landing on a snake’s head slides the player down to its tail.
2. **Ladders:** Landing at the base of a ladder allows the player to climb up to its top.
3. **Win Condition:** The first player to reach exactly position 100 wins.
4. **Rolling Dice:** Players must roll the dice to determine their move.
5. **Exceeding Position 100:** Moves that exceed position 100 are not allowed, and the turn is skipped.

---

## Code Structure

### 1. **`__init__`: Initialization**
- Initializes the main window, board, and GUI components.
- Sets up players, snakes, and ladders.

### 2. **`draw_board`: Draws the game board**
- Creates a 10x10 grid with alternating colors.
- Numbers each cell from 1 to 100.

### 3. **`draw_snake_or_ladder`: Draws snakes and ladders**
- Uses colored lines to represent snakes (red) and ladders (green).
- Adds arrows for better visualization.

### 4. **`add_players`: Sets up players**
- Prompts for the number of players (2-4).
- Assigns names, initial positions, and tokens.

### 5. **`roll_dice`: Handles dice rolls**
- Generates a random number between 1 and 6.
- Updates the player’s position based on dice results.
- Checks for snakes or ladders at the new position.
- Displays messages for special events (snake bite, ladder climb, winning).

### 6. **`animate_dice_roll`: Dice animation**
- Displays an animated rolling effect for the dice.

### 7. **`update_player_position`: Updates player positions**
- Draws player tokens on the board based on their positions.
- Supports multiple shapes: oval, rectangle, triangle, hexagon.

### 8. **`restart_game`: Resets the game**
- Resets player positions to 1.
- Enables the roll button for a new game.

---

## User Guide

### 1. **Starting the Game**
- Run the script using `a.py`.
- Enter the number of players (2-4).
- Input player names. Default names are assigned if left blank.

### 2. **Gameplay**
- Players take turns rolling the dice.
- The game highlights events like climbing ladders or sliding down snakes.
- The first player to reach position 100 wins.

### 3. **Controls**
- **Roll Dice:** Rolls the dice and updates the player’s position.
- **Restart Game:** Resets all player positions to start a new game.
- **Quit:** Exits the game.

---

## Snakes and Ladders Design

### Snakes
- 17 -> 7
- 54 -> 19
- 62 -> 18
- 95 -> 56
- 98 -> 64

### Ladders
- 3 -> 20
- 11 -> 28
- 60 -> 85
- 71 -> 91

---

## Future Improvements

1. **Sound Effects:** Add sounds for dice rolls, snakes, and ladders.
2. **Dynamic Board:** Allow custom board sizes and configurations.
3. **Player Avatars:** Add graphical avatars for players.
4. **Online Multiplayer:** Enable remote play with friends.
5. **Theming Options:** Allow users to customize board and token themes.

---

## Contributions

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a pull request.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contact

For questions or feedback, feel free to contact:
- GitHub: (https://github.com/83Gh0st)


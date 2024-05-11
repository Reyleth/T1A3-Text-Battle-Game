# T1A3-Text-Battle-Game

## Terminal Application for Coder Academy assignment

## Sources

<https://www.messletters.com/en/big-text/>

<https://pypi.org/project/art>

## Repository

The github repository is located at <https://github.com/Reyleth/T1A3-Text-Battle-Game>

## Style guides

This python project follows the standard PEP 8 style guide, more can be read [here](https://peps.python.org/pep-0008/)

## Features List

### User Creation/Log in

Terminal Battle uses `.json` files to save user made character classes to a storable format. A `save_data` and `dict_to_class` function is made to save a class as a dictionary in a `json` file and then revert that back to a class upon logging in.

### Town Square aka Main Manu

The `town()` function in locations.py serves as the main menu for the game. It displays the available options to the player and handles their input. Here's a summary of its functionality:

- The function takes a Hero class in the form of current_user as an argument, which contains the current state of the user's game.

- It first clears the screen and prints a welcome message to the player, along with a list of available actions:
    1. Go to the shop
    2. Scout the next battle
    3. Go to the next battle
    4. View inventory
    5. Log out
- The player is then prompted to enter a number to select an option.

- Depending on the player's choice, the function will:
  - Call the shop function if the player chooses to go to the shop, then return to the main menu.
  - Call the scout function if the player chooses to scout the next battle.
  - Call the battle function if the player chooses to go to the next battle. If the player wins the battle, their progress is incremented and saved. If their progress reaches 6, the ending function is called. Otherwise, the function returns to the main menu.
  - Call the view_inventory function if the player chooses to view their inventory, then return to the main menu.
  - Exit the game if the player chooses to log out.
If the player enters an invalid input, they are prompted to try again and the function returns to the main menu.

### Shop

The `shop()` function in `locations.py` allows the player to interact with the in-game shop. Here's a summary of its functionality:

- The function takes a `current_user` dictionary as an argument, which contains the current state of the user's game.

- It first clears the screen and prints a welcome message to the player, along with a list of available actions:
    1. Buy weapons
    2. Sell items
    3. View Inventory
    4. Exit

- The player is then prompted to enter a number to select an option.

- Depending on the player's choice, the function will:
  - Display available weapons for purchase if the player chooses to buy weapons. The weapons are loaded from a JSON file and filtered based on the player's progress. If the player has enough gold, the selected weapon is added to their inventory and the cost is deducted from their gold.
  - Allow the player to sell items from their inventory if they choose to sell items. The player cannot sell their only weapon. The value of the sold item is added to the player's gold.
  - Call the `view_inventory` function if the player chooses to view their inventory, then return to the shop.
  - Return to the main menu if the player chooses to exit.

- If the player enters an invalid input, they are prompted to try again and the function returns to the shop.

### Battle

The `battle()` function in `battle.py` handles the combat between the player and the enemies. Here's a summary of its functionality:

- The function takes a `current_user` object as an argument, which represents the player's character.

- It first matches the player to an enemy based on the player's progress. The enemy is selected from a predefined list of enemies.

- The health of both the player and the enemy is reset to 100 at the start of the battle.

- The function then enters a loop where the player and the enemy take turns attacking each other until one of them runs out of health. In each turn, the player is presented with the following options:
    1. Attack
    2. Change Weapon
    3. Run

- Depending on the player's choice, the function will:
  - Have the player and the enemy attack each other if the player chooses to attack. The health bars of both characters are updated after each attack.
  - Call the `change_weapon` function of the player's character if the player chooses to change their weapon.
  - End the battle if the player chooses to run.

- If the player enters an invalid input, they are prompted to try again and the function continues to the next turn.

- If the player's health drops to 0 or below, the function prints a death message and returns `False`.

- If the enemy's health drops to 0 or below, the function prints a victory message, calls the `loot` function of the player's character to loot the enemy, and returns `True`.

### Progression

Progression in terminal battle is determined by a `progress` value that is tied to each player's character

## Implementation Plan

Github Projects was used for the planning of development. It can be accessed [here](https://github.com/Reyleth/T1A3-Text-Battle-Game/blob/main/README.md).

[progress image](./docs/progress_image.png)

## FAQ

### Q: How do I start a new game?

A: To start a new game, run the bash script `install_requirements.sh` in your terminal. You may need administrator privileges for this. Then run the file `main.py` with python to begin.

### Q: How do I save my progress?

A: Your progress is automatically saved whenever you win a battle or log out of the game. There is no need to manually save your progress.

### Q: How do I exit the game?

A: To exit the game, simply choose the "Log out" option from the main menu.

### Q: How do I win the game?

A: The game is won by defeating all the enemies that threaten PythonLand. Once you achieve this, the game will display the ending message.

### Q: How do I report a bug or provide feedback?

A: You can report bugs or provide feedback by creating an issue on the GitHub repository. Please include as much detail as possible to help us investigate and address the issue.

### Q: Are there any known issues?

A: Currently, there are no known issues. However, if you encounter any problems while playing the game, please let us know so that we can investigate and address them.

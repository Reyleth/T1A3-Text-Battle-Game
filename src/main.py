"""Main file to run the game"""

from art import tprint
from character import Hero
from locations import town
from log_in import start
from initiate import initiate
from utilities import clear_screen, save_data, dict_to_class


def run():
    """Run the game"""
    clear_screen()
    # Print Title
    tprint("Terminal Battle")
    current_user = start()
    # convert current_user to Hero object
    current_user = Hero(
        current_user["username"],
        current_user["progress"],
        current_user["gold"],
        [dict_to_class(item) for item in current_user["inventory"]],
    )
    save_data(current_user)
    if current_user.progress == 6:
        clear_screen()
        print("This character has already completed the game!")
        print("Select a different character or create a new one.")
        input("Press Enter to continue...")
        return run()
    while current_user.progress <= 5:
        if current_user.progress == 0:
            initiate(current_user)
        # Once progress is == 1, bring player to town square
        elif current_user.progress <= 5:
            town(current_user)
        elif current_user.progress == 6:
            print("You have completed the game!")
            break
        else:
            print("Game Over")
            break
    print("Thank you for playing!")
    return

# Run the game if this file is the main file
if __name__ == "__main__":
    run()

"""This file contains the initiate function which is called when the game starts. It prints a welcome message to the user."""

from locations import clear_screen
from utilities import save_data
from weapons import rusty_sword

# This file contains the initiate function which is called when the game starts. It prints a welcome message to the user.


def initiate(current_user: classmethod):
    """Initiate the game by welcoming the user and providing them with a rusty sword"""
    clear_screen()
    print(
        """
              -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
              Welcome to the world of Terminal Battle!  
              
              You are about to embark on a journey filled with challenges,
              monsters, and treasures. Your goal is to defeat the evil
              wizard and save the town of Pythonland from his tyranny.
              You pick up your rusty sword and head towards the town square.
              
              Good luck, Hero """
        + current_user.name
        + "!"
        + """
              -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
              """
    )
    input("Press Enter to continue...")
    current_user.progress = 1
    current_user.inventory.append(rusty_sword)
    current_user.equip(rusty_sword)
    # Save progress
    save_data(current_user)

    return current_user

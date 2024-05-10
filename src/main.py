from art import tprint
from character import Hero
from locations import town
from log_in import start
from initiate import initiate
from utilities import clear_screen, save_data, dict_to_class

def run():
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
    while current_user.progress <= 6:
        if current_user.progress == 0:
            initiate(current_user)
        # Once progress is == 1, bring player to town square
        elif current_user.progress <= 5:
            town(current_user)
        elif current_user.progress == 6:
            print("You have completed the game!")
            # Add ending code here
            break
        else:
            print("Game Over")
            break
    print("Thank you for playing!")


if __name__ == "__main__":
    run()

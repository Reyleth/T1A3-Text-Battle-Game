import sys
from battle import battle
from save_data import save_data
from utilities import clear_screen

def town(current_user: dict):
    clear_screen()
    print("""
          -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          You are now in the town of Pythonland. 
          
          You can:
          1. Go to the shop
          2. Scout the next battle
          3. Go to the next battle
          4. View inventory
          5. Log out
          -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          """)
    choice = input("Enter a number to select an option: ")
    if choice == "1":
        clear_screen()
        shop(current_user)
    elif choice == "2":
        clear_screen()
        scout(current_user)
    elif choice == "3":
        clear_screen()
        if battle(current_user):
            current_user.progress += 1
            save_data(current_user)
            town(current_user)
    elif choice == "4":
        clear_screen()
        inventory(current_user)
    elif choice == "5":
        sys.exit("Thank you for playing!")
    else:
        print("Invalid input. Please try again.")
        input("Press Enter to return to the town...")
        town(current_user)

def shop(current_user: dict):
    print(f"""
          -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          Welcome to the shop! You currently have {current_user.gold} gold.
          
          You can:
          1. Buy weapons
          2. Sell weapons
          3. View Inventory
          4. Exit
          -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          """)
    choice = input("Enter a number to select an option: ")
    if choice == "1":
        print("Buy weapons")
    elif choice == "2":
        print("Sell weapons")
    elif choice == "3":
        inventory(current_user)
    elif choice == "4":
        return town(current_user)
    else:
        print("Invalid input. Please try again.")
        input("Press Enter to return to the shop...")
        return shop(current_user)

def scout(current_user: dict):
    progress_messages = {
        1: "You see a Goblin in the distance.",
        2: "You see a flying bat in the distance.",
        3: "You see a giant spider in the distance.",
        4: "You see a dragon in the distance.",
        5: "You see the evil wizard in the distance."
    }

    message = progress_messages.get(current_user.progress)
    if message:
        print(message)
    else:
        sys.exit("ERROR: Invalid progress")

    input("Press Enter to return to Pythonland...")
    
def inventory(current_user):
    # iterate over inventory and print each item in an unordered list
    for item in current_user.inventory:
        print(f"- {item['name']}")
        input("Press Enter to return to Pythonland...")


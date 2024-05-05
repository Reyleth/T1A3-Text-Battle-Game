import sys
from battle import battle
from save_data import save_data

def town(current_user: dict):
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
        print("Shop")
        shop(current_user)
    elif choice == "2":
        scout(current_user)
    elif choice == "3":
        if battle(current_user):
            current_user.progress += 1
            save_data(current_user)
            town(current_user)
    elif choice == "4":
        inventory(current_user)
    elif choice == "5":
        print("Log out")
        sys.exit("Thank you for playing!")
    else:
        print("Invalid input. Please try again.")
        town(current_user)

def shop(current_user: dict):
    print("""
          -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          Welcome to the shop! 
          
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
        print(inventory(current_user))
    elif choice == "4":
        print("Exit")
    else:
        print("Invalid input. Please try again.")
        return shop(current_user)

def scout(current_user: dict):
    if current_user.progress == 1:
        print("You see a Goblin in the distance.")
    elif current_user.progress == 2:
        print("You see a flying bat in the distance.")
    elif current_user.progress == 3:
        print("You see a giant spider in the distance.")
    elif current_user.progress == 4:
        print("You see a dragon in the distance.")
    elif current_user.progress == 5:
        print("You see the evil wizard in the distance.")
    else:
        sys.exit("ERROR: Invalid progress")

def inventory(current_user: dict):
    inventory_list = current_user.inventory
    # print the inventory array in a readable format
    for item in inventory_list:
        print("- Name: " + item.name + ", Damage: " + str(item.damage) + ", Value: " + str(item.value))

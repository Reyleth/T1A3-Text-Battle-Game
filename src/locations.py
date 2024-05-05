import sys

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
        print("Scout")
    elif choice == "3":
        print("Battle")
    elif choice == "4":
        print(inventory(current_user))
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

def scout():
    pass

def battle():
    pass

def inventory(current_user: dict):
    return current_user["inventory"]

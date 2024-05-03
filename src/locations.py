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
    elif choice == "2":
        print("Scout")
    elif choice == "3":
        print("Battle")
    elif choice == "4":
        print("Inventory")
    elif choice == "5":
        print("Log out")
        sys.exit("Thank you for playing!")
    else:
        print("Invalid input. Please try again.")
        town(current_user)

def shop():
    pass

def scout():
    pass

def battle():
    pass

def inventory():
    pass
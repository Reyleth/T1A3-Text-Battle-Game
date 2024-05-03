def town(current_user: dict):
    print("""
          -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          You are now in the town square. 
          
          You can:
          1. Go to the shop
          2. Go to the forest
          3. View inventory
          4. Log out
          -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          """)
    choice = input("Enter a number to select an option: ")
    if choice == "1":
        print("Shop")
    elif choice == "2":
        print("Forest")
    elif choice == "3":
        print("Inventory")
    elif choice == "4":
        print("Log out")
    else:
        print("Invalid input. Please try again.")
        town(current_user)
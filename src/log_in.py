import json

#Prompt user to log in or create a new user
def start():
    print("Welcome to the Terminal Battle Game!")
    print("Do you have an account?")
    print("1. Yes")
    print("2. No")
    choice = input("Enter your choice: ")
    if choice == "1":
        log_in()
    elif choice == "2":
        create_user()
    else:
        print("Invalid choice")

#Create a new user and export to a JSON file
def create_user():
    username = input("Enter a username: ")
    with open(f"./user_data/{username}.json", "w", encoding="utf-8") as file:
        json.dump({"username": username}, file)

#Log in to existing user and import user data from JSON file
def log_in():
    username = input("Enter your username: ")
    try:
        with open(f"./user_data/{username}.json", "r", encoding="utf-8") as file:
            user_data = json.load(file)
            print(f"Welcome back Hero {user_data['username']}!")
    except FileNotFoundError:
        print("User not found!")
        log_in()


import json
import os


# Prompt user to log in or create a new user
def start():
    print("Welcome to the Terminal Battle Game!")
    print("Do you have an account?")
    print("1. Yes")
    print("2. No")
    choice = input("Enter your choice: ")
    if (
        choice == "1"
        or choice == "yes"
        or choice == "Yes"
        or choice == "YES"
        or choice == "y"
        or choice == "Y"
    ):
        log_in()
    elif (
        choice == "2"
        or choice == "no"
        or choice == "No"
        or choice == "NO"
        or choice == "n"
        or choice == "N"
    ):
        create_user()
    else:
        print("Invalid choice, please try again.")
        start()


# Create a new user and export to a JSON file
def create_user():
    username = input("Enter a username: ")
    user_data = "./src/user_data/users.json"
    os.makedirs(os.path.dirname(user_data), exist_ok=True)

    # Load existing users
    if os.path.exists(user_data):
        with open(user_data, "r", encoding="utf-8") as file:
            users = json.load(file)
    else:
        users = []

    # Check if username already exists
    if any(user["username"] == username for user in users):
        print("Username already exists. Please choose a different username.")
        create_user()
    else:
        # Append new user and write back to file
        users.append({"username": username, "inventory": []})
        with open(user_data, "w", encoding="utf-8") as file:
            json.dump(users, file, indent=4)


# Log in to existing user and import user data from JSON file
def log_in():
    username = input("Enter your username: ")
    user_data = "./src/user_data/users.json"

    # Load existing users
    if os.path.exists(user_data):
        with open(user_data, "r", encoding="utf-8") as file:
            users = json.load(file)
    else:
        print("Hero not found. Retry or create a new hero.")

    # Check if username exists
    if any(user["username"] == username for user in users):
        print("Welcome, Hero " + username + "!")
    else:
        print("\nUsername not found. Please try again.\n")
        start()

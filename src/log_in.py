'''This module contains functions to log in or create a new user'''
import json
import os
import sys

# Get the directory of the executable or source code
if getattr(sys, "frozen", False):
    exe_dir = os.path.dirname(sys.executable)
else:
    exe_dir = os.path.dirname(os.path.abspath(__file__))

# Get the path to the users.json file
save_data = os.path.join(exe_dir, 'user_data/users.json')

#Check if the directory exists and create it if not
if not os.path.exists(os.path.dirname(save_data)):
    os.makedirs(os.path.dirname(save_data))

# Check if the file exists
if not os.path.exists(save_data):
    # If the file doesn't exist, create it with an empty list
    with open(save_data, 'w', encoding='utf-8') as f:
        json.dump([], f)

# Prompt user to log in or create a new user
def start():
    '''Start the game and prompt user to log in or create a new user'''
    print("Welcome to the Terminal Battle Game!")
    print("Do you have an existing character?")
    print("1. Yes")
    print("2. No")
    while True:
        choice = input("Enter your choice: ")
        if (
            choice == "1"
            or choice == "yes"
            or choice == "Yes"
            or choice == "YES"
            or choice == "y"
            or choice == "Y"
        ):
            return log_in()
        elif (
            choice == "2"
            or choice == "no"
            or choice == "No"
            or choice == "NO"
            or choice == "n"
            or choice == "N"
        ):
            return create_user()
        else:
            print("Invalid input, please try again.")


# Create a new user and export to a JSON file
def create_user() -> dict:
    '''Create a new user and export to a JSON file'''
    username = input("Enter a hero name: ")
    user_data = os.path.join(exe_dir, "user_data/users.json")
    os.makedirs(os.path.dirname(user_data), exist_ok=True)

    # Load existing users
    if os.path.exists(user_data):
        with open(user_data, "r", encoding="utf-8") as file:
            users = json.load(file)
    else:
        users = []

    # Check if username already exists
    if any(
        user.get("username") == username for user in users if isinstance(user, dict)
    ):
        print("Hero name already exists. Please choose a different name.")
        return create_user()
    else:
        # Append new user and write back to file
        users.append({"username": username, "progress": 0, "gold": 0, "inventory": []})
        with open(user_data, "w", encoding="utf-8") as file:
            json.dump(users, file, indent=4)
        current_user = next(
            (
                user
                for user in users
                if isinstance(user, dict)
                and "username" in user
                and user["username"] == username
            ),
            None,
        )
        return current_user


# Log in to existing user and import user data from JSON file
def log_in() -> dict:
    '''Log in to existing user and import user data from JSON file'''
    username = input("Enter your hero name: ")
    user_data = os.path.join(exe_dir, "user_data/users.json")
    print(f"Absolute path to users.json: {os.path.abspath(user_data)}")
    users = []

    # Load existing users
    if os.path.exists(user_data):
        with open(user_data, "r", encoding="utf-8") as file:
            users = json.load(file)
    else:
        print("Hero not found. Retry or create a new hero.")

    # Check if username exists
    if any(user["username"] == username for user in users):
        current_user = next(user for user in users if user["username"] == username)
        print("Welcome back, Hero " + username + "!")
        return current_user
    else:
        print("\nHero not found. Please try again.\n")
        return start()

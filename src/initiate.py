import json
# This file contains the initiate function which is called when the game starts. It prints a welcome message to the user.

def initiate(current_user: dict):
    print("""
          -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          Welcome to the world of Terminal Battle!  
          
          You are about to embark on a journey filled with challenges,
          monsters, and treasures. Your goal is to defeat the evil
          wizard and save the town of Pythonland from his tyranny.
          
          Good luck, Hero """ + current_user["username"] + "!" + """
          -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          """)
    input("Press Enter to continue...")
    current_user["progress"] = 1
    # update progress to users.json
    with open("src/user_data/users.json", "r", encoding="utf-8") as file:
        users = json.load(file)
    with open("src/user_data/users.json", "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)

    return current_user

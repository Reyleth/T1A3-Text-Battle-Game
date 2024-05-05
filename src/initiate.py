import json
from save_data import save_data
from weapons import rusty_sword
# This file contains the initiate function which is called when the game starts. It prints a welcome message to the user.

def initiate(current_user: classmethod):
    print("""
          -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          Welcome to the world of Terminal Battle!  
          
          You are about to embark on a journey filled with challenges,
          monsters, and treasures. Your goal is to defeat the evil
          wizard and save the town of Pythonland from his tyranny.
          You pick up your rusty sword and head towards the town square.
          
          Good luck, Hero """ + current_user.name + "!" + """
          -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          """)
    input("Press Enter to continue...")
    current_user.progress = 1
    current_user.inventory.append(rusty_sword)
    current_user.equip(rusty_sword)
    save_data(current_user)
    
    # # read the users.json file
    # with open("src/user_data/users.json", "r", encoding="utf-8") as file:
    #     users = json.load(file)

    # # update the progress of the current user and add the rusty sword to their inventory
    # for user in users:
    #     if user["username"] == current_user.name:
    #         user["progress"] = 1
    #         user["inventory"].append(rusty_sword.to_dict())
    #         break

    # # write the updated users back to the file
    # with open("src/user_data/users.json", "w", encoding="utf-8") as file:
    #     json.dump(users, file, indent=4)


    return current_user

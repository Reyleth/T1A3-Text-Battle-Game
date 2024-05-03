from locations import town
from log_in import start
from initiate import initiate

END_PROGRAM = False

def run():
    # Start the program and prompt user to log in or create a new user
    with open("src/sys_data/title.txt", "r", encoding="utf-8") as file:
        title = file.read()
        print(title)
    current_user = start()
    print(current_user)
    while current_user["progress"] < 5 and END_PROGRAM is False:
        if current_user["progress"] == 0:
            initiate(current_user)
        print(current_user)
        # Once progress is == 1, bring player to town square
        if current_user["progress"] == 1:
            town(current_user)
            print("Town Square")
        else:
            print("Game Over")
            break








if __name__ == '__main__':
    run()

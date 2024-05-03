from locations import town
from log_in import start
from initiate import initiate

end_program = False

def run():
    # Start the program and prompt user to log in or create a new user
    with open("src/sys_data/title.txt", "r", encoding="utf-8") as file:
        title = file.read()
        print(title)
    current_user = start()
    while current_user["progress"] < 5 and end_program is False:
        if current_user["progress"] == 0:
            initiate(current_user)
        # Once progress is == 1, bring player to town square
        if current_user["progress"] == 1:
            town(current_user)
        else:
            print("Game Over")
            break
    print("Thank you for playing!")








if __name__ == '__main__':
    run()

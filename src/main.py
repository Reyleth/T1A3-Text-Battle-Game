from log_in import start
from initiate import initiate

def run():
    # Start the program and prompt user to log in or create a new user
    title = ""
    with open("src/sys_data/title.txt", "r", encoding="utf-8") as file:
        title = file.read()
        print(title)
    current_user = start()
    print(current_user)
    if current_user["progress"] == 0:
        initiate()








if __name__ == '__main__':
    run()

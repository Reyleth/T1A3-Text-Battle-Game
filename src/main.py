from log_in import start
from initiate import initiate

def run():
    # Start the program and prompt user to log in or create a new user
    current_user = start()
    print(current_user)
    if current_user["progress"] == 0:
        initiate()








if __name__ == '__main__':
    run()

'''Utility functions for the game'''
import json
import os
from character import Item
from weapons import Weapon

def clear_screen():
    '''Clear the terminal screen'''
    os.system('clear' if os.name == 'posix' else 'cls')

# Save current_user class object to a JSON file
def save_data(current_user: classmethod):
    '''Save current_user class object to a JSON file'''
    filename = "src/user_data/users.json"
    data = {}

    # Load existing data
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
    # Check if username currently exists in data
    if any(user.get("username") == current_user.name for user in data if isinstance(user, dict)):
        # Update existing user
        for user in data:
            if user["username"] == current_user.name:
                user["progress"] = current_user.progress
                user["gold"] = current_user.gold
                user["inventory"] = [item.to_dict() if not isinstance(item, dict) else item for item in current_user.inventory]
                break
    else:
        # Add new user
        data.append(current_user.to_dict())
    # Write data back to file
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    return current_user

def dict_to_class(dict_obj):
    '''Convert a dictionary to a class object'''
    if dict_obj['type'] == 'Item':
        return Item(dict_obj['name'], dict_obj['value'])
    elif dict_obj['type'] == 'Weapon':
        return Weapon(dict_obj['name'], dict_obj['weapon_type'], dict_obj['damage'], dict_obj['value'])
    else:
        return None
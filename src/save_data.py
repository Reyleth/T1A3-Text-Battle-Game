import json
import os

# Save current_user class object to a JSON file
def save_data(current_user: classmethod):
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
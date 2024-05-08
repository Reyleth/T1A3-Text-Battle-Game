import json
import sys
from battle import battle

# from character import Item
from utilities import clear_screen, save_data
from weapons import Weapon


def town(current_user: dict):
    clear_screen()
    print(
        """
          -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          You are now in the town of Pythonland. 
          
          You can:
          1. Go to the shop
          2. Scout the next battle
          3. Go to the next battle
          4. View inventory
          5. Log out
          -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          """
    )
    choice = input("Enter a number to select an option: ")
    if choice == "1":
        clear_screen()
        shop(current_user)
        town(current_user)
    elif choice == "2":
        clear_screen()
        scout(current_user)
    elif choice == "3":
        clear_screen()
        if battle(current_user):
            current_user.progress += 1
            save_data(current_user)
            town(current_user)
        else:
            town(current_user)
    elif choice == "4":
        clear_screen()
        view_inventory(current_user)
        input("Press Enter to return to Pythonland...")
    elif choice == "5":
        sys.exit("Thank you for playing!")
    else:
        print("Invalid input. Please try again.")
        input("Press Enter to return to the town...")
        town(current_user)


def shop(current_user: dict):
    print(
        f"""
          -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          Welcome to the shop! You currently have {current_user.gold} gold.
          
          You can:
          1. Buy weapons
          2. Sell items
          3. View Inventory
          4. Exit
          -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          """
    )
    choice = input("Enter a number to select an option: ")
    if choice == "1":
        print("Buy weapons")
        shop_weapons = []
        # read shop weapons from JSON file
        with open("src/sys_data/shop_weapons.json", "r", encoding="utf-8") as file:
            # load all weapons that match current_user progress
            for weapon in json.load(file):
                if weapon["progress"] <= current_user.progress:
                    # Exclude 'type' and 'progress' from the dictionary
                    weapon_args = {
                        k: v for k, v in weapon.items() if k not in ["type", "progress"]
                    }
                    shop_weapons.append(Weapon(**weapon_args))
                    print(
                        f"{weapon['name']} - Damage: {weapon['damage']} - Value: {weapon['value']}"
                    )
        buy_weapon = input("Enter the name of the weapon you would like to buy: ")
        for weapon in shop_weapons:
            if weapon.name == buy_weapon:
                if current_user.gold >= weapon.value:
                    current_user.inventory.append(weapon)
                    current_user.gold -= weapon.value
                    save_data(current_user)
                    print(f"{weapon.name} purchased for {weapon.value} gold.")
                    break
                else:
                    print("You do not have enough gold to purchase this item.")
                    input("Press Enter to return to the shop...")
                    return shop(current_user)
            else:
                print("Item not found. Did you spell it correctly?")
                input("Press Enter to return to the shop...")
                return shop(current_user)
    elif choice == "2":
        print("Sell items")
        view_inventory(current_user)
        sell_item = input("Enter the name of the item you would like to sell: ")
        for item in current_user.inventory:
            if item.name == sell_item:
                current_user.gold += item.value
                current_user.inventory.remove(item)
                save_data(current_user)
                print(f"{item.name} sold for {item.value} gold.")
                break
            else:
                print("Item not found. Did you spell it correctly?")
                input("Press Enter to return to the shop...")
                return shop(current_user)
    elif choice == "3":
        view_inventory(current_user)
        input("Press Enter to return to the shop...")
        return shop(current_user)
    elif choice == "4":
        return town(current_user)
    else:
        print("Invalid input. Please try again.")
        input("Press Enter to return to the shop...")
        return shop(current_user)


def scout(current_user: dict):
    progress_messages = {
        1: "You see a Goblin in the distance.",
        2: "You see a flying bat in the distance.",
        3: "You see a giant spider in the distance.",
        4: "You see a dragon in the distance.",
        5: "You see the evil wizard in the distance.",
    }

    message = progress_messages.get(current_user.progress)
    if message:
        print(message)
    else:
        sys.exit("ERROR: Invalid progress")

    input("Press Enter to return to Pythonland...")


def view_inventory(current_user):
    # iterate over inventory and print each weapon in an unordered list followed by each item
    print(
        """
      -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
      Inventory:
      """
        + "\n".join(
            (
                f"{i.name} - Damage: {i.damage} - Value: {i.value}"
                if isinstance(i, Weapon)
                else f"{i.name} - Value: {i.value}"
            )
            for i in current_user.inventory
        )
        + """
      -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
      """
    )

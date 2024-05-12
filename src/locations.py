'''This module contains the main game locations and menus for navigating the game.'''
from art import tprint
import json
import sys
from battle import battle
from utilities import clear_screen, save_data
from weapons import Weapon


def town(current_user: dict):
    '''Main menu for the game'''
    clear_screen()
    tprint("Town Square")
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
            if current_user.progress == 6:
                ending(current_user)
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
    '''Shop menu for the game where the player can buy and sell weapons and items'''
    tprint("Shop")
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
        # if no weapons are available for purchase, return to the shop
        if not shop_weapons:
            print("There are no weapons available for purchase at this time.")
            input("Press Enter to return to the shop...")
            return shop(current_user)
        buy_weapon = input("Enter the name of the weapon you would like to buy: ")
        for weapon in shop_weapons:
            if weapon.name == buy_weapon:
                if current_user.gold >= weapon.value:
                    current_user.inventory.append(weapon)
                    current_user.gold -= weapon.value
                    save_data(current_user)
                    print(f"{weapon.name} purchased for {weapon.value} gold.")
                    input("Press Enter to return to the shop...")
                    return shop(current_user)
                else:
                    print("You do not have enough gold to purchase this item.")
                    input("Press Enter to return to the shop...")
                    return shop(current_user)
        print("Item not found. Did you spell it correctly?")
        input("Press Enter to return to the shop...")
        return shop(current_user)
    elif choice == "2":
        print("Sell items")
        view_inventory(current_user)
        if len(current_user.inventory) == 1 and isinstance(current_user.inventory[0], Weapon):
            print("You cannot sell your only weapon.")
            input("Press Enter to return to the shop...")
            return shop(current_user)
        sell_item = input("Enter the name of the item you would like to sell: ")
        for item in current_user.inventory:
            if item.name.strip().lower() == sell_item.strip().lower():
                current_user.inventory.remove(item)
                current_user.gold += item.value
                save_data(current_user)
                print(f"{item.name} sold for {item.value} gold.")
                input("Press Enter to return to the shop...")
                return shop(current_user)
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
    '''Scout the next battle'''
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
    '''View the player's inventory'''
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

def ending(current_user) -> None:
    '''Ending of the game'''
    if current_user.progress == 6:
        # Add ending code here TODO
        clear_screen()
        print(
            f"""
          -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          You have defeated the evil wizard and saved Pythonland!

            Thank you for playing Terminal Battle, Hero {current_user.name}!
          -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          """
        
        )
        input("Thank you for playing! Press Enter to continue...")
        sys.exit()
    else:
        sys.exit("ERROR: Invalid progress")

'''This module contains the battle function to create a battle between the hero and an enemy.'''
import character
from utilities import clear_screen

enemy_list = [
    character.goblin,
    character.flying_bat,
    character.giant_spider,
    character.dragon,
    character.evil_wizard
]

def battle(current_user: classmethod):
    '''Battle the enemy'''
    hero = current_user
    # Check if progress - 1 is a valid index for an enemy in the list
    if not 0 <= hero.progress - 1 < len(enemy_list):
        print("Error: Invalid progress level for hero.")
        return
    # Match hero to enemy based on progress
    enemy = enemy_list[hero.progress - 1]
    # Reset health values (update this later!!)
    hero.health = 100
    enemy.health = 100

    print(f"{hero.name} health: {hero.health}")
    print(f"{enemy.name} health: {enemy.health}")
    while hero.health > 0 and enemy.health > 0:
        print("1. Attack")
        print("2. Change Weapon")
        print("3. Run")
        choice = input("Enter a number to select an option: ")
        clear_screen()
        if choice == "1":
            hero.attack(enemy)
            enemy.attack(hero)
            # Show health bar
            hero.health_bar.draw()
            enemy.health_bar.draw()
        elif choice == "2":
            hero.change_weapon()
        elif choice == "3":
            print(f"You run away from the {enemy.name} back to the safety of the town!")
            input("Press Enter to continue...")
            return False
        else:
            print("Invalid input. Please try again.")
            continue
    if hero.health <= 0:
        print("You died! Ressurect in PythonLand and try again!")
        input("Press Enter to continue...")
        return False
    if enemy.health <= 0:
        print(f"You defeated the {enemy.name}!")
        #loot the enemy
        hero.loot(enemy)
        return True
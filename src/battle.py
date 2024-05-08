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
    hero = current_user
    # match hero to enemy based on progress
    enemy = enemy_list[hero.progress - 1]
    # reset health values (update this later!!)
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
            print("You ran away!")
            break
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
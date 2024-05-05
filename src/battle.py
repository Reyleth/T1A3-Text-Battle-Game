from character import Hero, goblin
import weapons

def battle(current_user: dict, current_weapon: str="Rusty Sword"):
    hero = Hero(current_user["username"], 100)
    hero.equip(current_weapon)
    enemy = goblin

    while hero.health > 0 and enemy.health > 0:
        print(f"{hero.name} health: {hero.health}")
        print(f"{enemy.name} health: {enemy.health}")
        print("1. Attack")
        print("2. Run")
        choice = input("Enter a number to select an option: ")
        if choice == "1":
            hero.attack(enemy)
            enemy.attack(hero)
            # Show health bar
            hero.health_bar.draw()
            enemy.health_bar.draw()
        elif choice == "2":
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
        return True
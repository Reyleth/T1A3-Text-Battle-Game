from character import Hero, Enemy

def battle(current_user: dict):
    hero = Hero(current_user["username"], 100)
    hero.equip("current_user['inventory'][0]")
    enemy = Enemy(name="Goblin", health=100, weapon="Sword")

    while hero.health > 0 and enemy.health > 0:
        print(f"{hero.name} health: {hero.health}")
        print(f"{enemy.name} health: {enemy.health}")
        print("1. Attack")
        print("2. Run")
        choice = input("Enter a number to select an option: ")
        if choice == "1":
            hero.attack(enemy)
            enemy.attack(hero)
        elif choice == "2":
            print("You ran away!")
            break
        else:
            print("Invalid input. Please try again.")
            continue
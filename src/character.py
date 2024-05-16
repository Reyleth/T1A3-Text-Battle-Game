"""Module for the Character class and its subclasses"""

import random
import weapons
from health_bar import HealthBar


class Character:
    """Class for all characters in the game"""

    def __init__(self, name: str, health: int, max_health=100):
        self.name = name
        self.health = health
        self.health_max = max_health

        self.weapon = weapons.rusty_sword

    def attack(self, target) -> None:
        """Attack a target character"""
        damage = self.weapon.damage

        # 20% chance for a critical hit
        if random.random() < 0.2:
            damage *= 2  # double the damage
            print("Critical hit!")

        target.health -= damage
        target.health = max(target.health, 0)
        target.health_bar.update()
        print(
            f"{self.name} dealt {damage} damage to {target.name} with {self.weapon.name}"
        )


class Hero(Character):
    """Class for the Hero character"""

    def __init__(
        self,
        name: str,
        progress: int,
        gold: int,
        inventory: list,
        health: int = 100,
        max_health=100,
    ):
        super().__init__(name, health, max_health)
        self.progress = progress
        self.gold = gold
        self.inventory = inventory
        self.default_weapon = self.weapon
        self.health_bar = HealthBar(self, colour="green")

    def equip(self, weapon) -> None:
        """Equip a weapon from the inventory"""
        self.weapon = weapon

    def change_weapon(self) -> None:
        """Change the weapon equipped by the Hero"""
        print("Change Weapon")
        for index, weapon in enumerate(self.inventory):
            print(f"{index + 1}. {weapon.name}")
        print(f"{len(self.inventory) + 1}. Return to main menu")
        choice = input("Enter a number to select an option: ")
        if choice == str(len(self.inventory) + 1):
            return
        try:
            choice = int(choice)
            if 0 < choice <= len(self.inventory):
                self.weapon = self.inventory[choice - 1]
                print(f"{self.name} equipped a(n) {self.weapon.name}!")
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")

    def loot(self, enemy) -> None:
        """Loot gold and items from a defeated enemy"""
        self.gold += enemy.gold
        print(f"{self.name} looted {enemy.gold} gold from the {enemy.name}!")
        for item in enemy.inventory:
            self.inventory.append(item)
            print(f"{self.name} looted {item.name} from the {enemy.name}!")
        input("Press Enter to continue...")

    def to_dict(self):
        """Convert Hero object to dictionary for saving to file"""
        return {
            "name": self.name,
            "progress": self.progress,
            "gold": self.gold,
            "inventory": [
                (
                    item.to_dict()
                    if isinstance(item, weapons.Weapon) or isinstance(item, Item)
                    else item
                )
                for item in self.inventory
            ],
            "health": self.health,
            "max_health": self.health_max,
        }


class Enemy(Character):
    """Class for the Enemy characters"""

    def __init__(
        self, name: str, health: int, weapon: str, gold: int, inventory: list
    ) -> None:
        super().__init__(name, health)

        self.weapon = weapon
        self.gold = gold
        self.inventory = inventory
        self.health_bar = HealthBar(self, colour="red")


class Item:
    """Class for items that can be looted from enemies"""

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def to_dict(self):
        return {"name": self.name, "value": self.value, "type": "Item"}


old_sock = Item("Old Sock", 1)
bat_wing = Item("Bat Wing", 5)
spider_silk = Item("Spider Silk", 10)
dragon_scale = Item("Dragon Scale", 20)
wizard_hat = Item("Wizard Hat", 100)

goblin = Enemy(
    name="Goblin",
    health=50,
    weapon=weapons.old_dagger,
    gold=10,
    inventory=[old_sock],
)

flying_bat = Enemy(
    name="Flying Bat",
    health=80,
    weapon=weapons.sharp_fang,
    gold=20,
    inventory=[bat_wing],
)

giant_spider = Enemy(
    name="Giant Spider",
    health=90,
    weapon=weapons.poisonous_fang,
    gold=30,
    inventory=[spider_silk],
)

dragon = Enemy(
    name="Dragon",
    health=100,
    weapon=weapons.fire_breath,
    gold=40,
    inventory=[dragon_scale],
)

evil_wizard = Enemy(
    name="Evil Wizard",
    health=100,
    weapon=weapons.magic_staff,
    gold=50,
    inventory=[wizard_hat],
)

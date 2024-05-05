import random
import weapons
from health_bar import HealthBar

class Character:
    def __init__(self, name: str, health: int, max_health=100):
        self.name = name
        self.health = health
        self.health_max = max_health

        self.weapon = weapons.rusty_sword

    def attack(self, target) -> None:
        damage = self.weapon.damage

        # 20% chance for a critical hit
        if random.random() < 0.2:
            damage *= 2  # double the damage
            print("Critical hit!")

        target.health -= damage
        target.health = max(target.health, 0)
        target.health_bar.update()
        print(f"{self.name} dealt {damage} damage to {target.name} with {self.weapon.name}")

class Hero(Character):
    def __init__(self, name: str, progress: int, gold: int, inventory: list, health: int=100, max_health=100):
        super().__init__(name, health, max_health)
        self.progress = progress
        self.gold = gold
        self.inventory = inventory
        self.default_weapon = self.weapon
        self.health_bar = HealthBar(self, colour="green")

    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped a(n) {self.weapon.name}!")

    def drop(self) -> None:
        print(f"{self.name} dropped {self.weapon.name}!")
        self.weapon = self.default_weapon

    def swap_weapon(self) -> None:
        print(f"{self.name} swapped the {self.weapon.name}")

class Enemy(Character):
    def __init__(self, name: str, health: int, weapon: str,) -> None:
        super().__init__(name=name, health=health)
    
        self.weapon = weapon
        self.health_bar = HealthBar(self, colour="red")

goblin = Enemy(name="Goblin", 
               health=100, 
               weapon=weapons.rusty_sword)

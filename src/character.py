import weapons
from health_bar import HealthBar

class Character:
    def __init__(self, name: str, health: int, max_health=100):
        self.name = name
        self.health = health
        self.health_max = max_health

        self.weapon = weapons.fists

    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        target.health_bar.update()
        print(f"{self.name} dealt {self.weapon.damage} damage to {target.name} with {self.weapon.name}")

class Hero(Character):
    def __init__(self, name: str, health: int, max_health=100):
        super().__init__(name, health, max_health)
        self.inventory = []
        self.default_weapon = self.weapon

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

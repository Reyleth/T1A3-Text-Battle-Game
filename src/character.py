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

    def loot(self, enemy) -> None:
        self.gold += enemy.gold
        print(f"{self.name} looted {enemy.gold} gold from the {enemy.name}!")
        for item in enemy.inventory:
            self.inventory.append(item)
            print(f"{self.name} looted {item.name} from the {enemy.name}!")

    def to_dict(self):
        return {
            "name": self.name,
            "progress": self.progress,
            "gold": self.gold,
            "inventory": [item.to_dict() if isinstance(item, weapons.Weapon) else item for item in self.inventory],
            "health": self.health,
            "max_health": self.health_max
        }

class Enemy(Character):
    def __init__(self, name: str, health: int, weapon: str, gold: int, inventory: list) -> None:
        super().__init__(name, health)

        self.weapon = weapon
        self.gold = gold
        self.inventory = inventory
        self.health_bar = HealthBar(self, colour="red")

class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

old_sock = Item("old sock", 1)
bat_wing = Item("bat wing", 1)
spider_silk = Item("spider silk", 1)
dragon_scale = Item("dragon scale", 1)
wizard_hat = Item("wizard hat", 1)

goblin = Enemy(name="Goblin", 
                health=100, 
                weapon=weapons.rusty_sword,
                gold=10,
                inventory=[old_sock])

flying_bat = Enemy(name="Flying Bat",
                    health=150,
                    weapon=weapons.sharp_fang,
                    gold=20,
                    inventory=[bat_wing])

giant_spider = Enemy(name="Giant Spider",
                    health=200,
                    weapon=weapons.poisonous_fang,
                    gold=30,
                    inventory=[spider_silk])

dragon = Enemy(name="Dragon",
                health=250,
                weapon=weapons.fire_breath,
                gold=40,
                inventory=[dragon_scale])

evil_wizard = Enemy(name="Evil Wizard",
                    health=300,
                    weapon=weapons.magic_staff,
                    gold=50,
                    inventory=[wizard_hat])

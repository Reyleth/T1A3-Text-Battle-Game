class Weapon:
    def __init__(self, name: str, weapon_type: str, damage: int, value: int) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value
    def to_dict(self):
        return {
            "name": self.name,
            "weapon_type": self.weapon_type,
            "damage": self.damage,
            "value": self.value
        }

rusty_sword = Weapon(name="Rusty Sword",
                        weapon_type="sharp",
                        damage=3,
                        value=5)

iron_sword = Weapon(name="Iron Sword",
                        weapon_type="sharp",
                        damage=5,
                        value=10)

short_bow = Weapon(name="Short Bow",
                        weapon_type="ranged",
                        damage=4,
                        value=8)

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
            "value": self.value,
            "type": "Weapon"
        }
# Hero weapons
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

# Enemy weapons
sharp_fang = Weapon(name="Sharp Fang",
                        weapon_type="sharp",
                        damage=2,
                        value=0)

poisonous_fang = Weapon(name="Poisonous Fang",
                        weapon_type="sharp",
                        damage=3,
                        value=0)

fire_breath = Weapon(name="Fire Breath",
                        weapon_type="fire",
                        damage=5,
                        value=0)

magic_staff = Weapon(name="Magic Staff",
                        weapon_type="magic",
                        damage=7,
                        value=0)


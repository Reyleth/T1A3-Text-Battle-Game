'''Module for weapons that are to be used in battle and the shop'''
class Weapon:
    '''Class for weapons that can be equipped by the Hero and used in battle'''
    def __init__(self, name: str, weapon_type: str, damage: int, value: int) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value
    def to_dict(self):
        '''Convert Weapon object to dictionary for saving to file'''
        return {
            "name": self.name,
            "weapon_type": self.weapon_type,
            "damage": self.damage,
            "value": self.value,
            "type": "Weapon"
        }
# Hero starter weapon
rusty_sword = Weapon(name="Rusty Sword",
                        weapon_type="sharp",
                        damage=3,
                        value=5)

# Enemy weapons
old_dagger = Weapon(name="Old Dagger",
                        weapon_type="sharp",
                        damage=1,
                        value=0)

sharp_fang = Weapon(name="Sharp Fang",
                        weapon_type="sharp",
                        damage=4,
                        value=0)

poisonous_fang = Weapon(name="Poisonous Fang",
                        weapon_type="sharp",
                        damage=7,
                        value=0)

fire_breath = Weapon(name="Fire Breath",
                        weapon_type="fire",
                        damage=10,
                        value=0)

magic_staff = Weapon(name="Magic Staff",
                        weapon_type="magic",
                        damage=13,
                        value=0)

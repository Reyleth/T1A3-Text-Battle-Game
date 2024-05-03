class Character:
    def __init__(self, name: str, health: int, max_health=100):
        self.name = name
        self.health = health
        self.health_max = max_health

class Hero(Character):
    pass

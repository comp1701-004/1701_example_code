class Character:

    def __init__(self, character_name: str, character_hp: int, damage: int) -> None:
        self.name = character_name
        self.hit_points = character_hp
        self.damage = damage
    
    def __str__(self) -> str:
        return f'{self.name} ({self.hit_points} hp)'


def attack(attacker: Character, target: Character) -> None:
    """subtracts the 1st characters damage from
    the 2nd character's hp"""
    target.hit_points -= attacker.damage


character1 = Character("Harry Potter", 2, 1)
character2 = Character("James Bond", 4000, 20_000)

attack(character1, character2)
print(character2)
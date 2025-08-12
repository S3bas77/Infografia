import random

class Character:
    def __init__(self, hp, base_damage, parry_prob, crit_prob):
        self.hp = hp
        self.base_damage = base_damage
        self.parry_prob = parry_prob
        self.crit_prob = crit_prob
        self.name = "default"
        self.abilities = []
        self.active_effects = []

    def attack(self, other):
        bonus_damage = sum(e["value"] for e in self.active_effects if e["type"] == "bonus_damage")
        damage = self.base_damage + bonus_damage

        if random.random() <= self.crit_prob:
            damage *= 2
            print(f"¡CRÍTICO de {self.name}!")

        print(f" {self.name} ataca a {other.name} con {damage} de daño.")
        other.hurt(damage)

    def hurt(self, damage):
        bonus_parry = sum(e["value"] for e in self.active_effects if e["type"] == "bonus_parry")
        parry_total = min(self.parry_prob + bonus_parry, 1.0)

        if random.random() <= parry_total:
            print(f" {self.name} bloquea el ataque!")
            damage_taken = 0
        else:
            damage_taken = damage

        self.hp -= damage_taken
        print(f"{self.name} recibe {damage_taken} de daño. HP restante: {self.hp}")

    def set_name(self, name):
        self.name = name

    def reduce_effects_duration(self):
        self.active_effects = [
            {"type": e["type"], "value": e["value"], "turns": e["turns"] - 1}
            for e in self.active_effects if e["turns"] > 1
        ]


def clone_character(character, new_name):
    nuevo = Character(character.hp, character.base_damage, character.parry_prob, character.crit_prob)
    nuevo.set_name(new_name)
    nuevo.abilities = character.abilities[:]  # copiar habilidades
    return nuevo

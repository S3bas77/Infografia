import random

class Dice:
    def __init__(self, n_sides:int, cheat_side: int):
        self.n_sides = n_sides
        self.cheat_side = cheat_side

    def throw(self):
        if random.random() < 0.8:
            return self.cheat_side
        return random.randint(1, self.n_sides)

dice = Dice(10,5)

print(dice.throw())
print(dice.throw())
print(dice.throw())
print(dice.throw())
print(dice.throw())
#import random

# ======== Clase Habilidad ======== #
class Ability:
    def __init__(self, name, effect_type, effect_value, duration=0, uses=1):
        """
        effect_type: "heal", "bonus_damage", "bonus_parry"
        duration: turnos que dura el efecto (0 si es instantáneo)
        uses: cuántas veces se puede usar
        """
        self.name = name
        self.effect_type = effect_type
        self.effect_value = effect_value
        self.duration = duration
        self.remaining_uses = uses

    def use(self, user, target=None):
        if self.remaining_uses <= 0:
            print(f" {user.name} no puede usar {self.name}, sin usos restantes.")
            return False

        self.remaining_uses -= 1

        # Aplicar efecto instantáneo
        if self.effect_type == "heal":
            user.hp += self.effect_value
            print(f" {user.name} se cura {self.effect_value} HP. (HP actual: {user.hp})")

        elif self.effect_type in ("bonus_damage", "bonus_parry"):
            user.active_effects.append({
                "type": self.effect_type,
                "value": self.effect_value,
                "turns": self.duration
            })
            print(f" {user.name} activa {self.name} por {self.duration} turnos.")

        return True

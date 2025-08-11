import random
from character import Character, clone_character
from habilidad import Ability

rogue = Character(15, 10, 0.2, 0.2)
rogue.set_name("rogue")
rogue.abilities = [
    Ability("Golpe Sorpresa", "bonus_damage", 10, duration=2, uses=1),
    Ability("Esquiva Maestra", "bonus_parry", 0.3, duration=2, uses=2)
]

tank = Character(50, 15, 0.25, 0.35)
tank.set_name("tank")
tank.abilities = [
    Ability("Provocar", "bonus_parry", 0.5, duration=1, uses=1),
    Ability("Golpe Poderoso", "bonus_damage", 15, duration=1, uses=2)
]

wizard = Character(25, 12, 0.1, 0.5)
wizard.set_name("wizard")
wizard.abilities = [
    Ability("Bola de Fuego", "bonus_damage", 20, duration=1, uses=1),
    Ability("Curación Menor", "heal", 10, duration=0, uses=2)
]

paladin = Character(10, 6, 0.6, 0.3)
paladin.set_name("paladin")
paladin.abilities = [
    Ability("Curación Divina", "heal", 15, duration=0, uses=1),
    Ability("Defensa Sagrada", "bonus_parry", 0.4, duration=2, uses=2)
]

personajes = [rogue, tank, wizard, paladin]
jugadores = []

numero_jugadores = int(input("Cantidad de Jugadores (2-4): "))

print("\nElija su personaje:")
for idx, p in enumerate(personajes):
    print(f"{idx + 1}. {p.name}")

for i in range(numero_jugadores):
    eleccion = int(input(f"Jugador {i + 1}, elija el número de su personaje: ")) - 1
    nombre_jugador = input(f"Nombre del jugador {i + 1}: ")
    nuevo_jugador = clone_character(personajes[eleccion], nombre_jugador)
    jugadores.append(nuevo_jugador)

random.shuffle(jugadores)

print("\nOrden de turnos:")
for j in jugadores:
    print(f"- {j.name} ({j.hp} HP)")

while sum(1 for j in jugadores if j.hp > 0) > 1:
    for atacante in jugadores:
        if atacante.hp <= 0:
            continue

        atacante.reduce_effects_duration()

        vivos = [j for j in jugadores if j.hp > 0 and j != atacante]
        if not vivos:
            break

        print(f"\nTurno de {atacante.name} (HP: {atacante.hp})")
        print("1. Atacar")
        print("2. Usar habilidad")
        accion = int(input("Elige acción: "))

        if accion == 1:
            for idx, objetivo in enumerate(vivos):
                print(f"{idx + 1}. {objetivo.name} (HP={objetivo.hp})")
            objetivo_idx = int(input("Elige a quién atacar: ")) - 1
            atacante.attack(vivos[objetivo_idx])

        elif accion == 2:
            for idx, hab in enumerate(atacante.abilities):
                print(f"{idx + 1}. {hab.name} (Usos restantes: {hab.remaining_uses})")
            hab_idx = int(input("Elige habilidad: ")) - 1
            habilidad = atacante.abilities[hab_idx]

            objetivo = None
            if habilidad.effect_type not in ("heal", "bonus_parry"):
                for idx, obj in enumerate(vivos):
                    print(f"{idx + 1}. {obj.name} (HP={obj.hp})")
                objetivo_idx = int(input("Elige objetivo: ")) - 1
                objetivo = vivos[objetivo_idx]

            habilidad.use(atacante, objetivo)

        for objetivo in vivos:
            if objetivo.hp <= 0:
                print(f"💀 {objetivo.name} ha sido derrotado!")

ganador = [j for j in jugadores if j.hp > 0][0]
print(f"\n🏆 El ganador es {ganador.name} con {ganador.hp} HP restantes!")
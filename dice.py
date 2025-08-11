import random
is_playing=True

while is_playing:
    n_sides = int(input("Ingrese el numero de caras: "))
    n_turns = int(input("Ingrese el numero de turnos: "))

    for turn in range(n_turns):
        input("Presiones para lanzar de nuevo")
        dice_value = random.randint(1, n_sides)
        print(f"El dado muestra: {dice_value}")

    answer= input("Quiere volver a jugar? [S/N]: ")
    if answer.lower()== "n":
        break

print("FIN")
edad = 19
estatura = 1.9
nombre = "juan"
print(f"hola a todos, mi nombre es {nombre}, mido {estatura}, y mi edad es {edad}")
try:
    edad2=float(input("ingrese edad:"))
    print(edad2, type(edad2))
except ValueError:
    print('Ingrese un valor valido')
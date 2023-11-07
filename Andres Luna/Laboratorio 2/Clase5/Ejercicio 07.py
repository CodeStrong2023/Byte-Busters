"""Ejercicio 7: Juego adivina el nro
Realizar un juego para adivinar un nro. Para ello se debe generar un nro aleatorio entre 1-100, y luego ir pidiendo
nros indicando "es mayor" o "es menor" según sea mayor o menor respecto a N. El proceso termina cuando el usuario
acierta y allí se debe mostrar el nro de intentos"""
import random   #funcion que genera un nro aleatorio
aleatorio = random.randint(0,100)   #rango de valores
contador = 0
while True:
    numero = int(input("Digite un número: "))
    contador += 1
    if numero > aleatorio:
        print("\nNo es el número, digite un número menor")
    elif numero < aleatorio:
        print("\nNo es el número, digite un número mayor")
    else:
        print(f"¡¡¡ Felicitaciones !!!, acabas de adivinar el número {aleatorio}")
        break   #Rompe el ciclo y el bucle
print(f"\nNúmero de intentos: {contador}")
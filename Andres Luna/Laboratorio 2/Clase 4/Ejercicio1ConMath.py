"""Ejercicio 1 de matemática
Sacar la raiz cuadrada de un número positivo"""
import math #Importamos la clase math para usar la función sqrt(raiz cuadrada)


numero = int(input("Digite un número positivo: "))
while numero < 0:
    print("Error -> Deberia ser un número positivo")
    numero = int(input("Digite un número positivo: "))
print(f"\nSu raíz cuadrada es: {math.sqrt(numero):.2f}")
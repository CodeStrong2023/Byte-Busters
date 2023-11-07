print("Juego adivina el numero")
#Realiza un juego para adivinar un numero. para ello se debe generar un numero aleatorio entre 1-100
#luego ir pidiendo numeros indicando "es mayor" o "es menor" segun sea mayo o menos con respeco a N
#el proceso cierra cuando el usuario acierta y alli se debe mostrar el numero de intentos

import random
print("\t Adivina el NUMERO")
aleatorio = random.randint(0, 100)
contador= 0
while True:
    numero =int(input("digite un numero:"))
    contador += 1
    if numero > aleatorio:
        print("\nNo es el numero, digite un numero menor")
    elif numero < aleatorio:
        print("\nNo es el numero, digite un numero mayor")
    else:
        print(f"felicidades, acabas de adivinar el numero {aleatorio}")
        break #ROMPE EL CICLO DE BUCLE
print(f" \nNumero de intentos: {contador}")


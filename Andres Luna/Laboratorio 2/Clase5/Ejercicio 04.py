"""Ejercicio 04: Sumar números pares dentro de un rango
Hacer un programa para sumar nros pares dentro de un rango, por ejemplo:
_ suma de nros pares del 2 al 30
_ suma=240"""

a = int(input("Digite de donde va a comenzar la suma: "))
b = int(input("Digite hasta donde quiere llegar a sumar: "))
suma = 0
for i in range(a,b+1):#SE COLOCA +1 PARA QUE LLEGUE A 30    
    if i % 2== 0:   #Esto es si el nro es par
        suma += i
print(f"\nLa suma de números pares dentro del rango es: {suma}")
print("*colecciones 1:")
print("Ejercicio1: Eliminar elementos repetidos de una lista")

#crear una lista y elimine los elementos repetidos

lista=["Pedro", "Juan", 5, 7, 10, 8, 7, "Pedro", "Luis"]
print(lista)
elementos=set(lista)
print(elementos)

print()
print("*Colecciones 2")
print("ejercicio2: operaciones de conjuntos con listas")
print()
#escriba un programa que tenga 2 lista y a continuacion creer las sig. listas(no debe haber repeticion)
#1 lista de palabras que aparecen en las listas
#2 lista de palabras que aparecen en la primera lista, pero no en la segunda
#3 lista de palabras que aparecen en la segunda lista, pero no en la primera
#4 lista de palabras que aparecen en ambas listas

lista1= [1, 2, 3, 4, 5, 4, 3, 2, 2, 1, 5]
lista2= [4, 5, 6, 7, 8, 4, 5, 6, 7, 7, 8]
print(lista1)
print(lista2)
print()

print("eliminamos elementos repetidos de ambas listas")
conjunto1= set(lista1)
conjunto2= set(lista2)
print(conjunto1)
print(conjunto2)
print()

union=list(conjunto1 | conjunto2)#unimos ambos conjuntos
solo1= list(conjunto1 - conjunto2)#muestra conjunto 1
solo2 = list(conjunto2- conjunto1)#muestra conjunto2
interseccion = list(conjunto1 & conjunto2) #mostramos ambos listas

print(f"lista de palabras que aparece en las listas : {union} ")
print(f"lista de palabras que aparece en la primera lista, pero no en la segunda:  {solo1} ")
print(f"lista de palabras que aparece en la segunda lista, pero no en la primera {solo2} ")
print(f"lista de palabras que aparece en las listas : {interseccion} ")
print()

print("*Colecciones3")
print("Ejercicio3: Agregar personajes a la lista")

personajes =[]
p = {'Nombre': 'Aragon', 'Clase': 'Guerrero', 'Raza': 'Dunadan del norte'}
personajes.append(p)
p= {'Nombre': 'Gandalf', 'Clase': 'Mago', 'Raza': 'Istar'}
personajes.append(p)
p= {'Nombre': 'Legolas', 'Clase': 'Arquero', 'Raza': 'Elfo'}
personajes.append(p)
print()

#agregar 3 personajes
p= {'Nombre': 'Frodo', 'Clase': '', 'Raza': 'Hobbit'}
personajes.append(p)
p= {'Nombre': 'Saruman', 'Clase': 'Mago', 'Raza': 'Istari'}
personajes.append(p)
p= {'Nombre': 'Galadriel', 'Clase': 'Dama de Lórie', 'Raza': 'Elfa'}
personajes.append(p)

print(personajes)

print()
print("       Matemáticas y la clase math")
print()
print("ejercicio1")

import math
tupla = (13, 1, 8, 3, 2, 5, 8)
lista =[]
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)

numero =int(input("ingrese un numero positivo:"))
while numero<0:
    print("ERROR el numero debe ser positivo")
    numero =int(input("ingrese un numero positivo:"))
print(f'\n Su raiz cuadrada es: {math.sqrt(numero):2f}')
print()



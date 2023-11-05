"""Ejercicio2: Operaciones de conjuntos con listas.
Escribir un programa que tenga 2 listas y que a continuación cree las siguientes listas
(en las que no debe haber repetición)
1- Lista de palabras que aparecen en las listas
2- Lista de palabras que aparecen en la 1ra lista, pero no en la 2da
3- Lista de palabras que aparecen en la 2da lista, pero no en la primera
4- Lista de palabras que aparecen en ambas listas
"""

lista1= [1,2,3,4,5,4,3,2,2,1,5]
lista2= [4,5,6,7,8,4,5,6,7,7,8]

#Eliminar los elementos repetidos de ambas listas con conjuntos. Desaparecen al hacer la transformación
conjunto1 = set(lista1)
conjunto2 = set(lista2)

union = list(conjunto1 | conjunto2)   #Unimos los 2 conjuntos
solo1 = list(conjunto1 - conjunto2)    #Solo muestra en conjunto1
solo2 = list(conjunto2 - conjunto1)    #Solo muestra en conjunto2
interseccion = list(conjunto1 & conjunto2)  #Mostramos ambas listas

print(f"Lista de palabras que aparecen en las listas: {union}")
print(f"Lista de palabras que aparecen en la 1ra lista, pero no en la 2da: {solo1}")
print(f"Lista de palabras que aparecen en la 2ra lista, pero no en la 1da: {solo2}")
print(f"Lista de palabras que aparecen en ambas listas: {interseccion}")
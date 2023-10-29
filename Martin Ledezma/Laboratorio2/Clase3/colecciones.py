# Repaso del tipo set o conjunto
#los conjuntos son grupos de elementos desordenados, su caracteristica es que no pueden haber duplicados
#dentro de un conjunto hay valores unicos, puede tener diferentes tipos de datos

conjunto2 = set()
conjunto1 = {"bye", }
conjunto2.add(7)
conjunto2.add("Hola")
print(conjunto2)
conjunto1.add("Hola")
print(conjunto1)
print(3 not in conjunto1)

#crear igualdad entre dos conjuntos
print(conjunto1 == conjunto2)

#Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2 #la linea une 2 elementos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2
print(conjunto3)

conjunto3= conjunto1 - conjunto2 #asigna el valor que esta en el conjunto1 y no el conjunto2
print(conjunto3)
conjunto3= conjunto2 - conjunto1
print(conjunto3)
conjunto3 = conjunto1 ^ conjunto2
print(conjunto3)

#aca se pregunta si un conjunto es un subconjunto dentro de otro:
conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3))
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))


print(conjunto3.issuperset(conjunto1))
print(conjunto3.issuperset(conjunto2))

##como saber cuando 2 conjuntos no comparte ninun  elemento en comun:
print(conjunto1.isdisjoint(conjunto2))

#convertir un conjunto totalmente inmutable,no se puede eliminar,modificar o agregar
#elementos del conjunto
conjunto1 = frozenset


# Repaso de Diccionarios
diccionarioNuevo = {"azul" : "Blue", "rojo" : "Red", "verde" : "Green", "amarillo" : "Yellow"}
print(diccionarioNuevo)

#como eliminar un elemento
del (diccionarioNuevo["rojo"])
print(diccionarioNuevo)

#los diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {"ariel": {"edad": 40, "altura": 1.83}, "osvaldo": [45, 1.85]}
print(diccionario2)





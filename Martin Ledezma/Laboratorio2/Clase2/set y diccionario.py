
#SET

 # no tiene orden, no almacena elementos,no mantiene indices, de orden aleatorio
 #Un ELEMENTO de tipo SET es una coleccion SIN ORDEN y SIN INDICES

planetas = {"Marte", "Jupiter", "Venus"}
print(planetas)

 #funcion LEN
print(len(planetas))

 #revisar si un elemento esta dentro de set
 #respetar mayusculas,minusculas de lo contrario sera FALSE
print("Marte" in planetas)

 #agregar elemento con funcion ADD
 #no se puede agregar  elementos repetidos en SET
planetas.add("tierra")
print(planetas)

 #eliminar elementos con REMOVE, si el elemento no existe dara error
planetas.remove("Jupiter")
print(planetas)

 #funcion DISCARD no presenta error en caso de mal sintaxis el programa seguira ejecutandose
planetas.discard("tierra")
print(planetas)

 #limpiar SET
planetas.clear()
print(planetas)

 #eliminar SET , al hacerlo nos muestra ERROR
del planetas
print(planetas)


#DICCIONARIO
 #se compone de 2 elementos LLAVE (KEY) Y UN VALOR (VALUE
 #dict(key,value)

diccionario = {
    "IDE": "INTEGRATED DEVELOPMENT ENVIRONMET",
    "POO": " PROGRAMACION ORIENTADA A OBJETOS",
    "SABD": "SISTMA DE ADMINISTRACION DE BASE DE DATOS"

}
print(diccionario)

#ejecutamos funcion LEN
print(len(diccionario))

#acceder a un diccionario con la llave (key)
#respetar sintaxis
print(diccionario["IDE"])

#recuperar elemento con GET
print(diccionario.get("POO"))

#modificamos elementos
diccionario["IDE"] = "entorno de desarrollo integrado"
print(diccionario)

#como recorrer los elementos
for termino in diccionario:
    print(termino)

#otra manera de acceder a un diccionario,funcion KEYS
#muestra solo las llaves
for termino in diccionario.keys():
    print(termino)

#muestra solo valores, funcion VALUE
for valor in diccionario.values():
    print(valor)

#comprobar la existencia de un algun elemento
#devuelve un boleano
print("IDE" in diccionario)

#agregar un elemento
diccionario["PK"] = "Primary Key"
print(diccionario)

#eliminar un elemento, funcion POP
diccionario.pop("SABD")
print(diccionario)

#vaciar diccionario con funcion CLEAR
diccionario.clear()
print(diccionario)

#eliminar diccionario con funcion DEL
del diccionario
print(diccionario)


#REPASO Y MAS CONCEPTOS DE LISTAS
#concatenamos listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1+lista2
print(lista3)

#funcion EXTEND permite agregar varios elementos a una lista
lista3.extend([7, 8, 9, 1, 1])
print(lista3)

#funcion INDEX para saber en que indice esta el elemento
print(lista3.index(5))

#como saber cuantos valores repetidos hay dentro de una lista con funcion COUNT
print(lista3.count(1))

#para poner lista en forma descendente con funcion reverse
lista3.reverse()
print(lista3)

#para que una lista se multiplique repitiendo sus elementos
lista3 = lista3 * 2
print(lista3)

#metodos de ordenamientos, funcion SORT de manera predeterminada de manera ascendente
lista3.sort()
print(lista3)

#para ordenamiento de manera descendente
lista3.sort(reverse=True)
print(lista3)


#REPASO Y CONCEPTOS DE TUPLAS
#podemos usar INDEX, LEN, TRANSFORMAR LISTAS EN TUPLAS Y LISTAS EN TUPLAS
#podemos buscar elementos
tupla = (4, "hola", 6.78, [1, 2, 78], 4, "hola")
print(tupla)
print(4 in tupla)








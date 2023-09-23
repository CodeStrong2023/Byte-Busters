# Laboratorio 2
# clase 1 -> Colecciones

# listas, son un conjunto de datos, cada elemento tiene un indice comenzando desde cero,
# pueden contener diferentes tipos de datos, son mutables o modificables
# se definen -> identificador = []
'''
nombres = ['Maria', 'Sergio', 'Manuel', 90, 88, True]
print(nombres)
print(nombres[0]) # -> imprime por indice
print(nombres[-1]) # -> imprime el ultimo elemento
print(nombres[-2]) # con numeros negativos podemos recorrer la lista a la inversa
print(nombres[0:2]) # muestra los indices colocados [n:n-1]
print(nombres[:3]) # se puede omitir el indice cero
print(nombres[1:]) # tambien se puede omitir el indice limite, mostrando el resto de la lista
nombres[3] = "Homar" # modifica valor del indice indicado
print(nombres)
for nombre in nombres:  #iterar la lista
    print(nombre)
print(len(nombres)) # funcion -len- para conocer la cantidad de elementos de la lista
nombres.append("Josefa") # metodo (funcion) append agrega elementos al final de la lista
print(nombres)
nombres.insert(2, "Fernanda") # metodo -insert- agrega elementos en un indice determinado
print(nombres)
nombres.insert(3, 455)
print(nombres)
nombres.remove("Homar") # metodo -remove- elimina el elemento pasado por parametro
print(nombres)
nombres.pop() # metodo -pop- elimina el ultimo elemento de la lista
print(nombres)
del nombres[1] # funcion -del- elimina el elemento del indice indicado
print(nombres)
nombres.clear() # metodo -clear- elimina todos los elementos de la lista
print(nombres)
del nombres # elimina la lista llamada nombres


## Ejercicios clase1
# Ejercicio 1:
# Iterar un rango de 0 a 10 e imprimir numeros divisibles entre 3
numeros = range(0, 10)
for i in numeros:
    if  i % 3 == 0:
        print(i)


# Ejercicio 2:
# Crear un rango de numeros de 2 a 6 e imprimelos
rangoNum = range(2, 6)
for i in rangoNum:
    print(i)


# Ejercicio 3:
# Crear un rango de 3 a 10 pero con incremento de 2 en 2
rangoNum2 = range(3, 10, 2)
for i in rangoNum2:
    print(i)


# Tuplas son similares a la listas pero, no se pueden eliminar sus elementos son inmutables
# se define -> identificador = ()
cocina = ("cuchara", "cuchillo", "tenedor", 2, True)
print(cocina)
print(len(cocina))
print(cocina[0]) # muestra el valor del indice seleccionado
print(cocina[-4]) # muestra el valor del indice seleccionado desde el final
print(cocina[0:1]) # muestra los valores entre el rango 0 y 1
for cocinar in cocina:
    print(cocinar, end = " ")  # recorre tupla con un bucle
print('\n')
cocinaLista = list(cocina) # asignamos tupla en lista cocinaLista
cocinaLista[0] = "plato" # cambiamos el valor del elemento en el indice 0
cocina = tuple(cocinaLista) # asignamos lista en tupla cocina --NO ES BUENA PRACTICA--
print(cocina)
del cocina # funcion -del- elimina la tupla
'''

## Ejercicios tupla y listas
# Ejercicio 1:
# Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8)
# Crear una lista que solo incluya los numeros menores a 5 e imprimir
lista = []
for i in tupla:
    if i < 5:
        lista.append(i)
print(lista)

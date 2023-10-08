# Leccion 2
# Colecciones parte 2
## set o conjunto no tiene un orden, son desordenados, no permite almacenar elementos duplicados o repetidos

planetas = {"Marte", 'Jupiter', 'Venus'}
print(planetas)
print(len(planetas)) # usamos la funcion len = length significa largo
print('Marte' in planetas) # revisar si un elemento existe dentro de set
planetas.add('Tierra') # -add- agrega un nuevo elemento
print(planetas)
planetas.remove('Jupiter') # -remove- elimina un elemento del set, si el elemento no existe genera error
print(planetas)
planetas.discard('Tierra') # -discard- elimina el elemento pasado por parametro, no genera error
print(planetas)
planetas.clear() # -clar- vacía el set por completo
print(planetas)
del planetas # -del- elimina el set

## Diccionario nos permite almacenar el contenido en forma de llave o valor
# se define identificador = {}
diccionario = {
    'IDE': 'Integrated Development Enviroment',
    'POO': 'Programacion Orientada a Objetos',
    'SABD': 'Sistema de administracion de bases de datos'
}
print(diccionario)
print(len(diccionario)) # musesta la cantidad de elementos
print(diccionario['IDE']) # nos muestra el valor del elemento pasado por parametro
print(diccionario.get('POO')) # -get- obtiene el valor de elemento pasado por parametro
diccionario['IDE'] = 'Entorno de desarrollo Integrado' # modifica el valor del elemento pasado entre []
print(diccionario)
for termino in diccionario:  # recorremos el diccionario, muestra solo llave

    print(termino)

for termino, valor in diccionario.items(): # recorremos el dicionario, -items- muestra llave y valor

    print(termino, valor)

for termino in diccionario.keys(): # recorre el diccionario, -keys- muestra solo llaves

    print(termino)

for valor in diccionario.values(): # recorre el diccionario, -values- muestra solo el valores

    print(valor)

print('IDE' in diccionario) # comprobar si existe el elemento en el diccionario
diccionario['PK'] = 'Primary key' # agrega llave y valor al diccionario
print(diccionario)
diccionario.pop('SABD') # -pop- elimina el elemento pasado por parametro
print(diccionario)
diccionario.clear() # -clear- elimina todos los elementos del diccionario
print(diccionario)
del diccionario # elimina el diccionario

## ---------- REPASO ---------

lista = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista + lista2 # concatenamos listas
print(lista3)
lista3.extend([7, 8, 9])  # -extend- agrega varios elementos a la lista
print(lista3)
print(lista3.index(5)) # -index- muesta el indece del elemento pasado por parametro, da error si el valor no esta
print(lista3.count(1)) # -count- cuenta cuantos valores hay repetidos en una lista
lista3.reverse() # -reverse- reorganiza los elementos de la lista al reves , de fin a inicio
print(lista3)
listar = [1, 2, 3] * 2  # repetimos los elementos de la lista segun el multiplicador
print(listar)
lista3.sort() # -sort- ordena la lista de forma ascendente
print(lista3)
lista3.sort(reverse=True) # -sort(reverse=True)- ordena la lista de forma descendente
print(lista3)

tupla = (4, 'Hola', 4.3, [3, 2, 5], 4,'chau')
print(tupla)
print(4 in tupla) # verificamos si se encuentra el elemento o no

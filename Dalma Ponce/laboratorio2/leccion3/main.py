## --------- REPASO SET O CONJUNTO ----
# para definir un conjunto
conjunto = set()
conjunto2 = {"inicio",} # para iniciar un conjunto mediante llaves debe contener un elemento
conjunto.add(7)
conjunto.add("Hola")
conjunto.add(8.5)
print(conjunto)
conjunto2.add(7)
print(conjunto2)
print(3 not in conjunto2) # verifica si un elemento se encuentra en el conjunto
print(conjunto == conjunto2) # verifica la igualdad de los conjuntos
conjunto3 = conjunto | conjunto2 # la pleca une los conjuntos
print(conjunto3)
conjunto3 = conjunto & conjunto2  # verificamos que elemento tienen en comun
print(conjunto3)
conjunto3 = conjunto - conjunto2 # asigna el valor que se encuentra en conjunto y no en conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto
print(conjunto3)
conjunto3 = conjunto ^ conjunto2 # elemento que no tienen en comun
print(conjunto3)
conjunto3 = conjunto | conjunto2
print(conjunto.issubset(conjunto3)) # -issubjet()- verificamos si es subconjunto del parametro
print(conjunto2.issubset(conjunto3)) # -issubjet()- verificamos si es subconjunto del parametro
print(conjunto3.issubset(conjunto2)) # -issubjet()- verificamos si es subconjunto del parametro
print(conjunto3.issuperset(conjunto)) # verificamos si es un superconjunto de elemento elegido
print(conjunto3.issuperset(conjunto2)) # si los elemento del parametro estan en el conjunto
print(conjunto2.issuperset(conjunto3))
print(conjunto.isdisjoint(conjunto2)) # verificamos si ambos conjuntos son disconexos, si comparten elemntos
conjunto = frozenset # esto produce que el conjunto sea inmutable, no se puede modificar

## --------- REPASO DICCIONARIO ----
diccionario = {'Azul': 'Blue', 'Rojo': 'red', 'Verde': 'Green', 'Amarillo': 'Yellow'}
del ( diccionario['Azul']) #  Eliminar diccionario
print(diccionario)
diccionario2 = {'Dalma': {'edad': 27, 'Altura': 1.52}, "German": [45, 1.70], 'Lorena': [32, 1.65]}
print(diccionario2) # Los diccionarios pueden almacenar diferentes tipos de datos

seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 millones', 'Posicion': 'Extremo Derecho'},
    11: {'Nombre': 'Angel Di Maria', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 millones', 'Posicion': 'Extremo Derecho'},
    24: {'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 millones', 'Posicion': 'Media Punta'},
    19: {'Nombre': 'Nicolas Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 millones', 'Posicion': 'Defensa Central'},
    1: {'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 millones', 'Posicion': 'Portero'},
    5: {'Nombre': 'Leandro Daniel Paredes', 'Edad': 29, 'Altura': 1.82, 'Precio': '5.3 millones', 'Posicion': 'Mediocampista'},
    20: {'Nombre': 'Alexis Mac Allister', 'Edad': 24, 'Altura': 1.74, 'Precio': '35 millones', 'Posicion': 'Mediocampista'},
    3: {'Nombre': 'Nicolás Tagliafico', 'Edad': 31, 'Altura': 1.72, 'Precio': '8.9 millones', 'Posicion': 'Lateral Izquierdo'},
    9: {'Nombre': 'Julián Álvarez', 'Edad': 23, 'Altura': 1.70, 'Precio': '60 millones', 'Posicion': 'Delantero'},

}
print(seleccionArgentina[10])

for llave, valor in seleccionArgentina.items():
    print(llave, valor)
print(len(seleccionArgentina), "Son los elementos en nuestro diccionario")

# PILAS usando listas -> el ultimo elemento ingresado es el ultimo en salir
pila = [1, 2, 3]
pila.append(4)  # agregando elementos a la pila
pila.append(5)
print(pila)
pila.pop() # elimina el ultimo elemento de la lista, para usar metodo pila
print(pila)
elemntoEliminado = pila.pop() # elimina el ultimo elemento y lo guarda en la variable
print(f'Eliminamos el elemento {elemntoEliminado}')
print(f'La pila ahora quedó asi: {pila}')

# COLAS con listas
# Escritura de datos de tipo fifo( first input / first output) -> primero en entrar primero en salir
cola = ['marta', 'jorge', 'esteban', 'hugo']
cola.append('marcela')
cola.append('lucia') #agregamos elementos al final de la lista
print(cola)
seRetira = cola.pop(0)
print(f'Atendió al cliente {seRetira}')
print(cola)
seRetira = cola.pop(0)
print(f'Atendió al cliente {seRetira}')
print(cola)
seRetira = cola.pop(0)
print(f'Atendió al cliente {seRetira}')
print(cola)


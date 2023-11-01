#lista = Ariel, Luna, Natalia
#a cada elemento se le asigna un indice: 0, 1, 2, 3...

nombres = ["Naty", "Osvaldo", "Luna", "Andrés"] #el una lista pueden haber distintos datos, string, int, etc
print(nombres)
"""
print(nombres[0])
print(nombres[1])
print(nombres[2])
print(nombres[3])
print(nombres[-1])
print(nombres[-2])
print(nombres[-3])
"""
print(nombres[0:2])  #Solo muestra el indice 0 y 1, pero no el 2

# ir desde el inicio de la lista al indice deseado (no lo incluye)
print(nombres[ :3])  #muestra 0,1,2

#Desde el inicio hasta el final
print(nombres[0: ])

#Modificamos un valor
nombres[2] = "Mate"
print(nombres)

# Iterar una lista
for nombre in nombres: #Nombre es singular, la lista es plural
    print(nombre)
else:
    print("Se acabaron los elementos de la lista")


# Preguntamos cuantos elementos tiene una lista
print(len(nombres)) #Le pasamos como parametro la lista

# Agregamos un elemento
nombres.append("Roco") # Efecto cola, se ingresa un elemento al final
print(nombres)

# Insertar un elemento en un indice especifico
nombres.insert(1,"Beto") #debe ser un entero para la posicion, y el elemento tipo String
print(nombres)
nombres.insert(3, "Debora")
print(nombres)

# Eliminamos un elemento
nombres.remove("Beto")
print(nombres)

# Eliminamos el ultimo elemento
nombres.pop()
print(nombres)

# Se elimina un indice especifico
del nombres[2]  #del significa Delete=eliminar
print(nombres)

# Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

# Eliminar la lista
del nombres
print(nombres) #elimina la lista, aparece error
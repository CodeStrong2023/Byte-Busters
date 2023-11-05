"""Ejercicio 3: Agregar personajes a una lista
Escriba un programa donde cree una lista con los siguientes personajes del Señor de los Anillos.
nombre: Aragorn
Clase: Guerrero
Raza: Dúnedain del Norte

nombre: Gandalf
Clase: Mago
Raza: Maiar

nombre: Legolas
Clase: Arquero
Raza: Elfo Sindar
"""

personajes = [] #Creamos una lista vacia
#Creamos diccionarios
p = {"Nombre": "Aragorn","Clase":"Guerrero","Raza": "Dúnedain del Norte"}
personajes.append(p)    #Agregmos a la lista un personaje

p = {"Nombre": "Gandalf","Clase":"Mago","Raza": "Maiar"}
personajes.append(p)

p = {"Nombre": "Legolas","Clase":"Arquero","Raza": "Elfo Sindar"}
personajes.append(p)

  #   Agregar al menos otros 3 personajes

p = {"Nombre": "Melkor","Clase":"Semi-dios","Raza": "Valar"}
personajes.append(p)

p = {"Nombre": "Beren","Clase":"Guerrero","Raza": "Hombres"}
personajes.append(p)

p = {"Nombre": "Huan","Clase":"Bestia","Raza": "Perro de Caza"}
personajes.append(p)

p = {"Nombre": "Bilbo","Clase":"Saqueador","Raza": "Hobbit"}
personajes.append(p)

p = {"Nombre": "Luthien","Clase":"Hechicera","Raza": "Elfo-Maiar"}
personajes.append(p)

p = {"Nombre": "Gimli","Clase":"Guerrero","Raza": "Enano"}
personajes.append(p)

p = {"Nombre": "Eomer","Clase":"Caballero","Raza": "Humano"}
personajes.append(p)

print(personajes)
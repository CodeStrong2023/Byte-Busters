#Ejercicio1: Eliminar duplicados de una lista.
#Escribir un programa donde tenga una lista y que a continuacion elimine
#los elementos repetidos, por ultimo mostrar la lista.

#Creamos la lista
lista = [1,2,3,"Andrés",7,7,3,"Luna","Andrés"]

#conjunto = set(lista)   #Convertimos la lista a un conjunto de tipo set
#lista = list(conjunto)  #Convertimos el conunto a una lista

lista = list(set(lista))    #Conversion en 1 sola linea de código(+eficiente)
print(lista)
# DADA LA SIGUIENTE TUPLA
tupla = (13, 1, 8, 3, 2, 5, 8)  #Definimos la tupla
#Crear una lista que solo incluya los números menores a 5
#e imprima por consola [1, 3, 2]

for tup in tupla:
    if tup<5:
        print (f" [ {tup} ]", end="")


# Resolucion en clase
print(" ")
lista = []
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)
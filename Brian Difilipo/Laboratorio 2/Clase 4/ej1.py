print("   LLenar una Lista")
#llenar una lista con los numero del 1 al 50
#luego muestra la lista con bucle for, los elementos
#deben mostrarse de la siguiente forma:
#1-2-3-4...-50

lista = list(range(1, 51))
for i in lista:
    print(i, end = '-')


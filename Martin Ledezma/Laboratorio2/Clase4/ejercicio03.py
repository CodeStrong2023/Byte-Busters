print("Insertar elementos y ordenarlos")
#pedier numeros y meterlos en una lista y cuando el usuario introduzca un numero 0
#nuestro programa dejaria de insertar
# mostrar los numeros ordenados de menor a mayor
lista =[]
salir = False
while not salir:
    numero = int(input("digite un numero:"))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)
lista.sort()#la lista esta ordenada con funcion sort
print(f'\n Lista ordenada: \n {lista}')

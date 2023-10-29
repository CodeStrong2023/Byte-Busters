print("Tabla de multiplicar")
#hacer un programa que pida un numero por teclado y guarde en una lista su tabla
#de multiplicar hasta el 10

numero= int(input("digite un numero:"))
lista =[]
for i in range(1, 11):
    lista.append(i*numero)

print(f"\nTabla de multiplicar del {numero}: \n {lista}")

for indice, i in enumerate(lista):
    print(f"{numero}x {i}={lista[indice]}")

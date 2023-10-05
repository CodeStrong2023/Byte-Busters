
print("Ejercicio 1: Iterar un rango de 0 a 10 e imprimir n° divisibles por 3")

for i in range(11):
    if i % 3 == 0:
        print(i)

# ejercicio 2: crear un rango de  2 a 6 e imprimirlos

print("Ejercicio2: Rango con valores de inicio 2 y fin 6")
rango= range(2, 7)
for i in rango:
    print(i)

# ejercicio 3: crear un rango de 3 a 10 pero con incremento de 2 en 2
print("Ejercicio 3: Rango de 3 a 10 con incremento de 2 en 2")
for i in range(3, 11, 2):
    print(i)


print("Ejercicio tupla y lista")

tupla= (13, 1, 8, 3, 2, 5, 8)
lista= []

for elemento in tupla:
    if elemento <5:
        lista.append(elemento)
print(lista)

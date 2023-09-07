# EJERCICIO 1: Iterar un rango de 0 a 10 e imprimir nùmeros divisibles entre 3

print("---Numeros divisibles por 3: ---")
for i in range(10):
    if i % 3 == 0:
        print(i)


print("")
# EJERCICIO 2: Crear un rango d nros de 2 a 6 e imprimirlos
print("---Imprimir de 2 a 6: ---")
rango= range(2,7)
for i in rango:
    print(i)


print("")
# EJERCICIO 3: crear un rango de 3 a 10, con decremento de 2 en 2
print("---Imprimir de 3 a 10, de 2 en 2: ---")
for i in range(3,11,2):
    print(i)

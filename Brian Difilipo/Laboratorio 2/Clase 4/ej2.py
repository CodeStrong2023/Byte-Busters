print("modificar los elementos de una tabla")
lista =list(range(1, 11))
print("lista original")
print()
for i in lista:
    print(i, end= '-')
valor = int(input('\nDigite un valor a multiplicar:'))

#multiplicamos todos los elementos de la lista
for indice, i in enumerate(lista):
    lista[indice] *= valor
print(f'lista final con los elementos multiplicados por {valor}')
for i in lista:
    print(i, end= '-')

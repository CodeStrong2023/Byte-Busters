print("Factorial de un numero positivo")
print()

numero= int(input("Digite un numero:"))
while numero < 0:
    print("Error -> el numero tiene que ser POSITIVO")
    numero= int(input("digite un numero"))
factorial = 1
for i in range(1, numero+1):
    factorial *= i
print((f"\nEl factorial del  numero {numero} positivo ingresado es: {factorial}"))

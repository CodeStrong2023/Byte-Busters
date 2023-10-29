print("Ejercicio 4 Sumar Números pares dentro de un rango")
print()
#sumar numeros pares dentro de  un rango

a= int(input("Ingrese un numero de donde va a comenzar la suma:"))
b= int(input("Ingrese hasta donde quiere llegar a sumar:"))

suma = 0
for i in range(a,b+1):
    if i % 2== 0:
        suma += i
print(f"\nLa suma de numeros pares dentro del rango es:{suma}")

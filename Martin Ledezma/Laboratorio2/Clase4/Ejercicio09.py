print("Mostrar una frase sin espacios y contar su longitud")
#hacer un programa donde el usuario ingrese una frase, se le devolvera la misma
#frase pero sin espacions en blanco, y ademas un contador de cuantos
#cararacteres tiene la frase(sin contar los espacios en blanco)
frase1 = input("digite una frase:")
frase2 = " "
for i in frase1:
    if i != " ":
        frase2 += i
frase1 = frase2
print(f"\nFrase final: {frase1}")
print(f"N° de caracteres: {len(frase1)}")

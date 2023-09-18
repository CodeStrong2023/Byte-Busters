# Definimos una Tupla, similar a una LISTA, pero es inmutable

cocina = ("cuchara","cuchillo","tenedor")
print (len(cocina)) #Len se usa para numerar las tuplas: 3

print()
# Acceder a un elemento, para esto se usa corchetes, NO parentesis
print(cocina[0])

print()
#mostrar de manera inversa
print(cocina[-1])

print()
# Acceder a un rango
print(cocina[0:1])

print()
#Ejemplo
verduras =("papa",)
print(verduras)
#una tupla necesita aunque sea de un elemento: la coma
#de lo contrario solo seria un tipo Streng, str, cadena


#TUPLAS PARTE 2
#recorremos los elementos de la tupla

for cocinar in cocina:
    print(cocinar, end=" ")  #Print usa \n para saltos de linea, para finalizarlos usar:  end=" "


# Para cambiar la tupla se la debe convertir en Lista, cambiarla y convertirla nuevamente a tupla

cocinaLista = list(cocina)
cocinaLista[0] = "Plato"

cocina = tuple(cocinaLista)
print("\n", cocina)


# eliminar tupla
# del cocina



# Tipo Set: no tiene orden ni se puede modificar, PERO, se puede agregar o eliminar
# es semi-inmutable. El orden es aleatorio

planetas = {"Marte","Jupiter","Venus"}
print(len(planetas))    #Len muestra la cantidad len =length= largo



print (" # Revisar si un elemento existe dentro de set:")
print("Marte" in planetas)  # T o F
print("Venus" not in planetas)



print("# Agregar un elemento: ")
planetas.add("Tierra")
print(planetas)



print("# Eliminar elementos, puede arrojar error si el elemento no exite:")
planetas.remove("Jupiter")
print(planetas)
planetas.discard("Tierra")
print(planetas)



print ("# Limpiar Set:")
planetas.clear()
print(planetas)


"""
print ("# Eliminar Set o conjunto:")
del planetas
print(planetas)
"""


#   DICCIONARIO
print("# DICCIONARIO:")
#"Maradona":10      todo eso seria un diccionario, consta de una llave y un valor. dict(key, value)
diccionario = {
    "IDE":"Integrated Development Enviroment",
    "POO":"Programa Orientada a objetos",
    "SABD":"Sistema de Administración de Base de Datos"
}
print(len(diccionario))     #VERIFICA LA CANTIDAD DE ELEMENTOS
print(diccionario)



print("# Acceder a un diccionario con la llaver=key:")
print(diccionario["IDE"])


#otra manera de recuperar un elemento
print(diccionario.get("POO"))
print(diccionario.get("SABD"))



print("# Modificamos elementos:")
diccionario["IDE"]= "Entorno de Desarrollo Integrado"
print(diccionario)



print(" # Como recorrer los elementos: ")
for termino in diccionario:
    print(termino)

#Necesitamos una funcion para recorrer el diccionario
for termino, valor in diccionario.items():
    print(termino, valor)
    

    
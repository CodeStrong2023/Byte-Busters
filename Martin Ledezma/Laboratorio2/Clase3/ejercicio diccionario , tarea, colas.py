
print(" Ingresar 4 elementos al diccionario llamado seleccionArgentina")
seleccionArgentina ={

    10: {"nombre": "Lio Messi", "edad" : 35, "altura" : 1.70, "precio": "50 millones", "posicion" : "Extremo Derecho " },
    11: {"nombre": "Angel Di Maria", "edad" : 34, "altura" : 1.80, "precio": "12 millones", "posicion" : "Extremo Derecho" },
    24: {"nombre": "Paulo Dybala", "edad" : 28, "altura" : 1.77, "precio": "35 millones", "posicion" : "Media Punta" },
    19: {"nombre": "Nicolas Otamendi", "edad" : 34, "altura" : 1.83, "precio": "3.5 millones", "posicion" : "Defensa Central" },
    1: {"nombre": "Franco Armani", "edad" : 35, "altura" : 1.89, "precio": "3.5 millones", "posicion" : "Portero " },

    23: {"nombre": "Emiliano Martinez", "edad" : 31, "altura" : 1.95, "precio": "28 millones", "posicion" : "Arquero " },
    13: {"nombre": "Cristian Romero", "edad" : 25, "altura" :1.85, "precio": "60 millones", "posicion" : "Defensa Central " },
    8:  {"nombre": "Marcos Acuña ", "edad" :31, "altura" : 1.72, "precio": "8 millones", "posicion" : "Lateral Izquierdo " },
    22:  {"nombre": "Lautaro Martinez", "edad" :26, "altura" :1.74, "precio": "100 millones", "posicion" : "Delantero Centro " },
}
print(seleccionArgentina[10])

for llave, valor in seleccionArgentina.items():
    print(llave, valor)
print(len(seleccionArgentina), "Son los elementos en nuestro diccionario")



#### PILAS ####


print()
print("      Metodo con listas llamado PILAS")
print()

pila = [1, 2, 3]
print(pila)


print()
print("agregar elemento a la pila por el final con funcion Append)")
pila.append(5)
pila.append(6)
print(pila)
print()
print("sacar elemento por el final con funcion Pop (elimina o retorna ultimo elemento)")
pila.pop()
print(pila)
print()

#sacar elemento por el final
elementoborrado = pila.pop() #quita el ultimo elemnto y lo guarda en la variable
print(f"Sacamos el ultimo elemento: {elementoborrado}")
print(f"La pila ahora quedo asi: {pila}")

print()

print("         Metodo con listas llamado COLA")
print()

#colas con lista
#estructura de datos de tipo fifo(first input, firs output)

cola= ["Ariel", "Osvaldo", "Liliana", "Pilar"]
print(cola)
print()
print("Agregamos elementos a la cola")
cola.append("Natalia")
cola.append("Jose")
print(cola)
print()
print("Sacamos elementos de la cola")
seRetira= cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)
print()
seRetira= cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)
print()

seRetira= cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)
print()

seRetira= cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)
print()
seRetira= cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)
print()


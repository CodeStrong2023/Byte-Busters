seleccionArgentina = {
    10: {"Nombre":"Lionel Messi","Edad":35,"Altura":1.70,"Precio":"50 Millones","Posición":"Extremo Derecho"},
    11: {"Nombre":"Ángel Di Maria","Edad":34,"Altura":1.80,"Precio":"12 Millones","Posición":"ExtremoDerecho"},
    24: {"Nombre":"Paulo Dybala","Edad":28,"Altura":1.77,"Precio":"35 Millones","Posición":"Media Punta"},
    19: {"Nombre":"Nicolas Otamendi","Edad":34,"Altura":1.83,"Precio":"3.5 Millones","Posición":"Defensa Central"},
    1: {"Nombre":"Franco Armani","Edad":36,"Altura":1.89,"Precio":"3.5 Millones","Posición":"Portero"}
}
for llave, valor in seleccionArgentina.items():
    print(llave,valor)

print("Tenemos cargados en el diccionario la cantidad de jugadores: ",end=" ")
print(len(seleccionArgentina))

#Agregar al menos 4 jugadores
seleccionArgentina["23"]= {"Nombre": "Emiliano Martinez", "Edad":31, "Altura":1.99, "Precio": "5 Millones", "Posición": "Portero"},
seleccionArgentina["9"]= {"Nombre": "Julian Alvarez", "Edad":23, "Altura":1.70, "Precio": "25 Millones", "Posición": "Delantero"},
seleccionArgentina["20"]= {"Nombre": "Alexis Mac Allister", "Edad":24, "Altura":1.75, "Precio": "15 Millones", "Posición": "Mediocampista"},
seleccionArgentina["19"]= {"Nombre": "Marcos Acuña", "Edad":32, "Altura":1.73, "Precio": "10 Millones", "Posición": "Defensa"}
for llave, valor in seleccionArgentina.items():
    print(llave,valor)

print("Tenemos cargados en el diccionario la cantidad de jugadores: ", end=" ")
print(len(seleccionArgentina))
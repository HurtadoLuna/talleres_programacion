auto = {
    "marca": "Ford",
    "modelo": "Mustang",
    "año": 2022,
    "placa": "dfv234",
    "color":"blanco"
}


#Accede a un valor dentro del diccionario
print(auto["modelo"])

#modificar valores dentro del diccionario

auto["año"]=2023
 
#Añadir nuevos elementos

auto["plazas"] = 4

print(auto)

#Eliminar elementos 

#Usando el "del"

del auto["modelo"]

#Usando el ".pop()"

auto.pop("marca")

print(auto)



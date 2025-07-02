#ejercicio 1 

'''nota1=float(input("por favor ingrese su primera nota: "))
nota2=float(input("por favor ingrese su segunda nota: "))
nota3=float(input("por favor ingrese su tercera nota: "))

calificaciones=[nota1, nota2 , nota3]

suma= nota1 + nota2 + nota3 / 3

calificaciones.append(suma)

print(f"sus notas y el promedio de estas son: {calificaciones}")

#ejercicio 2

productos = {
    "pan": 2000,
    "leche" : 3000,
    "harina" : 1500
}

print(productos)

porcentaje= float(input("Porcentaje de aunmento (%):"))
productos["pan"] += productos["pan"] * (porcentaje/100)
productos["leche"] += productos["leche"] * (porcentaje/100)
productos["harina"] += productos["harina"] * (porcentaje/100)
print(productos)

#ejercicio 3

c1=float(input("ingrese la primera temperatura: "))
c2=float(input("ingrese la segunda temperatura: "))
c3=float(input("ingrese la tercera temperatura: "))
c4=float(input("ingrese la cuarta temperatura: "))
c5=float(input("ingrese la quinta temperatura: "))

celsius=( c1,c2,c3,c4,c5)


f1= c1 * 9/5 + 35
f2= c2 * 9/5 + 35
f3= c3 * 9/5 + 35
f4= c4 * 9/5 + 35
f5= c5 * 9/5 + 35

farenheit = (f1 , f2 , f3 , f4 , f5 )

print(f"aqui estan los temperatura en celsius: {celsius}")
print(f"aqui estan los temperatura en farenheit: {farenheit}")


#ejeercicio 4 

edades=[ int(input("Edad 1: ")), int(input("edad 2: ")), int(input("edad 3: ")), int(input("edad 4: ")), int(input("edad 5: "))]
operacion= sum(edades) / 5
print(f"Mayor: {max(edades)}, Menor: {min(edades)}, Promedio: {operacion}")

# ejercicio 5 

frutas = {
    "fresa" : 2000,
    "pera" : 3000, 
    "uva" : 2500
}

print (f" Precios: {frutas}")
kilos_f= float(input("Cuantos kilos de fresa necesita:")) 
kilos_p= float(input("Cuantos kilos de pera necesita:")) 
kilos_u=float(input("Cuantos kilos de uva necesita:"))
operacion_1= kilos_f * frutas["fresa"]
operacion_2= kilos_p * frutas["pera"]
operacion_3= kilos_u * frutas["uva"]
total= operacion_1 + operacion_2 + operacion_3
print(f"total a pagar: {total}") 

#Ejercicio 6

numeros=(23,45,6,32,12)
suma = sum(numeros)
print(f"la suma de los elementos que se encuentran en la tupla es: {suma}")

#ejercicio 7 

inventario=[]



#ejercicio 8
precios=[2000,5000,7300,3000,2500]
print(f"los precios actuales son:{precios}")
descuento= int(input("Ingrese el porcentaje de descuento: "))

precios_descuento=[]
nuevos_precios1= 2000 - (2000*descuento/100)
nuevos_precios2= 5000 - (5000*descuento/100)
nuevos_precios3= 7300 - (7300*descuento/100)
nuevos_precios4= 3000 - (3000*descuento/100)
nuevos_precios5= 2500 - (2500*descuento/100)
precios_descuento.append(nuevos_precios1)
precios_descuento.append(nuevos_precios2)
precios_descuento.append(nuevos_precios3)
precios_descuento.append(nuevos_precios4)
precios_descuento.append(nuevos_precios5)
print(f"estos son los nuevos precios con el descuento: {precios_descuento}")

#Ejercicio 9

notas=()
lista_notas= list(notas)
nota1=float(input("Ingrese su nota de español:"))
nota2=float(input("Ingrese su nota de ingles:"))
nota3=float(input("Ingrese su nota de matematicas:"))
nota4=float(input("Ingrese su nota de geometria:"))

lista_notas.append(nota1)
lista_notas.append(nota2)
lista_notas.append(nota3)
lista_notas.append(nota4)

lista_notas.sort()
lista_notas.reverse()
notas= tuple(lista_notas)

print(f"estas son sus notas: {notas}")

#EJERCICIO 10
unidad_conversion={
    "Km":1000,
    "m":1,
    "Cm":100
}
cantidad=float(input("Ingrese que cantidad desea pasar a metros: "))
unidad=input("ingrese la unidad a la que la desea pasar: ")

resultado= cantidad * unidad_conversion[unidad]

print(f"su cantidad pasada a metros es: {resultado}")'''

#EJERCICIO 11

lista_precios=[]
precios=float(input("Ingrese los precios (usando comas):"))
lista_precios.append(precios)

print(lista_precios)

lista_IVA= []



print(f"estos son los nuevos precios con el 19% de IVA: {lista_IVA}")




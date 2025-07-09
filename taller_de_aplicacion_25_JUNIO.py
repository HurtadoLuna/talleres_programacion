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



'''#-------------------------------------EJERCICIO 11-----------------------------------
precio1= int(input("Ingrese el primer precio:"))
precio2= int(input("Ingrese el segundo precio:"))
precio3= int(input("Ingrese el tercer precio:"))


precios_originales= [precio1, precio2, precio3]
print(f"Estos son los precios originales: {precios_originales}")

operacion1 = (precio1 * 0.19) + precio1
operacion2 = (precio2 * 0.19) + precio2
operacion3 = (precio3 * 0.19) + precio3

precios_con_IVA= [operacion1, operacion2, operacion3]

print(f"Estos son los precios con el IVA: {precios_con_IVA}")

#-------------------------------------EJERCICIO 12-----------------------------------
num1= int(input("Ingrese el primer numero: "))
num2= int(input("Ingrese el segundo numero: "))

suma= num1 + num2
resta = num1 - num2
multi= num1 * num2
division= num1 / num2

operaciones= ( suma , resta , multi , division )

print (f"Asi queda la tupla con todas las operaciones dentro: {operaciones}")

#-------------------------------------EJERCICIO 13-----------------------------------
nombre1= input("Por favor ingrese su nombre: ")
nota1 = float(input("Ingrese su nota: "))

nombre2= input("Por favor ingrese su nombre: ")
nota2 = float(input("Ingrese su nota: "))

nombre3= input("Por favor ingrese su nombre: ")
nota3 = float(input("Ingrese su nota: "))

nombres_y_notas = {
    nombre1:nota1,
    nombre2: nota2,
    nombre3: nota3
 }

promedio = nota1 + nota2 + nota3 / 3
print (f"asi queda el diccionario: {nombres_y_notas}, este es el promedio general: {promedio}")

#-------------------------------------EJERCICIO 14-----------------------------------
salario1=int(input("Ingrese el salario del primer empleado: "))
salario2=int(input("Ingrese el salario del segudo empleado: "))
salario3=int(input("Ingrese el salario del tercer empleado: "))
salario4=int(input("Ingrese el salario del cuarto empleado: "))
salario5=int(input("Ingrese el salario del quinto empleado: "))

operacion1 = salario1 + (salario1 * 0.10)
operacion2 = salario2 + (salario2 * 0.10)
operacion3 = salario3 + (salario3 * 0.10)
operacion4 = salario4 + (salario4 * 0.10)
operacion5 = salario5 + (salario5 * 0.10)

Lista_de_salario= [operacion1, operacion2, operacion3, operacion4, operacion5]

print(f"Asi se ve la lista de los salarios {Lista_de_salario}")

#-------------------------------------EJERCICIO 15-----------------------------------
productos_sin_impuestos = {
    "huevos": 3000,
    "leche": 4000,
    "harina": 2500
}

impuestos_solicitados = float(input("Ingrese el porcentaje: "))

producto_1= productos_sin_impuestos["huevos"] + (productos_sin_impuestos["huevos"] * impuestos_solicitados /100)
producto_2= productos_sin_impuestos["leche"] + (productos_sin_impuestos["leche"] * impuestos_solicitados /100)
producto_3= productos_sin_impuestos["harina"] + (productos_sin_impuestos["harina"] * impuestos_solicitados /100)

print (f"estos son los productos con el impuesto incluido: {producto_1}, {producto_2}, {producto_3}")'''

'''#-------------------------------------EJERCICIO 16-----------------------------------
edad1 = int(input("Ingrese la primera edad: "))
edad2 = int(input("Ingrese la segunda edad: "))
edad3 = int(input("Ingrese la tercera edad: "))

edades=[ edad1, edad2, edad3 ]

menores=0
mayores=0
if edades[0] >= 18:
    menores = mayores +1
else: mayores = menores +1
if edades[1] >= 18:
    menores = mayores +1
else: mayores = menores +1
if edades[2] >= 18:
    menores = mayores +1
else: mayores = menores +1

print(f"Esta es la cantidad de menores: {menores}, Estas es la cantidad de mayores: {mayores}")'''
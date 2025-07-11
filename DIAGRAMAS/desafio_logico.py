#ejercicio 1
'''edad= int(input("Por favor ingrese su edad: "))
if edad >= 65:
    print(f" usted tiene {edad} años de edad por lo tanto usted es un adulto mayor")
elif edad < 18: 
    print(f" usted tiene {edad} por lo tanto usted es menor de edad")
else:
    print(f"usted tiene {edad} por lo tanto usted es mayor de adad")

#ejercicio 2
estatura= float(input("Por favor ingrese su estatura en metros: "))
if estatura > 1.8: 
    print(f"usted mide {estatura}m, por lo tanto usted cosiderado 'alto' ")
elif estatura < 1.5:
    print(f"usted mide {estatura}m, por lo tanto usted es considerado 'bajo' ")
else:
    print(f"usted mide {estatura}m, por lo tanto usted es cosiderado estatura 'media' ")

#ejercicio 3
numero= int(input("Ingrese un numero por favor:"))
if numero % 2 == 0:
    print(f"el numero {numero}, es multiplo del 2")
elif numero % 3 == 0:
    print(f"el numero {numero}, es multiplo del 3")
else:
    print(F"el numero {numero}, no es multiplo de ninguno de los dos")

#ejercicio 4
num= float(input("Ingrese un numero decimal: "))
cantidad= str(num).split(".")

if cantidad == 1:
    print(f"el numero {num}, tiene 1 decimal")
elif cantidad == 2:
    print(f"el numero {num}, tiene 2 decimales") #falta
else:
    print(f"el numero {num}, tiene mas de 2 decimales")

#ejercicio 5
pais= input("Por favor ingrese el nombre de un pais: ")

paises=("colombia", "Perú", "Argentina", "México")
print(paises)

if pais in paises:
    print(f" {pais}, si esta en la tupla")
else:
    print(f"{pais}, no esta en la tupla")

#ejercicio 6
compatibilidad={
    "A": ["A","O"],
    "B": ["B", "O"],
    "AB": ["A", "B", "AB","O"],
    "O": ["O"]
}

tipo=input("Por favor ingrese su tipo de sangre: ")
compatible= ",". join(compatibilidad[tipo])
if tipo in compatibilidad:
    print(f"su sangre es compatible con: {compatible}")
else:
    print("No valido")

#ejercicio 7
temperatura= float(input("Por favor ingrese la temperatura en °C:"))
if temperatura > 25:
    print(f"la temperatura es de {temperatura}° por lo tanto esta haciendo calor ")
elif temperatura < 10:
    print(f"la temperatura es de {temperatura}° por lo tanto esta haciendo frio ")
else:
    print(f"la temperatura es de {temperatura}° por lo tanto esta templado ")

#ejericicio 8
menu= [ "1. suma",
       "2. resta",
       "3. multipliacion"
]
print(menu)

opciones=input("Ingrese la operacion que desea: ")

num1= int(input("Ingrese el primer numero:"))
num2= int(input("Ingrese el segundo numero:"))


if opciones == "1. suma":
    resultado=(num1+ num2)
    print(f"{num1} + {num2} = {resultado} ")
elif opciones== "2. resta":
    resultado1=(num1-num2)
    print(f"{num1} - {num2} = {resultado1} ")
elif opciones== "3. multipliacion":
    resultado2=(num1*num2)
    print(f"{num1} * {num2} = {resultado2} ")
else: 
    print("Instruccion no valida ")


#ejercicio 9 
meses={
    1:"Enero",
    2:"Febrero",
    3:"marzo",
    4:"abril",
    5:"mayo",
    6:"junio",
    7:"julio",
    8:"agosto",
    9:"septiembre",
    10:"octubre",
    11:"noviembre",
    12:"diciembre"

}

mes=int(input("ingrese un numero del 1 al 12 por favor: "))
if 1 <= mes <= 12:
    print(f"el numero {mes} es el mes de :{meses[mes]}")
else:
    print("hubo un error")

#ejercicio 10
num=int(input("Por avor ingrese un numero de 4 digitos"))

if len(num)==4 and num.isdigit():
    if num.
    print("el primer digito es el numero 1")

#ejercicio11
#ejercicio12'''

frutas=["manzana":,"pera", "piña"]
precios={
    
}
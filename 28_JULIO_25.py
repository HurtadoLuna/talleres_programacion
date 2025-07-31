'''
#------------------------------------------------ EJEMPLO 1 --------------------------------------------
vocal= input("Ingrese una vocal:")

if vocal == "a" :
    print(f"su vocal '{vocal}' convertida a mayuscula queda A ")
elif vocal == "e" :
    print(f"su vocal '{vocal}' convertida a mayuscula queda E ")
elif vocal == "i" :
    print(f"su vocal '{vocal}' convertida a mayuscula queda I ")
elif vocal == "o" :
    print(f"su vocal '{vocal}' convertida a mayuscula queda O ")
elif vocal == "u": 
    print(f"su vocal '{vocal}' convertida a mayuscula queda U ")
else:
    print(f"'{vocal}' no es una vocal")

#---------------------------------------------------ejemplo 2 ---------------------------------------------
comando= input("Ingrese el comando:")
if comando == "ENTRAR": 
    print("Bienvenido al sistema")
elif comando == "SALUDO":
    print("Hola, como estas?")
elif comando == "SALIR": 
    print("Saliendo del sistema")
else:
    print("el comando ingresado no existe")

#-------------------------------------------------TALLER-------------------------------------------------


#1. -------------------------Verifica si un numero es positivo o negativo ------------------------

num= int(input("Ingrese un numero por favor: "))
if num == 0:
    print("el numero ingresado es igual a 0")
elif num > 0:
    print(f"el numero '{num}' es positivo")
else:
    print(f"el numero '{num}' es negativo")

#2. ---------------------- Calcula el mayor de dos numeros ingresados ------------------
num1= float(input("Ingrese el primer numero por favor: "))
num2= float(input("Ingrese el segundo numero por favor: "))

if num1 > num2:
    print(f"el numero {num1}, es mayor que el numero {num2}")
elif num1 < num2:
    print(f"el numero {num1}, es menor que el numero {num2}")
else:
    print(f"los numeros {num1} y {num2} son iguales")

#3. -------------------- Determina si un numero es par o impar ---------------------------------
num=int(input("por favor ingrese un numero: "))

if num % 2 == 0: 
    print(f"el numero {num}, es par")
else:
    print(f"el numero {num}, es impar")

#4. ---------------Dado un numero, verifica si esta entre 10 y 20-------------------------------

num1= int(input("Ingrese el numero por favor: "))

if num1 >= 10 and num1 <= 20:
    print(f"el numero {num1} si esta entre 10 y 20")

else:
    print(f" el numero {num1} no esta dentro del rango")

#5. --------------------Dado tres numeros, encuentra ela mayor usando condicionales------------------------

num1= int(input("Ingrese el primer numero por favor: "))
num2= int(input("Ingrese el segundo numero por favor: "))
num3= int(input("Ingrese el tercer numero por favor: "))

if num1 > num2 and num1 > num3:
    print(f"el numero {num1} es mayor que los numeros {num2} y {num3}")
elif num2 > num1 and num2 > num3:
    print(f"el numero {num2} es mayor que los numeros {num1} y {num3}")
else:
    print(f"el numero {num3} es mayor que los numeros {num1} y {num2} ")

#6. -----------------Calcula el precio final con un 10% de descuento si el total es mayor a 100--------------------

num1= float(input("Ingrese el precio del primer producto por favor: "))
num2= float(input("Ingrese el precio del segundo producto por favor: "))
suma= num1 + num2 
descuento= suma - (suma * 0.10)

if suma >= 100:
    print(f"Este es su precio {suma} y este es con el precio con descuento {descuento}")
else:
    print(f"este es su precio total {suma}, su total es menor a 100 por lo tanto no se le puede realizar el descuento")

#7. ------------------------ Verifica si una persona puede votar -----------------

edad= int(input("Por favor ingrese su edad:"))

if edad >= 18:
    print(f"usted tiene {edad} años de edad, por lo tanto usted puede votar")
else:
    print(f"usted tiene {edad} años de edad, por lo tanto no puede votar por ser menor de edad")

#8.---------------- Dado el precio y tipo de cliente (VIP o normal), aplica un descuento del 20% solo al VIP-------------

precio= float(input("Ingrese el precio del producto por favor: "))
usuario= input("Ingrese el tipo de usuario que es usted: ")
descuento= precio - ( precio * 0.20)

if usuario == "VIP": 
    print(f"Usted porque es cliente VIP su precio final sera de {descuento}")
else:
    print(f"Usted por ser un cliente normal no tendria descuento alguno por lo tanto su precio final es {precio}")

#9 ----------------- Determina si un numero es multiplo del 5 y de 3 al mismo tiempo-----------------------

num= float(input("Ingrese un numero: "))

if num % 5 == 0 and num % 3 == 0: 
    print(f" el numero {num} si es multiplo de ambos numeros")
else:
    print(f"el numero {num} no es multiplo de los dos numeros")

#10. Dado un numero mire si es divisible entre dos numeros dados 
num= int(input("ingrese un numero: "))
divisor1= int(input("Ingrese el numero divisor:"))
divisor2= int(input("Ingrese el segundo numero divisor:"))

if num % divisor1 == 0 and num%divisor2 == 0:
    print(f"el numero  {num} es divisible por ambos numeros")
else:
    print(f"el numero {num} no es divisible por ambos numeros")

#----------------------------------EJERCICIO CON LISTAS---------------------------
# 11. CREA UNA LISTA CON 5 NUMEROS. SI EL TERCER NUMERO ES MAYOR QUE 10, MUESTRA "MAYOR A 10", SI NO, MUESTRA "MENOR O IGUAL A 10"  

numeros=[int(input("Ingrese el primer numero:")), int(input("Ingrese el segundo numero:")), int(input("Ingrese el tercer numero:")), int(input("Ingrese el cuarto numero:")), int(input("Ingrese el quinto numero:"))]
print(f"asi quedaria la lista {numeros}")

if numeros[2] > 10:
    print(f"el numero {numeros[2]} es mayor a 10")
elif numeros[2] == 0:
    print(f"el numero {numeros[2]} es igual a cero")
else:
    print(f"el numero {numeros[2]} es menor a 10")

#12. VERIFICA SI EL NUMERO 7 ESTA EN LA LISTA. SI ESTA, MUESTRA "ESTA EN LA LISTA", SI NO, MUESTRA "NO ESTA EN LA LISTA"

numeros=[int(input("Ingrese el primer numero:")), int(input("Ingrese el segundo numero:")), int(input("Ingrese el tercer numero:")), int(input("Ingrese el cuarto numero:"))]
print(f"asi quedaria la lista {numeros}")

if numeros[0] == 7:
    print("el numero 7 si esta en la lista")
elif numeros[1] == 7:
    print("el numero 7 si esta en la lista")
elif numeros[2] == 7:
    print("el numero 7 si esta en la lista")
elif numeros[3] == 7:
    print("el numero 7 si esta en la lista")
else:
    print("el numero 7 no esta en la lista")

#13. SUMA LOS DOS PRIMEROS ELEMENTOS DE UNA LISTA, SI LA SUMA ES MAYOR A 10, MUESTRA "SUMA ALTA", DE LO CONTRARIO MUESTRA "SUMA BAJA"

numeros=[int(input("Ingrese el primer numero:")), int(input("Ingrese el segundo numero:")), int(input("Ingrese el tercer numero:")), int(input("Ingrese el cuarto numero:"))]
print(f"asi quedaria la lista {numeros}")

operacion= numeros[0] + numeros[1]

if operacion > 10:
    print(f"la suma de los numeros {numeros[0]} y {numeros[1]} es una suma alta pues su resultado es: {operacion}")
else:
    print(f"la suma de los numeros {numeros[0]} y {numeros[1]} es una suma baja pues su resultado es: {operacion}")

#14. DADA LA LISTA, MUESTRA EL ULTIMO NOMBRE, SI ESE NOMBRE ES MARTA, MUESTRA NOMBRES "CORRECTO", SI NO , "NOMBRE DIFERENTE"

nombres= [input("ingrese el primer nombre: "), input("ingrese el segundo nombre: "), input("ingrese el tercer nombre: "), input("ingrese el ultimo nombre: ")]
print(nombres)

if nombres[3] == "Marta": 
    print(f"El ultimo nombres es Marta por lo tanto es CORRECTO")
else:
    print("usted ha ingresado un nombre diferente")

#15. CREA UNA LISTA CON TRES COLORES. CAMBIA EL SEGUNDO COLOR SOLO SI ES IGUAL A "AZUL" Y MUESTRA LA LISTA ACTUALIZADA

colores= [input("ingrese un color :"), input("ingrese un color: "), input("ingrese un color: ") ]
print(f"asi esta la lista original {colores}")

if colores[2] == "azul" 



#----------------------------------------EJERCICIOS CON TUPLA-----------------------------------

#16. CREA UNA TUPLA. SI EL PRIMER VALOR ES MENOR QUE EL ULTIMO, MUESTRA "ORDEN ASCENDENTE", SI NO, "ORDEN DESCENDENTE"

 int(input("Ingr ese el segundo numero:"))numeros=(int(input("Ingrese el primer numero:")),, int(input("Ingrese el tercer numero:")), int(input("Ingrese el cuarto numero:")))
print(f"asi esta la Tupla: {numeros}")

if numeros[0] < numeros[3]:
    print(f"la tupla {numeros} esta ordenada de forma ascendente")
else: 
    print(f"la tupla {numeros} esta ordenada de forma descendiente")

#17. DADA LA TUPLA, VERIFICA SI EL SEGUNDO VALOR ES MAYOR A 30, SI LO ES "MUESTRAR EDAD MAYOR A 30" , SI NO "EDAD MENOR O IGUAL A 30"

edad=(int(input("Ingrese la primera edad: ")), int(input("Ingrese la segunda edad: ")), int(input("Ingrese la tercera edad: ")), int(input("Ingrese la cuarta edad: ")) )

if edad[1] < 30:
    print(f"la sedunda edad '{edad[1]}', es menor a 30")
elif edad[1] == 30:
    print(f"la sedunda edad '{edad[1]}', es igual a 30")
else:
    print(f"la segunda edad '{edad[1]}', es mayor mayor a 30")

#18. CONVIERTE LA TUPLA A LISTA, CAMBIA EL SEGUNDO VALOR A 10 SOLO SI ES IGUAL A 2, LUEGO VUELVELA A CONVERTIR A TUPLA Y MUESTRALA

numeros=(int(input("Ingrese el primer numero:")), int(input("Ingrese el segundo numero:")), int(input("Ingrese el tercer numero:")))
numeros_lista=list(numeros)
if numeros_lista[1] == 10:
    numeros_lista[1]= 2
    print("el segundo valor de la lista ha cambiado")
else:
    print("la lista quedará igual")

new_tupla=tuple(numeros_lista)

print(f"asi queda la nueva tupla : {new_tupla}")'''

#19. DADA LA TUPLA, ACCEDE AL SEGUNDO VALOR Y SI ES MAYOR DE 5, MUESTRA 'COORDENADA ALTA', SI NO, 'COORDENADA BAJA'

coordenadas=(int(input("Ingrese el primer punto: ")), int(input("ingrese el segundo punto: ")))
if coordenadas[1] > 5 :
    print(f"la coordenada {coordenadas[1]}, es una coordenada alta")
else:
    print(f"la coordenada {coordenadas[1]}, es una coordenada baja")

#20. 
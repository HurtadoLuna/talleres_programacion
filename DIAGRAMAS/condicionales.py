'''#2. Calcula el mayor de dos numeros ingresados 
num1= float(input("Ingrese el primer numero por favor: "))
num2= float(input("Ingrese el segundo numero por favor: "))

if num1 > num2:
    print(f"el numero {num1}, es mayor que el numero {num2}")
elif num1 < num2:
    print(f"el numero {num1}, es menor que el numero {num2}")#3333
else:
    print(f"los numeros {num1} y {num2} son iguales")

#3.  Determina si un numero es par o impar 


#4. Dado un numero, verifica si esta entre 10 y 20

num1= int(input("Ingrese el numero por favor: "))

if num1 >= 10 and num1 <= 20:
    print(f"el numero {num1} si esta entre 10 y 20")

else:
    print(f" el numero {num1} no esta dentro del rango")

# Dado tres numeros, encuentra ela mayor usando condicionales

num1= int(input("Ingrese el primer numero por favor: "))
num2= int(input("Ingrese el segundo numero por favor: "))
num3= int(input("Ingrese el tercer numero por favor: "))

if num1 > num2 and num1 > num3:
    print(f"el numero {num1} es mayor que los numeros {num2} y {num3}")
elif num2 > num1 and num2 > num3:
    print(f"el numero {num2} es mayor que los numeros {num1} y {num3}")
else:
    print(f"el numero {num3} es mayor que los numeros {num1} y {num2} ")

#6. Calcula el precio final con un 10% de descuento si el total es mayor a 100

num1= float(input("Ingrese el precio del primer producto por favor: "))
num2= float(input("Ingrese el precio del segundo producto por favor: "))
suma= num1 + num2 
descuento= suma - (suma * 0.10)

if suma >= 100:
    print(f"Este es su precio {suma} y este es con el precio con descuento {descuento}")
else:
    print(f"este es su precio total {suma}, su total es menor a 100 por lo tanto no se le puede realizar el descuento")

#7. Verifica si una persona puede votar

edad= int(input("Por favor ingrese su edad:"))

if edad >= 18:
    print(f"usted tiene {edad} años de edad, por lo tanto usted puede votar")
else:
    print(f"usted tiene {edad} años de edad, por lo tanto no puede votar por ser menor de edad")

#8 Dado el precio y tipo de cliente (VIP o normal), aplica un descuento del 20% solo al VIP
precio= float(input("Ingrese el precio del producto por favor: "))
usuario= input("Ingrese el tipo de usuario que es usted: ")
descuento= precio - ( precio * 0.20)

if usuario == "VIP": 
    print(f"Usted porque es cliente VIP su precio final sera de {descuento}")
else:
    print(f"Usted por ser un cliente normal no tendria descuento alguno por lo tanto su precio final es {precio}")

#9 Determina si un numero es multiplo del 5 y de 3 al mismo tiempo
num= float(input("Ingrese un numero: "))

if num % 5 == 0 and num % 3 == 0: 
    print(f" el numero {num} si es multiplo de ambos numeros")
else:
    print(f"el numero {num} no es multiplo de los dos numeros")'''

#10 Dado un numero mire si es divisible entre dos numeros dados 
num= int(input("ingrese un numero: "))
divisor1= int(input("Ingrese el numero divisor:"))
divisor2= int(input("Ingrese el numero divisor:"))

if num % divisor1 == 0 and num%divisor2 == 0:
    print(f"el numero  {num}es divisible por ambos numeros")
else:
    print(f"el numero {num} no es divisible por ambos numeros")





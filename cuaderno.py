# ejercicio 1 
'''base= 7 
expo1=5
expo2=2
operacion= (base**expo1)// (base**expo2) 
print(f"el resultado de esta operacion es: {operacion}")

# ejercicio 2 
base= 10
expo1=4
expo2=1
operacion= (base**expo1)// (base**expo2) 
print(f"el resultado de esta operacion es: {operacion}")

#ejercicio 3
base= 3
expo1=2
expo2=3
operacion= (expo1 * expo2)
result= operacion ** base
print(f"el resultado de esta operacion es: {result}")

#ejercicio 4

base= 3
expo1=2
expo2=4
operacion=  (expo1 * expo2)  ** base 
print(f"el resultado de esta operacion es: {operacion}")

#ejercicio 5

base= 5
expo1=3
expo2=2
operacion=  (expo1 * expo2)  ** base 
print(f"el resultado de esta operacion es: {operacion}")

#ejercicio 6

num1= 2
num2= 3
expo =2
operacion= num1 ** expo
operacion2= num2 ** expo
result= operacion * operacion2
print(f"el resultado de esta operacion es: {result}")

#-----------------------------------------------------------------TALLER-----------------------------------------------------------------

#Variables y Strings (1-10)

#1 
nombre= input("¿Cómo te llamas?")

print(f"Hola, {nombre}, bienvido/a")

#2
print(f"Bienvenido {nombre}, espero que te encuentres bien")

#3
ciudad= input("¿En que ciudad vives? R//") 
print(f"{ciudad}, wow que ciudad tal linda")

#4
print(f"Hola, soy {nombre} y vivo en {ciudad}")

#5
color= input("¿Cuál es tu color favorito?")

#6
print(f"tu color favorito es: {color}")

#7 
animal= input("¿Cuál es tu animal favorito?")
animal= input("¿Cuál es tu segundo animal favorito? R//")

print(f"tú animal favorito es: {animal}")

#8
nombre= input("¿Cómo te llamas? R//")
ciudad= input("¿En que ciudad vives? R//")
print(f"Yo me llamo {nombre}, y vivo en la ciudad de {ciudad}")

#9
nacionalidad= input("¿De donde eres?")
edad= int(input("Ingrese su edad: "))
telefono= int(input("Ingrese su numero telefono: "))
fruta= input("¿Cuál es tu fruta favorita?")

print(f"usted nacion es {nacionalidad}, tiene {edad}, su numero telefonico: {telefono}, y sufruta forita es: {fruta}")

#10
num1=int(input("Ingrese un numero: "))
num2=int(input("Ingrese un numero: "))
num3=int(input("Ingrese un numero: "))
num4=int(input("Ingrese un numero: "))
num5=int(input("Ingrese un numero: "))

operacion= num1 + num2 + num3 + num4 + num5 

print(f"la suma de los numeros {num1},{num2},{num3},{num4},{num5}, da como resultado: {operacion}")

# Operaciones matematicas con 'int'

#11
num1=int(input("Ingrese un numero: "))
num2=int(input("Ingrese el otro numero: "))

operacion= num1 + num2 

print((f"el resultado de la suma: {operacion}"))

#12
num1=int(input("Ingrese un numero: "))
num2=int(input("Ingrese el otro numero: "))

operacion= num1 - num2 

print((f"el resultado de la resta: {operacion}"))

#13
num1=int(input("Ingrese un numero: "))
num2=int(input("Ingrese el otro numero: "))

operacion= num1 * num2 

print((f"el resultado de la multiplicacion: {operacion}"))

#14
num1=int(input("Ingrese un numero: "))
num2=int(input("Ingrese el otro numero: "))

operacion= num1 / num2 

print((f"el resultado de la division: {operacion}"))

#15
num1=int(input("Ingrese un numero: "))
num2=int(input("Ingrese el otro numero: "))

operacion= num1 ** num2 

print(f"el resultado de la potenciacion: {operacion}")

#16
edad= int(input("Ingrese su edad: "))
print(f"usted tiene {edad} años")

#17
num1=10
suma= edad + num1

print(f"usted en unos 10 años tendria {suma} años de edad")

#18
num1=int(input("Ingrese un numero: "))
num2=int(input("Ingrese el otro numero: "))

operacion = num1 + num2 

print (f"el resultado de la suma es: {operacion}")

#19
num1=int(input("Ingrese un numero: "))
num2=int(input("Ingrese el otro numero: "))
operacion= num1 % num2 
print(f"el residuo de los numeros que ingreso es: {operacion}")

#20
ciencias= int(input("ingrese la nota de la asignatura de ciencias: "))
ingles= int(input("ingrese la nota de la asignatura de ingles: "))
fisica= int(input("ingrese la nota de la asignatura de fisica: "))
operacion= ciencias + ingles + fisica / 3 

print(f"el promedio de sus notas es: {operacion}")

#21
nombre_completo= input("Por favor ingrese su nombre completo: ")
print(f"Hola, {nombre_completo} bienvenidos")

#22
primer_nombre= nombre_completo[:4]
print(f"Tu primer nombre es:{primer_nombre}")

#23
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))

if num1 > num2:
    print(f"El numero mayor es el:{num1}")
elif num2 < num1:
    print(f"El numero mayor es el:{num2}")
else:
    print(f"Ambos numeros son iguales:")

#24
año_nacimiento= int(input("Ingrese su edad: "))
año= 2025
operacion= año - año_nacimiento
print (f"Usted nacio en el año {operacion}")

#25
nombre= input("¿Cómo te llamas? R//")
año_nacimiento= int(input("Ingrese su edad: "))
año=2025
operacion= año - año_nacimiento

print(f"Hola {nombre}, naciste en el año {operacion}, y tienes {año_nacimiento} años de edad")

#26
fruta= input("ingrese el nombre de una fruta: ")
print(f"Me gusta la {fruta}")'''

#27
num1= int(input("Ingrese el primer numero: "))
num2= int(input("Ingrese el segunfo numero: "))

suma= num1 + num2
resta= num1 - num2
multiplicacion= num1 * num2
division= num1 // num2

print (f"los numeros {num1} y {num2}, en suma {suma}, resta {resta}, multiplicacion: {multiplicacion}, division: {division}")
#2. Calcula el mayor de dos numeros ingresados 
num1= float(input("Ingrese el primer numero por favor: "))
num2= float(input("Ingrese el segundo numero por favor: "))

if num1 > num2:
    print(f"el numero {num1}, es mayor que el numero {num2}")
elif num1 < num2:
    print(f"el numero {num1}, es menor que el numero {num2}")
else:
    print(f"los numeros {num1} y {num2} son iguales")
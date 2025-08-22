#-------------------------------------------------WHILE-----------------------------------------------------------

"""num= int(input("ingrese un numero:"))

while num > 0:
    print(f"{num}")         #el print se puede dejar tanto dentro como fuera del bucle (afuera es mejor)
    num -= 1
print("El conteo terminó!")

#---------------------------------------Ejemplo Tabla de multiplicar---------------------------------------------

numero= int(input("ingrese su numero de la tabla de multiplicar:"))

iniciar=1 #inicia el conteo desde el numero que se le ingrese aqui (primer multiplicador)

print(f"\n inicia el contador en {numero}: ") #imprime un titulo para la tabla de multiplicar

while iniciar <= 10:  #el bucle se repite mientras "iniciar" sea menor que 10
    print(f"{numero} * {iniciar} = {numero * iniciar}") #muestra la multiplicacion y su rersultado
    iniciar += 1  #Incrementa "iniciar" de uno en uno en cada iteracion de la tabla

print("esta es su tabla de multiplicar") #imprime que la tabla ya esta lista

#------------------------------------------------------BREAK----------------------------------------------------
    
X=5
while True:
    X -= 1
    print(X)
    if X == 0:
        break
    print("el bucle ha finalizado")

#---------------------------------------------------WHILE-ELSE----------------------------------------------------   
chance=1
while chance <="""



#------------------------------------------------EJERCICIO CON WHILE---------------------------------------------  
# 1. SUMA HASTA CERO

num=int(input("Ingrese un numero:"))
while num == 0: 



#2. CONTRASEÑA SECRETA
contraseña= ""
while contraseña != "Python123":
    contraseña= input("ingrese la contraseña:")
print("la contraseña es correcta")

#3. LISTA DE COMPRAS
listas_compras= [input("Ingrese el nombre de su producto: "),input("Ingrese el nombre de su producto: "),input("Ingrese el nombre de su producto: ") ]




'''#ejercicio3
lista=[1,2,3,4]
lista.extend([5,6,7])
print(lista)

letras=["a","b"]
letras.extend(["ok"])
print(letras)

#ejercicio4
frutas=["uva", "manzana", "cereza", "mango", "pera"]
frutas.remove("uva")
print(frutas)

numeros= [1, 2, 3, 4, 2]
numeros.remove()
print(numeros)

#ejercicio 5

numeros= [1, 2, 3, 4]
print(numeros)

numeros.pop()
print(f"se elimino el ultimo valor de la lista: {numeros}")

lista=["uno", "dos", "tres"]
lista.pop(0)
print(f"se elimino el elemento que estaba en la posicion cero {lista}")

#ejercicio6
lista=[1, 2, 4 ,3]
lista.clear()
print(f"se ha vaciado la lista {lista}")

frutas=["uva", "manzana", "cereza", "mango", "pera"]
frutas.clear()
print(f"la lista fruta se ha vaciado {frutas}")
#ejercicio7
fruutas=["uva", "manzana", "cereza", "mango", "pera"]
print(fruutas.index("pera"))

numeros=[4,5,6,7,]
print(numeros.index(6))


#ejercicioo8
numeros=[1,2,3,4,3,5,]
print(f"el numero 3 aparece:{numeros.count(3)}")

letras= ["a", "b", "c", "a"]
print(f"la letra 'a' aparece:{letras.count("a")}")

#ejercicio9

numeeros=[5,1,4,2,3]
numeeros.sort()
print(numeeros)

letras=["z","a","m","b"]
letras.sort()
print(letras)

#ejercicio10

numeros=[1,2,3,4,5]
numeros.reverse()
print(numeros)

lista=["inicio", "medio", "fin"]
lista.reverse()
print(lista)

#ejercicio11

lista1=[1,2,3]
print(lista1)
nueva_lista=lista.copy()
print(nueva_lista)


lista1=["a","b","c"]
print(lista1)
nueva_lista=lista.copy()
nueva_lista.append("d")
print(nueva_lista)



#--------------------------------------ACTIVIDAD LISTAS----------------------------
LISTA1= []
LISTA1.append(100)
LISTA1.append("Hola Mundo")

print(LISTA1)

LISTA2= []
LISTA2.append("Hola y Adios")
LISTA2.append(300)

print(LISTA2)

LISTA3= []
LISTA3= LISTA1.copy()
LISTA3.remove("Hola Mundo")

print(LISTA3)

LISTA4= []
LISTA4= LISTA2.copy()
LISTA4.clear()

print(LISTA4)

LISTA5= []
LISTA5= LISTA4.copy()
LISTA5= LISTA3.copy()

print(LISTA5)'''
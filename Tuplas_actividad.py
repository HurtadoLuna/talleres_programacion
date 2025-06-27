'''mi_tupla=(1,2,3,)
mi_lista=list(mi_tupla)
print(mi_lista)

#-----------------------LISTA A DUPLA------------------------

mi_lista=(1,2,3,)
mi_dupla=tuple(mi_lista)
print(mi_dupla)

#-----------------------EJERCICIO 1 ------------------------
frutas=('manzana', 'pera')
lista_frutas=list(frutas)
nueva_fruta=input("ingrese una fruta por favor:")
lista_frutas.append(nueva_fruta)

lista_frutas=('manzana','pera', nueva_fruta)
tupla_frutas=tuple(lista_frutas)

print(f"asi quedo su lista: {tupla_frutas}")

#-----------------------EJERCICIO 2 ------------------------
tupla_calificaciones=(4.2, 3.8)
lista_calificaciones=list(tupla_calificaciones)
new_calificacion=float(input("ingrese su tercera calificacion: "))
lista_calificaciones.append(new_calificacion)

tupla_calificaciones=(4.2, 3.8, new_calificacion)
lista_nueva=tuple(tupla_calificaciones)

operacion= 4.2 + 3.8 + new_calificacion / 3

print(f"esta es la lista de sus calificaciones: {lista_nueva}, su nota final es de: {operacion}")

#-----------------------EJERCICIO 3 ------------------------

nombre=("ana","Gomez")
nombreyapellido=list(nombre)
num_documento=int(input("ingrese su numero de documento: "))
nombreyapellido.append(num_documento)

nombre=("ana","Gomez", num_documento )
tupla_noombre=tuple(nombre)



print(f"estos son sus nombres y numero de documeto: {tupla_noombre}")'''




#------------------------------------EJERCICIOS PRACTICOS------------------------

#1 
#numeros=(1,2,3,4,5)[1]

#numeros=(1,2,3,4,5).index(4)

numeros=(1,2,3,4,5).count(2)



print(numeros)











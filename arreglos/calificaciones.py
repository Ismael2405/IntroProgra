"""
Desarrolla un programa que permita
calcular el promedio de un conjunto de notas
ingresadas por el usuario
"""
while True:
    cantidad=int(input("Ingrese la cantidad de notas: "))
    if cantidad>0:
        break
    else:
        print("Ingresa una cantidad real!!!")
calificaciones=[0]*cantidad
for i in range(cantidad):
    calificaciones[i]=int(input(f"Ingresa la {i+1} calificación: "))
suma=0
for i in range (cantidad):
    suma+=calificaciones[i]
promedio=suma/cantidad
print(f"El promedio de notas es {int(promedio)}")
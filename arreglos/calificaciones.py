while True:
    cantidad=int(input("Proporciona la cantidad de notas: "))
    if cantidad>0:
        break
    else:
        print("Cantidad incorrecta, ingrese nuevamente")

"""Se crea una lista llamada vector con tantos elementos
como dijo el usuario (tamaño), todos inicialmente son 0.
Ejemplo: si tamaño = 3, entonces vector empieza como [0, 0, 0]"""

calificaciones=[0]*cantidad
for i in range(cantidad): 
    calificaciones[i]=int(input(f"Proporciona la {i+1} nota: ")) 
"""calculamos los valores guardados en el vector llamado (calificaciones) """
suma=0
for i in range(cantidad):
    suma=suma+calificaciones[i]
    suma
print(f"el promedio es: {int(suma/cantidad)}")
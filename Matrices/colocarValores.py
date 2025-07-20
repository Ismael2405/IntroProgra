"""
Introducir valores a una matriz
El tamaño de la matriz debe ser positivo y mayor a 2, es decir
las filas o columnas no pueden ser menores de 2
"""
while True:
    filas = int(input("Proporciona el número de filas \n(mayor o igual a 2): "))
    columnas = int(input("Proporciona el número de columnas \n(mayor o igual a 2): "))
    if filas >= 2 and columnas >= 2:
        break
    else:
        print("¡MAYOR A 2 TE DIGOOO!!")
"""
Ahora vamos a agregar los valores en la matriz, mostrando las posiciones
en donde las vamos a colocar. Usamos 2 ciclos For para que vaya por filas primero
y luego por columnas.
Pero antes, en cada posicion vamos a poner un 0, para que asi haya un espacio
´esperando´ por ser llenado.
"""
matriz=[([0]*columnas) for i in range(filas)]
for fila in range(filas):
    for columna in range(columnas):
        matriz[fila][columna]=int(input(f"Proporciona el valor de la posicion {fila}, {columna}: "))
"""
Una vez completada la matriz, tanto en filas como en columnas, se muestra la misma
nuevamente usando 2 ciclos for, uno para filas y otro para columnas
"""
for fila in matriz:
    print("  ".join(f"{valor:2}" for valor in fila))
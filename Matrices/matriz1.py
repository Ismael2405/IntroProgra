filas = 2
columnas = 3
matriz = [([0] * columnas) for i in range(filas)]
matriz[0][0] = 100
matriz[0][1] = 200
matriz[0][2] = 300
matriz[1][0] = 400
matriz[1][1] = 500
matriz[1][2] = 600
for fila in range(filas):
    for columna in range(columnas):
        print(matriz[fila][columna], end=" ")
    print()
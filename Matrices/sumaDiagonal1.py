"""Para hacer la suma diagonal
se debe tener la misma cantidad
de filas y columnas"""
filas = 3
columnas = 3
matriz = [([0] * columnas) for _ in range(filas)]
matriz[0][0] = 100
matriz[0][1] = 200
matriz[0][2] = 300
matriz[1][0] = 400
matriz[1][1] = 500
matriz[1][2] = 600
matriz[2][0] = 700
matriz[2][1] = 800
matriz[2][2] = 900
suma_diagonal=0
for fila in matriz:
    print(" ".join(f"{valor:2}" for valor in fila))
for i in range(filas):
    for j in range(columnas):
        if i==j:
            suma_diagonal += matriz[i][j]
print("La suma diagonal de la matriz es: ",suma_diagonal)
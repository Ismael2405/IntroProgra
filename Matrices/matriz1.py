"""filas = 2
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
    print()"""
# Validación del tamaño de la matriz
while True:
    filas = int(input("Proporciona el número de filas (mayor a 1): "))
    columnas = int(input("Proporciona el número de columnas (mayor a 1): "))
    if filas > 1 and columnas > 1:
        break
    else:
        print("¡MAYOR A 1 TE DIGOOO!!")

# Inicializar matriz
matriz = [[0] * columnas for _ in range(filas)]

# Llenar la matriz con datos del usuario
for fila in range(filas):
    for columna in range(columnas):
        matriz[fila][columna] = int(input(f"Valor en posición [{fila},{columna}]: "))

# Imprimir la matriz como tabla
for fila in matriz:
    print("  ".join(f"{valor:5}" for valor in fila))

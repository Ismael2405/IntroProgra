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

"""
SUMA RENGLONES Y COLUMNAS DE UNA MATRIZ
Realiza la suma de los renglones y columnas de una matriz.
El resultado de cada renglón y cada columna se debe agregar a un
arreglo por separado.
"""
while True:
    filas = int(input("Proporciona el número de filas \n(mayor o igual a 2): "))
    columnas = int(input("Proporciona el número de columnas \n(mayor o igual a 2): "))
    if filas >= 2 and columnas >= 2:
        break
    else:
        print("QUE MAYOR A 2 TE ESTOY DICIENDO!!!")

matriz = [[0]*columnas for _ in range(filas)]

for i in range(filas):
    for j in range(columnas):
        matriz[i][j] = int(input(f"Proporciona el valor de la posición {i}, {j}: "))

suma_filas = [0] * filas
for i in range(filas):
    for j in range(columnas):
        suma_filas[i] += matriz[i][j]  

suma_columnas = [0] * columnas
for j in range(columnas):
    for i in range(filas):
        suma_columnas[j] += matriz[i][j]

print("\nMatriz:")
for fila in matriz:
    print("  ".join(f"{valor:3}" for valor in fila))

print("\nSuma de filas:", suma_filas)
print("Suma de columnas:", suma_columnas)
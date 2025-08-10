"""
Suma todos los valores en la diagonal principal de una matriz cuadrada
(El número de filas debe ser igual al número de columnas)
"""
while True:
    filas = int(input("Proporciona el número de filas \n(mayor que 1): "))
    columnas = int(input("Proporciona el número de columnas \n(mayor que 1): "))
    if filas > 1 and columnas > 1:
        if filas == columnas:
            break
        else:
            print("¡DEBEN SER IGUALES TE DIGOOO!!")
    else:
        print("¡MAYOR A 1 TE DIGOOO!!")

"Aqui agregamos los valores en la matriz, tanto en filas como en columnas"
matriz = [[0]*columnas for _ in range(filas)]
for i in range(filas):
    for j in range(columnas):
        matriz[i][j] = int(input(f"Proporciona el valor de la posición {i}, {j}: "))
"Aqui mostramos la matriz como tal"
for fila in matriz:
    print("  ".join(f"{valor:2}" for valor in fila))
"Finalmente, aqui hacemos la suma de todos los numeros en diagonal"
suma_diagonal = 0
for i in range(filas):
    for j in range(columnas):
        if i==j:
            suma_diagonal += matriz[i][j]
print(f"\nLa suma de la diagonal principal es: {suma_diagonal}")
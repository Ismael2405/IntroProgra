"""Encontrar la posición del número mayor y del número menor
Una vez encontrados los valores, imprimir tanto los números
mayor y menor, además la posición en la matriz de cada uno
"""
while True:
    filas=int(input("Ingrese la cantidad de filas: "))
    columnas=int(input("Ingrese la cantidad de columnas: "))
    if filas>=2 and columnas>=2:
        break
    else: print("MAYOR A 2 TE DIJE!!!")
matriz=[[0]*columnas for _ in range(filas)]
for i in range(filas):
    for j in range(columnas):
        matriz[i][j]=int(input(f"Ingresa la posición {i},{j} de la matriz: "))

print("\nMatriz")
for i in range(filas):
    for j in range(columnas):
        print(matriz[i][j], end=" ")
    print( )


mayor=matriz[0][0]
posición_may=(0,0)
menor=matriz[0][0]
posición_men=(0,0)

for i in range(filas):
    for j in range(columnas):
        if matriz[i][j]>mayor:
            mayor=matriz[i][j]
            posición_may=(i,j)
        elif matriz[i][j]<menor:
            menor=matriz[i][j]
            posición_men=(i,j)

print("El menor de todos es: ",menor," y están en la posición ",posición_men)
print("El mayor de todos es: ",mayor," y están en la posición ",posición_may)
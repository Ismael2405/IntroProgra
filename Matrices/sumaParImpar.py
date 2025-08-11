"""Sumar los números pares e impares de una matriz
y mostrar la suma en pantalla"""
while True:
    filas=int(input("Ingresa la cantidad de filas: "))
    columnas=int(input("Ingresa la cantidad de columnas: "))
    if filas>=2 and columnas>=2:
        break
    print("Ingrese nuevamente el tamaño de la matriz")

matriz=[[0]*columnas for _ in range(filas)]
for i in range(filas):
    for j in range(columnas):
        matriz[i][j]=int(input(f"Ingrese el valor de la posición {i}, {j}: "))
print("\nMatriz")
for i in range(filas):
    for j in range(columnas):
        print(matriz[i][j], end=" ")
    print( )

cant_par=0
cant_impar=0
suma_impar=0
suma_par=0
for i in range(filas):
    for j in range(columnas):
        if matriz[i][j]%2==0:
            suma_par+=matriz[i][j]
            cant_par+=1
        else:
            suma_impar+=matriz[i][j]
            cant_impar+=1

print("\n")
print(f"la suma de los pares es {suma_par}")
print(f"la suma de los impares es {suma_impar}")
print(f"Hay {cant_par} números pares y {cant_impar} números impares")


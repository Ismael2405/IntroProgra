"Coloca la matriz en orden inverso y muestra el resultado"
while True:
    print("Introduce la cantidad de filas y columnas (DEBE SER MAYOR O IGUAL A 2)")
    filas=int(input("filas: "))
    columnas=int(input("columnas: "))
    if filas>=2 and columnas>=2:
        break
    else: print("Introduzca nuevamante los valores")

matriz=[[0]*columnas for _ in range(filas)]
for i in range(filas):
    for j in range(columnas):
        matriz[i][j]=int(input(f"Introduce el valor {i},{j} de la matriz: "))

print("\nMatriz")
for i in range(filas):
    for j in range(columnas):
        print(matriz[i][j], end=" ")
    print( )

nueva=[[0]*columnas for _ in range(filas)]
for i in range(filas):
    for j in range(columnas):
       nueva[i][j] = matriz[filas-1-i][columnas-1-j]
    
print("\nMatriz invertida")
for i in range(filas):
    for j in range(columnas):
        print(nueva[i][j], end=" ")
    print( )
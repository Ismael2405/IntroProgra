"""mostrar valores de un arreglo ingresado por teclado
El tamaño del vector o array (DEBE SER POSITIVO)"""
while True:
    tamaño=int(input("Proporciona el tamaño del array(solo positivos): "))
    if tamaño>0:
        break
    else:
        print("Positivooos te digo")
"""Se crea una lista llamada vector con tantos elementos
como dijo el usuario (tamaño), todos inicialmente son 0.
Ejemplo: si tamaño = 3, entonces vector empieza como [0, 0, 0]"""
vector=[0]*tamaño
"""
for i in range(tamaño): → Un ciclo que se repite "tamaño" veces.
i toma los valores 0, 1, 2, ..., hasta tamaño-1.
Dentro del ciclo:
Pide al usuario un número.
Lo convierte en entero (int()).
Lo guarda en la posición i del vector.
"""
for i in range(tamaño): 
    vector[i]=int(input(f"Proporciona el valor {i+1} del arreglo: "))
"""
Primero imprime una frase para avisar que va a mostrar los datos.
Luego otro ciclo for para recorrer todos los elementos del vector.
Para cada elemento:
Muestra su número de orden (i+1) y su posición real en la lista (vector[i]).
"""
print("Los valores almacenados son: ")
for i in range (tamaño):
    print(f"{i + 1}. Valor[{i}] = {vector[i]}")
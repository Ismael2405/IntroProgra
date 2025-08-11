"""
Crea un programa que solicite al usuario un arreglo de números enteros
y luego imprima ese arreglo en orden inverso.
"""

while True:
    tamaño = int(input("Ingresa el tamaño del array: "))
    if tamaño > 0:
        break
    else:
        print("Ingresa un número válido!!!")

numbers = [0] * tamaño
for i in range(tamaño):
    numbers[i] = int(input(f"Ingresa el valor {i} del arreglo: "))

print("\nArreglo original:")
print(numbers)

nuevo = [0] * tamaño
for i in range(tamaño):
    nuevo[i] = numbers[tamaño - 1 - i]

print("\nArreglo invertido:")
print(nuevo)
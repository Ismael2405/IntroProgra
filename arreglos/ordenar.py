"""
Escribe un programa que lea un arreglo de números enteros
y luego lo ordene de menor a mayor. Muestra el arreglo original y el arreglo ordenado.
"""
while True:
    tamaño = int(input("Ingrese el tamaño del array: "))
    if tamaño > 0:
        break
    else:
        print("Ingrese un número real!!!")
numbers = [0] * tamaño
for i in range(tamaño):
    numbers[i] = int(input(f"Ingrese el valor {i} del arreglo: "))
print(numbers)
for i in range(tamaño - 1):
    for j in range(tamaño - 1 - i):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print(numbers)

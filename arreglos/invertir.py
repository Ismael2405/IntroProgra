"""
Crea un programa que solicite al usuario un arreglo de números enteros
y luego imprima ese arreglo en orden inverso.
"""
while True:
    tamaño=int(input("Ingresa el tamaño del array: "))
    if tamaño>0:
        break
    else:
        print("Ingresa un numero real!!!")
numbers=[0]*tamaño
for i in range (tamaño):
    numbers[i]=int(input(f"Ingresa el valor {i} del arreglo: "))
print(numbers)
nuevo=[]
for i in range(tamaño,0,-1):
    nuevo.append(numbers[i-1])
print(nuevo)

"""
Realiza un programa que pida al usuario un arreglo de números enteros, y luego pregunte por un número a buscar.
El programa debe indicar si ese número existe o no en el arreglo y,
si existe, en qué posición(es) se encuentra.
"""
while True:
    tamaño=int(input("Ingrese el tamaño del array: "))
    if tamaño>0:
        break
    else:
        print("Ingrese un tamaño real!!!")
numbers=[0]*tamaño
for i in range(tamaño):
    numbers[i]=int(input(f"Ingresa el valor {i} del array: "))
numero=int(input("Ingrese el número que desea encontrar: "))
print(numbers)
posiciones=[]
for i in range(tamaño):
    if numbers[i]==numero:
        posiciones.append(i)
print(f"El numero {numero} esta en la posiciones: {posiciones}")
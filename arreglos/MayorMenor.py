while True:
    tamaño=int(input("Ingrese el tamaño del arreglo: "))
    if tamaño>0:
        break
    else:
        print("Ingrese un tamaño real")
numbers=[0]*tamaño
for i in range(0,tamaño):
    numbers[i]=int(input(f"Ingrese el valor {i} del arreglo: "))
mayor=numbers[0]
menor=numbers[0]
for i in range(1,tamaño):
    if numbers[i]>mayor:
        mayor=numbers[i]
    elif numbers[i]<menor:
        menor=numbers[i]
print("El mayor de todos es: ",mayor)
print("El menor de todos es: ",menor)
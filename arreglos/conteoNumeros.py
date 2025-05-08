"Realiza un programa que cuente el total de los numeros positivos, negativos y neutrales"
"es decir 0, de un array"
while True:
    tamaño=int(input("Ingrese el tamaño del array: "))
    if tamaño>0:
        break
    else:
        print("Ingrese un tamaño válido")
numbers=[0]*tamaño
for i in range(tamaño):
    numbers[i]=int(input(f"Ingrese el valor {i} del array: "))
contMay=0
contMen=0
neutro=0
for i in range(0,tamaño):
    if numbers[i]>0:
        contMay+=1
    elif numbers[i]<0:
        contMen+=1
    else:
        neutro+=1
print(f"Hay {contMay} numeros positivos")
print(f"Hay {contMen} numeros negativos")
print(f"Hay {neutro} numeros neutros")
while True:
    dimension=int(input("Ingrese cuantos fibonacci quiere: "))
    if dimension>0:
        break
    else:
        print("ingrese un numero valido: ")
fibonacci=[0]*dimension
fibonacci[0]=0
fibonacci[1]=1
for i in range(2,dimension):
    fibonacci[i]=fibonacci[i-1]+fibonacci[i-2]
for i in range(dimension):
    print(fibonacci[i])
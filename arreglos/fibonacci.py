"""Serie fibonacci con arreglos"""
while True:
    cantidad=int(input("Ingrese cuántos fibonacci quiere: "))
    if cantidad>0:
        break
    else:
        print("Ingrese un número positivo!!!")

fibonacci=[0]*cantidad
b=0
a=1
print(b)
print(a)
for i in range(cantidad-2):
    fibonacci[i]=c=b+a
    b=a
    a=c
    print(fibonacci[i])
"""recuerda que con esto puedes mostrar los resultados"""

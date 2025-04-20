"""determinar si un numero es positivo o negativo"""
a=int(input("Dame un número cualquiera: "))
if a>0:
    print("El número es positivo")
else:
    if a==0:
        print("El número es cero")
    else:
        print("El número es negativo")
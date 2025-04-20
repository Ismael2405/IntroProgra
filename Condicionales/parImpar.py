"""Determinar si in número es par o impar"""
num=int(input("Dame un número positivo: "))
if num>0:
    if num%2==0:
        print(f"el número es par")
    else:
        print("El número es impar")
else:
    print("positivo te dije pndj")
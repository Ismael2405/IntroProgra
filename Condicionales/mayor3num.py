"""Calcular el mayor de 3 numeros"""
a,b,c=map(int,input("Dame 3 números: ").split())
if a>=b and a>=c:
    print(f"el mayor es {a}")
else:
    if b>=a and b>=c:
        print(f"el mayor es {b}")
    else:
        print(f"el mayor es {c}")
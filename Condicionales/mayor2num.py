"""Calcula el mayor de 2 números"""
a,b=map(int,input("Ingresa dos numeros: ").split())
if a<b:
    print(f"El mayor es: {b}")
else:
    print(f"El mayor es: {a}")
"""proporcione un número de 2 dígitos"""
while True:
    a=int(input("Introduzca un número de 2 dígitos: "))
    if 99>=a>=10:
        break
print(f"El números es {a}")
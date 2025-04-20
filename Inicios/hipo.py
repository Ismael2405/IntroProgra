"""//Dados dos (2) lados de un triángulo en cm,
calcular la hipotenusa del mismo"""
import math
print("Digite un lado del triangulo:")
a=int(input())
print("Digite el otro lado del triangulo:")
b=int(input())
hipo=math.sqrt((a**2)+(b**2))
print(f"La hipotenusa es: {int(hipo) }")
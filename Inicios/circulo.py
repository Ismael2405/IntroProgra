"""Ejercicio2
Saca el area de un circulo y su perimetro a partir de su area"""
import math
print("Ingresa el radio: ")
r=int(input())
area=math.pi*(r**2)
perimetro=2*math.pi*r
print(f"El area del circulo es {int(area)} y el perimetro es {int(perimetro)}")
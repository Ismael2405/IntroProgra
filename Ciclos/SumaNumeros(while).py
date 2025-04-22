"""Sumar los primeros 5 numeros"""
print("Con ciclo while")
print(" ")
suma=0
n=6
contador=0
while n>contador:
    print("acumulador + suma: ",suma,"+",contador)
    suma+=contador
    print("La suma es: ",suma)
    contador+=1
"""Sumar los primeros 5 numeros"""

print("")
print("Con ciclo For")
print(" ")
suma=0
for i in range(1,6,1):
    print("acumulador + suma: ",suma,"+",i)
    suma=suma+i
    print("la suma parcial: ",suma)
    
"""Multiplica los primeros 5 números"""
print("Con ciclo while")
print(" ")
multiplicacion=1
n=6
contador=1
while n>contador:
    print("acumulador * suma: ",multiplicacion,"*",contador)
    multiplicacion=multiplicacion*contador
    print("La multiplicación es: ",multiplicacion)
    contador+=1


print(" ")
print("Con ciclo For")
print(" ")
multiplicación=1
for i in range(1,6,1):
    print("acumulador * multiplicación: ",multiplicación,"*",i)
    multiplicación=multiplicación*i
    print("la multiplicación parcial: ",multiplicación)
    
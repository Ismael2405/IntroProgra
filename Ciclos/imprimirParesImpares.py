"""
imprimir los primeros 10 numeros pares e impares positivos
"""
print("Numeros pares")
for numero in range (0,11):
    if numero%2==0:
        print(numero)
print("Numeros impares")
for numero in range(0,11):
    if numero%2!=0:
        print(numero)
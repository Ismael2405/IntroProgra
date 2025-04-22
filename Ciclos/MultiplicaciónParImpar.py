"""Multiplicar los primeros números pares"""
valor_par=1
valor_impar=1
for i in range(1,7):
    if i%2==0:
        print("Multiplicación de pares: ",valor_par,"*",i)
        valor_par=valor_par*i
    else:
        print("Multiplicación de impares: ",valor_impar,"*",i)
        valor_impar=valor_impar*i
print("Multiplicación de valores pares: ",valor_par)
print("Multiplicación de valores impares: ",valor_impar)

print(" ")
print("Con ciclo while")
print(" ")

valor_par=1
valor_impar=1
n=7
i=1
while n>i:
    if i%2==0:
        print("La multipicación es: ",valor_par,"*",i)
        valor_par=valor_par*i
        i+=1
    else:
        print("La multipicación es: ",valor_impar,"*",i)
        valor_impar=valor_impar*i
        i+=1
print("Multiplicación de valores pares: ",valor_par)
print("Multiplicación de valores impares: ",valor_impar)

"""Has un calculadora con las operaciones basicas con 2 numeros"""
a,b=map(int,input("Ingresa 2 números: ").split())
print("Selecciona un número del menu:\n 1.Suma  \n 2.Resta \n 3.Multiplicación \n 4.División \n 5.Salida")
opc=int(input())
if opc==1:
    print("La suma de los números ingresados son:",a+b)
elif opc==2:
    print("La resta de los números ingresados son:",a-b)
elif opc==3:
    print("La multiplicación de los números ingresados son:",a*b)
elif opc==4:
    print("La división de los números ingresados son:",a/b)
elif opc==5:
    print("pues ya vete alv")
else:
    print("que escojas una opcion del menuuuú, pndj")
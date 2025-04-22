"""Elige una opcion DEL MENU"""
while True:
    print("Menú \n1.Saludar \n2.Salida")
    while True:
        opc=int(input("Elija una opcion del menú: "))
        condicion=(opc==1) or opc==2
        if not condicion:
            print("Del menuuú, webon ")
        else:
            break
    if opc==1:
        print("Cómo es chamo??")
    else:
        print("ya largate")
        break
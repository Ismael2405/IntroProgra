"""determina si aprobaste o no, usando solo tu nota"""
nota=int(input("Ingresa tu nota: "))
if 100>=nota>=85:
    print("Crack,fiera,mastodonte. Aprobaste con buena nota")
elif 85>nota>=65:
    print("Bueno, al menos aprobaste wey")
elif 65>nota>=51:
    print("Casi te tiras, nmms")
elif nota<50:
    print("ya valiste bro")
else:
    print("si cjd? dame una calificación real AJAJA")
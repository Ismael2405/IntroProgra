"""Realiza la serie fibonacci usando los ciclos For y while"""

"""
0+1=1
1+1=2
1+2=3
2+3=5
3+5=8
5+8=13
"""
print("Ciclo While")
b=0
a=1
lim=10
acom=0
print(b)
print(a)
while acom<lim-2:
    c=b+a
    print(c)
    b=a
    a=c
    acom+=1

print("")
print("Ciclo For")
b=0
a=1
lim=10
print(b)
print(a)
for i in range(lim-2):
    c=b+a
    print(c)
    b=a
    a=c
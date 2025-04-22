"""Determine el Factorial de un número"""
print("Bucle While")
num=int(input("Dame un número: "))
i=1
facto=1
while num>=i:
    facto=facto*i
    i+=1
print("Su factorial es: ", facto)


print("")
print("Bucle For")
num=int(input("Dame un número: "))
facto=1
for i in range(1,num+1):
    facto=facto*i
print("Su factorial es: ", facto)
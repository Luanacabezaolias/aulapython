numero = int(input("Insira um numero com 3 digitos: "))
a = numero % 100
b = numero // 100
c= a // 10
d = a % 10
e = (d * 10) + (c * 10) + b 
print (e)
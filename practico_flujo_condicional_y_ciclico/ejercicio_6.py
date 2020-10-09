num1 = int(input("Ingrese número: "))
num2 =int(input("Ingrese otro número: "))
if   num1 > num2:
    print(num2,num1)
else:
    print(num1,num2)



num1 = int(input("Ingrese número: "))
num2 = int(input("Ingrese otro número: "))
num3 = int(input("Ingrese un tercer número: "))
min=min(num1, num2, num3)
max=max(num1, num2, num3)
mid=(num1+num2+num3)-min-max
print(min," ", mid," ", max)
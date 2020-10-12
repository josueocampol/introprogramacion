suma = 0
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

for i in range(num1+1,num2):
        suma += i

print(f"La suma es: {suma}")
num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))

def numM(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2

print ("El mayor es: ",numM(num1,num2))
num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))
num3 = int(input("Número 3: "))

def numM(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        print(num3)
    else:
        return ("Los números son iguales.")

print(numM(num1,num2,num3))
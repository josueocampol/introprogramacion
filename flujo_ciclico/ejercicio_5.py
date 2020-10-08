num = int(input("Digite un numero: "))
while num == 1:
    print("*")
    num = int(input("**"))
if num == 2:
    print("**")
    num = int(input("***"))
elif num == 3:
    print("***")
    num = int(input("****"))
elif num == 4:
    print("****")
    num = int(input("*****"))
elif num == 5:
    print("*****")
    num = int(input("******"))
elif num == 6:
    print("******")
    num = int(input("*******"))
suma = 0
for i in range (1,num+6):
    suma = suma + i
    print(suma)
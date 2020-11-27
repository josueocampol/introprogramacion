import random
n=int(input("Ingrese el tamaño del array: "))
vectorA=[]

for i in range(0,n):
    num = random.randint(0, 300)
    p=str(num)
    vectorA.append(num)
    g = p[len(p) - 1]

ultimodigito = input("Mostrar números que acaben en: ")

vectorB = []
if g == ultimodigito:
        vectorB.append(p)

print(vectorA)
print(vectorB)
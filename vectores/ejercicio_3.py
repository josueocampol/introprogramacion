import random
num=int(input("Ingrese el tamaño del vector: "))
def VectorRandom(num):
    vector=[]
    for i in range(1,num+1):
        vector.append(random.randint(0,300))
    return vector


VNumAl=VectorRandom(num)
vectorEncontrado=[]
print(VNumAl)

ultimodigito=int(input("Mostrar los números que acaben en: "))
for i in range(0,num):
    valor=VNumAl[i]
    residuo = valor % 10
    if (residuo == ultimodigito):
        vectorEncontrado.append(valor)
print(vectorEncontrado)
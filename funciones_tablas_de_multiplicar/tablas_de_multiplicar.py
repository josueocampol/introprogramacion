num=int(input("Introduce el número: "))
def tablaM(numI):
    for i in range (1,11):
        print(numI, "x", i," = ",i*numI)


for i in range (1,11):
    print("La tabla del ",i,"es: ",tablaM(i))
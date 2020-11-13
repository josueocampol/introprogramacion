def imprimirAhorcado(intentos):
    if(intentos==5):
        print("================")
        print("=")
        print("=")
        print("=")
        print("=")
        print("=")
        print("=")
        print("=")
        print("===")
    if (intentos == 4):
        print("================")
        print("=              |")
        print("=              O")
        print("=")
        print("=")
        print("=")
        print("=")
        print("=")
        print("===")
    if (intentos == 3):
        print("================")
        print("=              |")
        print("=              O")
        print("=          }-------{")
        print("=")
        print("=")
        print("=")
        print("=")
        print("===")
    if (intentos == 2):
        print("================")
        print("=              |")
        print("=              O")
        print("=          }-------{")
        print("=              |")
        print("=              |")
        print("=")
        print("=")
        print("===")
    if (intentos == 1):
        print("================")
        print("=              |")
        print("=              O")
        print("=          }-------{")
        print("=              |")
        print("=              |")
        print("=             /")
        print("=            /")
        print("===         /")
    if (intentos == 0):
        print("================")
        print("=              |")
        print("=              O")
        print("=          }-------{ ")
        print("=              |")
        print("=              |")
        print("=             /\ ")
        print("=            /  \ ")
        print("===         /    \ ")



palabraoculta="ARROZ"
tam=len(palabraoculta)
vectorPalabraOculta=[]
vectorPalabraGuiones=[]
intentos=6
for pos in range (0,tam,1):
    vectorPalabraOculta.append(str(palabraoculta[pos]))
    vectorPalabraGuiones.append("-")

print(vectorPalabraGuiones)
while(intentos>0):
    print("Cantidad de intentos: ",intentos)
    coincidencias=0
    cantidadguiones=0
    letra=input("Ingrese una letra: ")
    for pos in range(0,tam,1):
        if(letra.upper()==vectorPalabraOculta[pos]):
            vectorPalabraGuiones[pos]=letra.upper()

    print(vectorPalabraGuiones)

    for pos in range(0,tam,1):
        if(vectorPalabraGuiones[pos]=="-"):
            cantidadguiones=cantidadguiones+1

    if(coincidencias==0):
        intentos=intentos-1
        imprimirAhorcado(intentos)

    if(cantidadguiones==0):
        print("Ganaste, adivinaste la palabra")
        intentos=-1


if(intentos==0):
    print("Se terminaron tus intentos! Perdiste!")




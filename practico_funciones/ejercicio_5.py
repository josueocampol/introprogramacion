palabra=input("Ingrese una frase: ")
print(palabra)

tam=len(palabra)
tam=tam-1
print("Indice del 0 al ",tam)

invertida=""
for indice in range (tam,-1,-1):
    invertida=invertida+palabra[indice]

print(invertida)
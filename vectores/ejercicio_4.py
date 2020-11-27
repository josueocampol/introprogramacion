n=int(input("Ingrese un número: "))
EnString=str(n)
nArmado=""
inicio=len(EnString)-1
final=-1

for pos in range(inicio,final,-1):
    nArmado=nArmado+EnString[pos]
print (nArmado)

if(nArmado==EnString):
    print("Es capicua")
else:
    print("No es capicua")
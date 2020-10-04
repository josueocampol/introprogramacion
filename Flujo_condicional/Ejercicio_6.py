año = int(input("Escriba el año: "))
if  año%4 == 0:
    if  año%100 == 0:
        if  año%400 == 0:
            print("El año si es bisiesto")
        else:
            print("El año no es bisiesto")
    else:
        print("El año si es biciesto")
else :
    print("El año no es bisiesto")
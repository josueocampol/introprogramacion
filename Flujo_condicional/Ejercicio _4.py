agua_consumida = int(input("Ingrese su consumo total de agua: "))
if  agua_consumida < 100:
    print("usted debe pagar Bs. 1.00")
elif    agua_consumida > 100 and agua_consumida < 499:
    print("usted debe pagar Bs. 1.20")
elif    agua_consumida > 500 and agua_consumida < 999:
    print("usted debe pagar Bs. 1.50")
else    :
    print("usted debe pagar 2.00")
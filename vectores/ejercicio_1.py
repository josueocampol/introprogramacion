

def factorial(numero):
    FACT = [numero]
    fac = 1
    for i in range(1,numero+1):
        fac = fac * i

        FACT.append(fac)
    print(FACT)

numero=int(input("Ingrese un número: "))
factorial(numero)

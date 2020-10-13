def imc(estatura, peso):
    return peso / estatura**2

estatura = float(input("Ingrese su estatura: "))
peso = int(input("Ingrese su peso: "))

indice = imc(peso, estatura)

print("Su IMC es: {}".format(indice))
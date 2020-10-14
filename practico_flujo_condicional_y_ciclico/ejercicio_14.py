estatura = float(input("Ingrese su estatura: "))
peso = int(input("Ingrese su peso: "))
edad = int(input("Ingrese su edad: "))

imc = peso / estatura**2
if imc < 22.0 and edad < 45:
    print(f"Su IMC es: {imc}, su condición de riesgo es bajo")
elif imc < 22.0 and edad >= 45:
    print(f"Su IMC es: {imc}, su condición de riesgo es medio")
elif imc >= 22.0 and edad < 45:
    print (f"Su IMC es: {imc}, su condición de riesgo es medio")
elif imc >= 22.0 and edad >= 45:
    print (f"Su IMC es: {imc}, su condición de riesgo es alta")
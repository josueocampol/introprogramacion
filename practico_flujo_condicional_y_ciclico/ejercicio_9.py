operando = int(input("Ingrese Operando: "))
operador = input("Operador: ")
operando2 = int(input("Ingrese Operando: "))
if operador == "+" :
    print(f"Resultado: {(operando) + (operando2)}")
elif operador == "-" :
    print(f"Resultado: {(operando) - (operando2)}")
elif operador == "*" :
    print(f"Resultado: {(operando) * (operando2)}")
elif operador == "/" :
    print(f"Resultado: {float(operando) // (operando2)}")
elif operador == "**":
    print(f"Resultado: {(operando) ** (operando2)}")
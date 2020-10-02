monto_a_invertir = int(input("Ingrese su monto a invertir: "))
interes_anual = int(input("Interes anual: "))
periodo_de_ahorro = int(input("Numero de años a invertir: "))

ganancia_generada = monto_a_invertir * (1 + interes_anual) ** periodo_de_ahorro

print(f"Ganancia neta generada por la inversion: {ganancia_generada}")
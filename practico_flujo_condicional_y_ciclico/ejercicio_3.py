dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))
cociente = dividendo // divisor
resto = dividendo % divisor
if dividendo%divisor ==0:
    print("La división es exacta")
else:
    print("La división es inexacta")
print(f"cociente: {cociente}")
print(f"resto: {resto}")
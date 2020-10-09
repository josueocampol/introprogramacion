palabra1 = input("Ingrese palabra 1: ")
palabra2 = input("Ingrese palabra 2: ")
len(palabra1)
len(palabra2)
if  len(palabra1) > len(palabra2):
    print(f"La palabra: {palabra1} tiene {len(palabra1)-len(palabra2)} letras más que {palabra2}")
elif    len(palabra2) > len(palabra1):
    print(f"La palabra: {palabra2} tiene {len(palabra2)-len(palabra1)} letras más que {palabra1}")
else:
    print("Las dos palabras tienen el mismo largo")
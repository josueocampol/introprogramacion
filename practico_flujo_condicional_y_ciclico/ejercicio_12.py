num = int(input("Cantidad de palabras: "))
palabra_mas_larga = ""
for i in range (1,num +1):
    palabra_actual = input(f"Ingrese palabra: ")
    if len(palabra_actual) >= len(palabra_mas_larga):
        palabra_mas_larga = palabra_actual
print(f"La palabra más larga es: {palabra_mas_larga}")

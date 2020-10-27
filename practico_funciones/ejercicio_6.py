def palindromo(palabra):
    x=len(palabra)
    x = x-1
    palabra_invertida = ""
    for i in range(x, -1, -1):
        palabra_invertida = palabra_invertida + palabra[i]
    palabra2 = palabra_invertida
    if palabra == palabra2 :
        print("True.")
    else:
        print("False.")

palabra = input("Ingrese palabra: ")
palindromo(palabra)
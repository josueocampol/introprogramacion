def largo_cadena(lista):
    cont=0

    for i in lista:
        cont+=1
    print("La cadena tiene %d caracteres" %cont)

string = input("Ingrese su cadena de carcteres: ")
largo_cadena(string)
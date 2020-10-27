def comp (x) :
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        return ("True")
    else:
        return ("False")

if __name__ == "__main__":
    le = str(input("Ingrese una letra: "))
    var = comp(le)

    if var == True:
        print("Es vocal")
    else:
        print("No es vocal")
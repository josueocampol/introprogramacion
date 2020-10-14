numero_de_terminos = int(input("n: "))
suma = 0
for i in range(1, numero_de_terminos):
    if i % 2 == 0:
        signo =-1
    else:
        signo = 1
    valor_termino_actual = signo / (1 + 2*(i-1))
    suma += valor_termino_actual
pi = 4*suma
print(pi)
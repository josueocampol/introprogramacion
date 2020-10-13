def NumeroN(n):
        numero = ((-1)**n)/((2*n)+1)
        return numero

pi = 0
for i in range(10000):
    pi = pi + NumeroN(i)
print(pi*4)
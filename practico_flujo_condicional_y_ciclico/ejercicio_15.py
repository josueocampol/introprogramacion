num = int(input("n: "))
while num != 1:
    if num % 2 == 0:
        print("%d,"%(num), end = "")
        num = num / 2
    else:
        print("%d,"%(num), end = "")
        num = (num*3) + 1

    if num == 1:
        print("1")

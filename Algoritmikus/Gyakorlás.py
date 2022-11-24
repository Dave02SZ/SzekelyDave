#csigaalakban megy a pont és n szer kell megtennie

n = int(input("Kérlek írd be, hogy mennyit lépjen a pont: "))
n2 = 0

x = 0
y = 0
x1 = 1
y1 = 1
pozitiv = True
f = False

while True:
    if pozitiv is True:
        for i in range(x1):
            x += 1
            n2 += 1
            print(x, y)
            if n2 == n:
                f = True
                break
        if f is True:
            break
        for i in range(y1):
            y += 1
            n2 += 1
            print(x, y)
            if n2 == n:
                f = True
                break
        if f is True:
            break

    if pozitiv is False:
        for i in range(x1):
            x -= 1
            n2 += 1
            print(x, y)
            if n2 == n:
                f = True
                break
        if f is True:
            break
        for i in range(y1):
            y -= 1
            n2 += 1
            print(x, y)
            if n2 == n:
                f = True
                break
        if f is True:
            break
    if x1 % 2 != 0 and y1 % 2 != 0:
        pozitiv = False
        print("helo")
    else:
        pozitiv = True
    x1 += 1
    y1 += 1

print(x, y)














print("Adja meg a háromszög 3 oldalának a hosszát:")

a = int(input("a oldal: "))
b = int(input("b oldal: "))
c = int(input("c oldal: "))

if a + b >= c and a + c >= b and c + b >= a:
    print("A(z)", a, b, c, "oldalú háromszög szerkeszthető.")
else:
    print("A(z)", a, b, c, "oldalú háromszög NEM szerkeszthető.")


























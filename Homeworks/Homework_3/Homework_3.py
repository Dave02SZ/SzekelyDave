print("Adja meg a háromszög három oldalát cm-ben: ")

a = int(input("a oldal (cm):"))
b = int(input("b oldal (cm):"))
c = int(input("c oldal (cm):"))

if a >= b and a >= c:
    if a <= c+b:
        print(f"A {a}, {b} és {c} háromszög szerkeszthető.")
    else:
        print(f"A {a}, {b} és {c} háromszög nem szerkeszthető.")

elif c >= b and c >= a:
    if c <= a+b:
        print(f"A {a}, {b} és {c} háromszög szerkeszthető.")
    else:
        print(f"A {a}, {b} és {c} háromszög nem szerkeszthető.")

else:
    if b <= a+c:
        print(f"A {a}, {b} és {c} háromszög szerkeszthető.")
    else:
        print(f"A {a}, {b} és {c} háromszög nem szerkeszthető.")












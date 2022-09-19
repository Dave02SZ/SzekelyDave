###### 1. házi ######

#1. feladat

mondat = input("Írjon be egy mondatot: ")
karakterek = {}

for i in mondat:
    if i not in karakterek.keys():
        k = mondat.count(i)
        karakterek[i] = k

print("Betük gyakorisága: ", karakterek)
print("Fordítva: ", mondat[::-1])

#2. feladat

print("Adjon be egy értéket és egy mértékegységet(cm/inch): ")

tav = float(input())
mertek = input()

if mertek == "cm":
    print("A megadott érték inchben:", tav / 2.54)
elif mertek == "inch":
    print("A megadott érték centiméterben:", tav * 2.54)
else:
    print("Not correct unit!")

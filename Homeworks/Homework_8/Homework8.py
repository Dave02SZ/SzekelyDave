x_valtozo = int(input("Írj be egy számot: "))
y_valtozo = int(input("Írj be egy számot: "))


for i in range(y_valtozo):
    s = str(i)
    if len(s) == 1:
        print("  ", i+1, end="")
    else:
        print(i+1, end="  ")

k = 4*y_valtozo*"-"
print()
print(f" :{k}--")

x = 1
while x <= x_valtozo:
    row = ""
    y = 1
    while y <= y_valtozo:
        row += format(x*y, '>4')
        y += 1

    print(f"{x}:", "", row)
    x += 1


s = 12345
s2 = str(s)

print(len(s2))

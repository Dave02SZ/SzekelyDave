import random

# 1. feladat

def beolvas():
    playlist = []
    f = open("playlist", "r", encoding="utf-8")

    for i in f:
        s = i.strip().split(";")
        zene = {
            "eloado": s[0],
            "cim": s[1],
            "mufaj": s[2],
            "hossz": int(s[3])
        }
        playlist.append(zene)
    f.close()
    return playlist


# 2. feladat

def teljes_hossz(playlist):
    h = 0
    for i in playlist:
        h += playlist[3]["hossz"]
    m = str(h // 60)
    sec = str(h % 60)
    s = ("Az összes lejátszott idő (perc:mperc): " + m + ":" + sec)
    return s


f2 = open("02_hossz.txt", "w", encoding="utf-8")
f2.write(teljes_hossz(beolvas()))
f2.close()


teljes_hossz(beolvas())

# 3. feladat


def leghosszabb_rockzene(playlist):
    rockzenek = []
    for i in playlist:
        if i["mufaj"] == "rock":
            rockzenek.append(i)
    n = rockzenek[0]
    for i in rockzenek:
        if i["hossz"] > n["hossz"]:
            n = i
    f3 = open("03_leghosszabb_rock.txt", "w", encoding="utf-8")
    f3.write(n["cim"] + " a leghosszabb zene.")
    f3.close()


leghosszabb_rockzene(beolvas())

# 4. feladat


def leggyakoribb_mufaj(playlist):
    mufajok = []
    kedvenc = ""
    for i in playlist:
        if i["mufaj"] not in mufajok:
            mufajok.append(i["mufaj"])
    elofordulas = []
    for i in mufajok:
        s = 0
        for j in playlist:
            if j["mufaj"] == i:
                s += 1
        elofordulas.append(s)
    k = max(elofordulas)
    for i in range(len(elofordulas)):
        if elofordulas[i] == k:
            kedvenc = mufajok[i]
    f4 = open("04_kedvenc_mufaj.txt", "w", encoding="utf-8")
    f4.write(kedvenc)
    f4.close()


leggyakoribb_mufaj(beolvas())
# 5. feladat


def zeneket_csoportosit(playlist):
    eloadok = []
    for i in playlist:
        if i["eloado"] not in eloadok:
            eloadok.append(i["eloado"])
    eloadok = sorted(eloadok)
    ossz = []
    for i in eloadok:
        o = 0
        for j in playlist:
            if i == j["eloado"]:
                o += j["hossz"]
        ossz.append(o)

    f5 = open("05_osszegzes.txt", "w", encoding="utf-8")
    for i in range(len(ossz)):
        s = str(ossz[i])
        f5.write(eloadok[i] + " : " + s + "\n")
    f5.close()


zeneket_csoportosit(beolvas())

# 6. feladat


def zeneket_listaz(playlist, eloadonev):
    v = ""
    k = False
    c = 0
    for i in playlist:
        if eloadonev.upper() == i["eloado"].upper():
            v = i["eloado"]
            k = True
    if not k:
        print("Nincs ilyen eloado a lejatszasi listaban!")

    v2 = v.lower().replace(" ", "_")
    f6 = open(f"06_{v2}_dalok.txt", "w", encoding="utf-8")
    for i in playlist:
        if i["eloado"] == v:
            f6.write(i["cim"] + ";" + i["mufaj"] + ";" + str(i["hossz"]) + "\n")
    f6.close()


# eloadoneve = input("Írja be az előadó nevét: ")
zeneket_listaz(beolvas(), "imagine dragons")

#7. feladat


def zeneket_torol(playlist, randnevek):
    f7 = open("07_torolt.txt", "w", encoding="utf-8")
    for i in playlist:
        if i["eloado"] not in randnevek:
            f7.write("Előadó: " + i["eloado"] + " ; " + "Cím: " + i["cim"] + " ; " + "Műfaj: " + i["mufaj"] + " ; " +
                     "A dal hossza: " + str(i["hossz"]) + "\n")
    f7.close()


lista = beolvas()
nevek = []

for i in lista:
    if i["eloado"] not in nevek:
        nevek.append(i["eloado"])

rand_szam = random.randint(1, len(nevek)-1)

randnevek = random.sample(nevek, rand_szam)

# print(len(nevek))
# print(randnevek)
# print(len(randnevek))
zeneket_torol(beolvas(), randnevek)




















class Csopi:
    def __init__(self, nev, projekt, szerepkor):
        self.nev = nev
        self.projekt = projekt
        self.szerepkor = szerepkor
        print("-- Developer létrehozva. --")
        print(f"{nev} a {projekt}-en dolgozik {szerepkor} szerepkörben")

    def __eq__(self, masik_dev):
        return self.projekt == masik_dev.projekt


def eggyut_dolgoznak(dev_team):
    for index_i, item_i in enumerate(dev_team):
        for index_j, item_j in enumerate(dev_team):
            if item_i.projekt == item_j.projekt and index_i < index_j:
                print(f"{item_i.nev} és {item_j.nev} dolgoznak egy projekten")
            pass


def main():

    Developer1 = Csopi("Ricsi", "SolArch", "Frontend")
    Developer2 = Csopi("Angela", "ZerTeng", "Tesztelő")
    Developer3 = Csopi("Peti", "KefERP", "Backend")
    Developer4 = Csopi("Sanyi", "ZerTeng", "Frontend")

    print()

    ubisoft = [Developer1, Developer2, Developer3, Developer4]
    eggyut_dolgoznak(ubisoft)

    
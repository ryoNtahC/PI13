import datetime
import random

class Osoba:
    # toto je konstruktor to innit
    def __init__(self, meno, priezvisko, rok):
        self.meno = meno
        self.priezvisko = priezvisko
        self.rok = rok
        self.vek = datetime.date.today().year - self.rok

        # toto je metoda pozdrav
    def pozdrav(self):
        print("Ahoj, ja som", self.meno, self.priezvisko, "a mám", self.vek, "rokov.")

    def vypis_vek(self):
        print(self.vek)

class Ucitel(Osoba):
    def __init__(self, meno, priezvisko, rok, titul, predmet, trieda):
        Osoba.__init__(self, meno, priezvisko, rok)
        self.titul = titul
        self.predmet = predmet
        self.trieda = trieda

    def pozdrav(self):
        print("Dobrý ďeň, som učiteľ",self.titul, self.meno, self.priezvisko, "a mám", self.vek, "rokov, učím predmet", self.predmet, "a som triedny", self.trieda)

class Student(Osoba):
    def __init__(self, meno, priezvisko, rok, trieda):
        Osoba.__init__(self, meno, priezvisko, rok)
        self.trieda = trieda

    def pozdrav(self):
        print("Dobrý ďeň, som študent", self.meno, self.priezvisko, "a mám", self.vek, "rokov a som žiakom triedy", self.trieda)


pocet_studentov = 10
pocet_ucitelov = 5

studenti = list()
for i in range(pocet_studentov):
    with open("mena.txt", "r", encoding="utf-8") as t:
        mena = tuple(t)
    meno = random.choice(mena)
    meno = meno[:-1]

    with open("priezviska.txt", "r", encoding="utf-8") as p:
        priezviska = tuple(p)
    priezvisko = random.choice(priezviska)
    priezvisko = priezvisko[:-1]

    rok = random.randint(2005,2008)
    if rok == 2005:
        trieda = "IV."
    elif rok == 2006:
        trieda = "III."
    elif rok == 2007:
        trieda = "II."
    else:
        trieda = "I."

    trieda = trieda + random.choice(("A", "B", "C"))

    studenti.append(Student(meno,priezvisko, rok, trieda))
print("Študenti:")
for i in range(pocet_studentov):
    print(i, studenti[i].meno, studenti[i].priezvisko, studenti[i].vek, studenti[i].rok, studenti[i].trieda)
studenti[1].pozdrav()

print("==============================\n")

ucitelia = list()
for i in range(pocet_ucitelov):
    with open("mena.txt", "r", encoding="utf-8") as t:
        mena = tuple(t)
    meno = random.choice(mena)
    meno = meno[:-1]

    with open("priezviska.txt", "r", encoding="utf-8") as p:
        priezviska = tuple(p)
    priezvisko = random.choice(priezviska)
    priezvisko = priezvisko[:-1]

    rok = random.randint(1960,2004)

    trieda = random.choice(("IV.","III.","II.","I."))

    trieda = trieda + random.choice(("A", "B", "C"))

    titul = random.choice(("Ing.","Mgr.","PhDr."))

    predmet = random.choice(("Programovanie","Telesná Výchova", "Matematika"))

    ucitelia.append(Ucitel(meno,priezvisko, rok, titul, predmet, trieda))
print("Učitelia:")
for i in range(pocet_ucitelov):
    print(i, ucitelia[i].meno, ucitelia[i].priezvisko, ucitelia[i].vek, ucitelia[i].rok,ucitelia[i].titul,ucitelia[i].predmet ,ucitelia[i].trieda)
ucitelia[1].pozdrav()

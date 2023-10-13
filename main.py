import datetime

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
    def __init__(self, meno, priezvisko, rok, titul, predmet):
        Osoba.__init__(self, meno, priezvisko, rok)
        self.titul = titul
        self.predmet = predmet

    def pozdrav(self):
        print("Dobrý ďeň, som učiteľ",self.titul, self.meno, self.priezvisko, "a mám", self.vek, "rokov a učím predmet", self.predmet)


jano = Osoba("Ján", "Jablko", 2004)
jano.pozdrav()
jozo = Ucitel("Jozef", "Hruška", 1995, "Ing.", "Programovanie")
jozo.pozdrav()

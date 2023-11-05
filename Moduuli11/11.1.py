class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f'Nimi: {self.nimi}')


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'Kirjoittaja: {self.kirjoittaja}')
        print(f'Sivumäärä: {self.sivumaara}')


class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'Päätoimittaja: {self.paatoimittaja}')


def main():
    aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
    hytti_no_6 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

    print("Tiedot Aku Ankka lehdestä:")
    aku_ankka.tulosta_tiedot()
    print("\nTiedot Hytti n:o 6 kirjasta:")
    hytti_no_6.tulosta_tiedot()


if __name__ == "__main__":
    main()

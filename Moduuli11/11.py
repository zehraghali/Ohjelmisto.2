class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print("Julkaisun nimi:", self.nimi)


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print("Kirjoittaja:", self.kirjoittaja)
        print("Sivumäärä:", self.sivumaara)


class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print("Päätoimittaja:", self.paatoimittaja)


class Auto:
    def __init__(self, rekisterinumero, huippunopeus):
        self.rekisterinumero = rekisterinumero
        self.huippunopeus = huippunopeus
        self.matkamittari = 0

    def aja(self, tuntimaara):
        self.matkamittari += tuntimaara * self.huippunopeus


class Sahkoauto(Auto):
    def __init__(self, rekisterinumero, huippunopeus, akkukapasiteetti):
        super().__init__(rekisterinumero, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

    def aja(self, tuntimaara):
        super().aja(tuntimaara)
        print("Akkukapasiteetti:", self.akkukapasiteetti, "kWh")
        print("Matkamittari:", self.matkamittari, "km")


class Polttomoottoriauto(Auto):
    def __init__(self, rekisterinumero, huippunopeus, bensatankin_koko):
        super().__init__(rekisterinumero, huippunopeus)
        self.bensatankin_koko = bensatankin_koko
        self.bensatankki = bensatankin_koko

    def aja(self, tuntimaara):
        super().aja(tuntimaara)
        print("Bensatankin koko:", self.bensatankin_koko, "l")
        print("Bensaa kulunut:", (tuntimaara * self.huippunopeus * 0.07), "l")
        self.bensatankki -= tuntimaara * self.huippunopeus * 0.07
        print("Matkamittari:", self.matkamittari)
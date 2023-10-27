class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):
        uusi_nopeus = self.nopeus + nopeuden_muutos
        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus

    def __str__(self):
        return f"Rekisteritunnus: {self.rekisteritunnus}, Huippunopeus: {self.huippunopeus} km/h, Nopeus: {self.nopeus} km/h, Kuljettu matka: {self.kuljettu_matka} km"

if __name__ == "__main__":
    uusi_auto = Auto("ABC-123", 142)

    print("Uuden auton tiedot:")
    print(uusi_auto)

    uusi_auto.kiihdytä(30)
    print("Auton nopeus 30 km/h kiihdytyksen jälkeen:")
    print(uusi_auto)

    uusi_auto.kiihdytä(70)
    print("Auton nopeus 100 km/h kiihdytyksen jälkeen:")
    print(uusi_auto)

    uusi_auto.kiihdytä(50)
    print("Auton nopeus 150 km/h kiihdytyksen jälkeen:")
    print(uusi_auto)

    uusi_auto.kiihdytä(-200)
    print("Hätäjarrutus -200 km/h:")
    print(uusi_auto)

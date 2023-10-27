import random

class Auto:
    auto_laskuri = 0

    def __init__(self, huippunopeus):
        Auto.auto_laskuri += 1
        self.rekisteritunnus = f"ABC-{Auto.auto_laskuri}"
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

    def kulje(self, tuntimaara):
        matka = self.nopeus * tuntimaara
        self.kuljettu_matka += matka

    def __str__(self):
        return f"Rekisteritunnus: {self.rekisteritunnus}, Huippunopeus: {self.huippunopeus} km/h, Nopeus: {self.nopeus} km/h, Kuljettu matka: {self.kuljettu_matka} km"

if __name__ == "__main__":
    autot = [Auto(random.randint(100, 200)) for _ in range(10)]

    kilpailu_ohi = False
    tunti = 1

    while not kilpailu_ohi:
        for auto in autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdytä(nopeuden_muutos)
            auto.kulje(1)

            if auto.kuljettu_matka >= 10000:
                kilpailu_ohi = True
                break

        if tunti % 10 == 0 or kilpailu_ohi:
            print(f"Kilpailun kulun tunti {tunti}:")
            for auto in autot:
                print(auto)
            print()

        tunti += 1

    print("Kilpailu päättyi!")

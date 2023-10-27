import random

class Auto:
    def __init__(self, nimi, nopeus):
        self.nimi = nimi
        self.nopeus = nopeus
        self.kilometrit = 0

    def kulje(self):
        self.kilometrit += self.nopeus

    def __str__(self):
        return f"{self.nimi}: {self.kilometrit} km"

class Kilpailu:
    def __init__(self, nimi, pituus_km, autot):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-5, 5)  # Nopeuden muutos -5...5 km/h
            auto.nopeus += muutos
            auto.kulje()

    def tulosta_tilanne(self):
        print(f"{self.nimi} - Tilanne:")
        for auto in self.autot:
            print(auto)
        print()

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kilometrit >= self.pituus_km:
                return True
        return False

def luo_kilpailu():
    autot = [Auto(f"Auto-{i}", random.randint(80, 120)) for i in range(1, 11)]
    kilpailu = Kilpailu("Suuri romuralli", 8000, autot)
    return kilpailu

if __name__ == "__main":
    kilpailu = luo_kilpailu()
    tunti = 1

    while not kilpailu.kilpailu_ohi():
        kilpailu.tunti_kuluu()

        if tunti % 10 == 0:
            kilpailu.tulosta_tilanne()

        tunti += 1

    kilpailu.tulosta_tilanne()
    print("Kilpailu päättyi!")

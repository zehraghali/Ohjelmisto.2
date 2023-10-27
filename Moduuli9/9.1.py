class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def __str__(self):
        return f"Rekisteritunnus: {self.rekisteritunnus}, Huippunopeus: {self.huippunopeus} km/h, Nopeus: {self.nopeus} km/h, Kuljettu matka: {self.kuljettu_matka} km"

if __name__ == "__main__":
    uusi_auto = Auto("ABC-123", 142)

    print("Uuden auton tiedot:")
    print(uusi_auto)

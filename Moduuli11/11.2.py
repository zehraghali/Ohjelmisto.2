class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.matkamittari = 0

    def aja(self, tuntia):
        self.matkamittari += self.huippunopeus * tuntia

    def tulosta_matkamittari(self):
        print(f"Rekisteritunnus: {self.rekisteritunnus}")
        print(f"Matkamittari: {self.matkamittari} km")


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

    def tulosta_tiedot(self):
        super().tulosta_matkamittari()
        print(f"Akkukapasiteetti: {self.akkukapasiteetti} kWh")


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko

    def tulosta_tiedot(self):
        super().tulosta_matkamittari()
        print(f"Bensatankin koko: {self.bensatankin_koko} litraa")


def main():
    sähköauto = Sähköauto("ABC-15", 180, 52.5)
    polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

    sähköauto.aja(3)  # Aja sähköautoa 3 tuntia
    polttomoottoriauto.aja(3)  # Aja polttomoottoriautoa 3 tuntia

    print("Sähköauton tiedot:")
    sähköauto.tulosta_tiedot()

    print("\nPolttomoottoriauton tiedot:")
    polttomoottoriauto.tulosta_tiedot()


if __name__ == "__main__":
    main()

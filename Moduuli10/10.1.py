class Hissi:
    def __init__(self, alin_kerros, ylimm_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylimm_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros < self.alin_kerros:
            kohde_kerros = self.alin_kerros
        elif kohde_kerros > self.ylin_kerros:
            kohde_kerros = self.ylin_kerros

        while self.nykyinen_kerros > kohde_kerros:
            self.kerros_alas()
        while self.nykyinen_kerros < kohde_kerros:
            self.kerros_ylos()

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
        print(f"Hissi on kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
        print(f"Hissi on kerroksessa {self.nykyinen_kerros}")

if __name__ == "__main__":
    alin_kerros = 1
    ylimm_kerros = 10

    hissi = Hissi(alin_kerros, ylimm_kerros)

    kohde_kerros = 5
    hissi.siirry_kerrokseen(kohde_kerros)

    hissi.siirry_kerrokseen(alin_kerros)

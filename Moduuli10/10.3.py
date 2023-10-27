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

class Talo:
    def __init__(self, alin_kerros, ylimm_kerros, hissien_lukumaara):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylimm_kerros
        self.hissit = [Hissi(alin_kerros, ylimm_kerros) for _ in range(hissien_lukumaara)]

    def aja_hissia(self, hissin_numero, kohde_kerros):
        if 0 <= hissin_numero < len(self.hissit):
            self.hissit[hissin_numero].siirry_kerrokseen(kohde_kerros)

    def palohalytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin_kerros)

if __name__ == "__main__":
    alin_kerros = 1
    ylimm_kerros = 10
    hissien_lukumaara = 2

    talo = Talo(alin_kerros, ylimm_kerros, hissien_lukumaara)

    print("Palohälytys! Kaikki hissit pohjakerrokseen.")
    talo.palohalytys()

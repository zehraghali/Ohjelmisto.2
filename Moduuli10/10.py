class Hissi:
    def __init__(self, alin_kerros, ylimpia_kerros):
        self.kerros = alin_kerros
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylimpia_kerros

    def siirry_kerrokseen(self, kohde_kerros):
        while self.kerros != kohde_kerros:
            if self.kerros < kohde_kerros:
                self.kerros_ylos()
            else:
                self.kerros_alas()

    def kerros_ylos(self):
        if self.kerros < self.ylin_kerros:
            self.kerros += 1
            print("Hissi on kerroksessa", self.kerros)

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
            print("Hissi on kerroksessa", self.kerros)


class Talo:
    def __init__(self, alin_kerros, ylimpia_kerros, hissien_lukumaara):
        self.hissit = []
        for i in range(hissien_lukumaara):
            self.hissit.append(Hissi(alin_kerros, ylimpia_kerros))

    def aja_hissia(self, hissin_numero, kohde_kerros):
        hissi = self.hissit[hissin_numero - 1]
        hissi.siirry_kerrokseen(kohde_kerros)

    def palohalytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin_kerros)


class Kilpailu:
    def __init__(self, nimi, pituus, autolista):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autolista

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.arvo_nopeuden_muutos()
            auto.kulje()

    def tulosta_tilanne(self):
        print("{:<10} {:<10} {:<10}".format("Auto", "Matka (km)", "Nopeus (km/h)"))
        for auto in self.autot:
            print("{:<10} {:<10} {:<10}".format(auto.nimi, auto.matka, auto.nopeus))

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus:
                return True
        return False
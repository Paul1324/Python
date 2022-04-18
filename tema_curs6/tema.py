class Fractie:

    def __init__(self,numarator,numitor):
        self.numarator = numarator
        self.numitor = numitor

    def __str__(self):
        return f"{self.numarator}/{self.numitor}"

    def __add__(self, frac):
        numitor = self.numitor * frac.numitor
        numarator = self.numarator*frac.numitor +self.numitor*frac.numarator
        return f"{numarator}/{numitor}"

    def __sub__(self, frac):
        numitor = self.numitor * frac.numitor
        numarator = self.numarator * frac.numitor - self.numitor * frac.numarator
        return Fractie(numarator, numitor)

    def inverse(self):
        aux = Fractie(numarator=self.numitor, numitor=self.numarator)
        return aux


frac1 = Fractie(1, 2)

print(frac1)

frac2 = Fractie(2, 3)

print(frac1+frac2)

print(frac1-frac2)

print(frac1.inverse())

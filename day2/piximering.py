import math
import random
import dataclasses

@dataclasses.dataclass
class Koordinat:
    x: float
    y: float

    @classmethod
    def slumpa(cls):
        def tal_mellan_minus_ett_och_ett() -> float:
            return random.random() * 2 - 1
        return cls(tal_mellan_minus_ett_och_ett(), tal_mellan_minus_ett_och_ett())

def i_cirkel(koord):
    return math.sqrt(koord.x**2 + koord.y**2) < 1

@dataclasses.dataclass
class UtanOchInnan:
    utan: int = 0
    innan: int = 0

    def lagg_till_koordinat(self, koord):
        if i_cirkel(koord):
            self.innan += 1
        else:
            self.utan += 1

def approximera_pi(uoi: UtanOchInnan) -> float:
    return uoi.innan / (uoi.innan + uoi.utan) * 4

uoi = UtanOchInnan()
i = 1
while True:
    koord = Koordinat.slumpa()
    uoi.lagg_till_koordinat(koord)
    loggad = math.log10(i)
    islog = loggad == int(loggad)
    if islog:
        approximerad_pi = approximera_pi(uoi)
        print(i, approximerad_pi, abs(math.pi - approximerad_pi))
    i += 1

class MojaKlasa:
    c = 10


print(hasattr(MojaKlasa, "a"))
print(setattr(MojaKlasa, "a", 10))
print(hasattr(MojaKlasa, "a"))
print(getattr(MojaKlasa, "a"))


MojaKlasa.b = 15

print(getattr(MojaKlasa, "b"))

x = MojaKlasa()
print(x.c)
print(x.a)

print(dir(x))
x2 = MojaKlasa()
x2.b = 66
MojaKlasa.b = 77

print(x.b, x2.b)


class Osoba:
    nazwa_gatunkowa = "Homo sapiens"  # atr klasowy

    def __init__(self, imie, rok_ur):
        self.imie = imie  # atr. instancji
        self.rok_ur = rok_ur

    @property
    def wiek(self):
        return 2023 - self.rok_ur

    @wiek.setter
    def wiek(self, x):
        self.rok_ur = 2023 - x


os = Osoba("Konrad", 1976)
os.imie = "Jacek"
print(os.wiek)
os.wiek = 110
print(os.rok_ur)


def przedstaw_sie(self):
    print(f"Jestem {self.imie}")


def przedstaw_sie_oficjalnie(self):
    print(f"Dzien dobory!. Nazywam sie {self.imie}")


x = 115

if x > 10:
    # oficjalne
    setattr(Osoba, "xxx", przedstaw_sie_oficjalnie)
else:
    # nieoficjalne
    setattr(Osoba, "xxx", przedstaw_sie)

os.xxx()

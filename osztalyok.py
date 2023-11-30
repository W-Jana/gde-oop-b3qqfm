from abc import ABC, abstractmethod

# Wisztercill János Márk - B3QQFM
class Szoba(ABC):
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

    @abstractmethod
    def info(self):
        print(f"{self.szobaszam}-s szoba, ára: {self.ar}")


class EgyagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam, klima):
        super().__init__(ar, szobaszam)
        self.klima = klima

    def info(self):
        print(f"{self.szobaszam}-s szoba, ára: {self.ar}, klíma: {'igen' if self.klima else 'nem'}")


class KetagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam, erkely):
        super().__init__(ar, szobaszam)
        self.erkely = erkely

    def info(self):
        print(f"{self.szobaszam}-s szoba, ára: {self.ar}, erkély: {'igen' if self.erkely else 'nem'}")


class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def keres_szoba(self, szobaszam):
        for szoba in self.szobak:
            if (szoba.szobaszam == szobaszam):
                return szoba
        else:
            print("Nincs ilyen szobaszámú szoba a hotelben")
            raise ValueError("Rossz szobaszám")

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def add_foglalas(self, foglalas):
        self.foglalasok.append(foglalas)

    def listaz_foglalas(self):
        print(f"{self.nev} szálloda foglalasai:\n")
        for foglalas in self.foglalasok:
            foglalas.info()

    def foglalas(self, szoba, datum):
        if szoba in self.szobak:
            foglalas = Foglalas(szoba, datum)
            if foglalas not in self.foglalasok:
                self.add_foglalas(foglalas)
                return szoba.ar
            else:
                print("Az adott napon a kiválasztott szoba már le van foglalva.")
        else:
            print("A megadott szoba nem található a szállodában.")
            raise ValueError("Rossz szobaszám")

    def foglalas_lemondas(self, szoba, datum):
        for foglalas in self.foglalasok:
            if szoba.szobaszam == foglalas.szoba.szobaszam and datum == foglalas.datum:
                self.foglalasok.remove(foglalas)
                print(f"A {szoba.szobaszam}-s szoba foglalása a {datum.strftime('%Y-%m-%d')} napra sikeresen lemondva.")
                break
        else:
            print("A lemondani kívánt foglalás nem létezik.")
            raise ValueError("Nem létező foglalás")


class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

    def info(self):
        self.szoba.info()
        print(f"Dátum: {self.datum.strftime('%Y-%m-%d')} \n")

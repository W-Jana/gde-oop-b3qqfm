from datetime import datetime
from osztalyok import Szalloda, EgyagyasSzoba, KetagyasSzoba, Foglalas

# Wisztercill János Márk - B3QQFM
hotel = Szalloda("Hotel OOP")

egyagyas1 = EgyagyasSzoba(20000, 1, True)
egyagyas2 = EgyagyasSzoba(15000, 2, False)
ketagyas1 = KetagyasSzoba(30000, 3, True)

hotel.add_szoba(egyagyas1)
hotel.add_szoba(egyagyas2)
hotel.add_szoba(ketagyas1)

hotel.add_foglalas(Foglalas(egyagyas1, datetime(2023, 12, 25)))
hotel.add_foglalas(Foglalas(egyagyas1, datetime(2023, 12, 26)))
hotel.add_foglalas(Foglalas(ketagyas1, datetime(2023, 12, 25)))
hotel.add_foglalas(Foglalas(ketagyas1, datetime(2023, 12, 31)))
hotel.add_foglalas(Foglalas(egyagyas2, datetime(2023, 12, 27)))

while True:
    print("\nVálassz egy műveletet:")
    print("1. Foglalások listázása")
    print("2. Foglalás")
    print("3. Lemondás")
    print("4. Kilépés")

    valasztas = input("Kérem adja meg melyik menüpontot kívánja választani: ")

    if valasztas == "1":
        hotel.listaz_foglalas()
    elif valasztas == "2":
        szobaszam = int(input("Add meg a szobaszámot: "))

        try:
            szoba = hotel.keres_szoba(szobaszam)
        except ValueError:
            continue

        datum_str = input("Add meg a foglalás dátumát (YYYY-MM-DD): ")
        try:
            datum = datetime.strptime(datum_str, "%Y-%m-%d")
        except ValueError:
            print("Érvénytelen dátumformátum. Kérem YYYY-MM-DD formátumban adja meg a dátumot.")
            continue

        if datetime.now() < datum:
            ar = hotel.foglalas(szoba, datum)
            print(f"A(z) {szoba.szobaszam}-s számú szoba foglalása sikeres volt a {datum.strftime('%Y-%m-%d')} napra. Ára: {ar} Ft")
        else:
            print("Érvénytelen dátum. Kérem a jövőbeni dátumot válasszon.")
    elif valasztas == "3":
        szobaszam = int(input("Add meg a szobaszámot: "))

        try:
            szoba = hotel.keres_szoba(szobaszam)
        except ValueError:
            continue

        datum_str = input("Add meg a foglalás dátumát (YYYY-MM-DD): ")
        try:
            datum = datetime.strptime(datum_str, "%Y-%m-%d")
        except ValueError:
            print("Érvénytelen dátumformátum. Kérem YYYY-MM-DD formátumban adja meg a dátumot.")
            continue

        try:
            hotel.foglalas_lemondas(szoba, datum)
        except ValueError:
            continue

    elif valasztas == "4":
        print("Kilépés...")
        break
    else:
        print("Érvénytelen választás. Kérlek, válassz újra.")

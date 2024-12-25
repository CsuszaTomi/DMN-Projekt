#------------FÜGGVÉNYEK------------#
#dizájn elemek
def kiemeléshatár():
    print("=" * 40)
def kiemelés(szoveg):
    kiemeléshatár()
    print(f"{szoveg.center(40)}")
    kiemeléshatár()
#Bejelentkezés ellenőrzés
def bejelentkezes(felhasznalonev, jelszo):
    for bejelenkezes in bejelentkezések:
        if bejelenkezes['Felhasználónév'] == felhasznalonev and bejelenkezes['Jelszó'] == jelszo:
            return True
    return False

#------------FŐKÓD------------#
#Lista amibe a bejelentkezéseket tároljuk a fájlból kiszedés után
bejelentkezések = []
#Fájl megnyitása
with open('bejeletkezések.txt') as bemenet:
    for sor in bemenet:
        adatok = sor.strip().split(';')
        bejelenkezes = {'Felhasználónév': adatok[0], 'Jelszó': adatok[1]}
        bejelentkezések.append(bejelenkezes)
kiemelés("Üdvözlünk a rendszerben!")
felhasznalonev = input("\nAdja meg a felhasználónevét: ")
jelszo = input("Adja meg a jelszavát: ")
siker = 0
if bejelentkezes(felhasznalonev, jelszo):
    kiemelés("Sikeres bejelentkezés!")
    siker = 1
else:
    kiemelés("Hibás felhasználónév vagy jelszó.")
    siker = 0
if siker == 1:
    kiemelés("Főmenü")
    kerdes = input("Mit szeretnél csinálni?\nRegisztrálni (r)\nBejegyzésteket kezelni (b)\nVálasztás: ")
    #Regisztráció
    if kerdes == "r":
        kiemelés("Regisztráció")
        felhasznaloreg = input("Add meg a felhasználó nevet: ")
        jelszoreg = input("Add meg a jelszót: ")
        with open("bejeletkezések.txt", 'a') as kimenet:
            regisztra = {'Felhasználónév': felhasznaloreg, 'Jelszó': jelszoreg}
            kimenet.write(f"{regisztra['Felhasználónév']};{regisztra['Jelszó']}\n")
        kiemelés("Sikeres regisztráció!")
    #Bejegyzések
    bejegyzeskezelőkerdes = 0
    kiemelés("Bejegyzés Kezelő")
    if kerdes == "b":
        bejegyzeskezelőkerdes = int(input("Mit szeretnél csinálni a bejegyzésekkel?\nÚjjat írni(1)\nTörölni(2)\nMódosítani(3)\nLezárni(4)\nVálasztás: "))
        #Bejegyzések írása
        if bejegyzeskezelőkerdes == 1:
            kiemelés("Bejegyzés írása")
            cim = input("Add meg a bejegyzés címét: ")
            leiras = input("Adj hozzá egy leírást: ")
            datum = input("Add meg a határidőt: ")
            with open('bejegyzesek.txt', 'a', encoding='utf-8') as bejegyzes:
                kiiras = {'Cím': cim, 'Leírás': leiras, 'Dátum': datum}
                bejegyzes.write(f"{kiiras['Cím']};{kiiras['Leírás']};{kiiras['Dátum']}\n")
            kiemelés("Bejegyzés mentve!")
        #Bejegyzések törlése
        elif bejegyzeskezelőkerdes == 2:
            kiemelés("Bejegyzés Törlő")
            bejegyzéseklista = []
            with open('bejegyzesek.txt', encoding="utf-8") as bemenet:
                for sor in bemenet:
                    bejegyzeselemek = sor.strip().split(';')
                    bejegyzesek = {'Cím': bejegyzeselemek[0], 'Leírás': bejegyzeselemek[1], 'Dátum': bejegyzeselemek[2]}
                    bejegyzéseklista.append(bejegyzesek)
            print("Bejegyzések(cím szerint):")
            for bejegyzesek in bejegyzéseklista:
                print(f"- {bejegyzesek['Cím']}")
            torleskerdes = input("Melyik bejegyzést szeretnéd törölni?\nVálasz: ")
            torlesilista = []
            for bejegyzesek in bejegyzéseklista:
                if bejegyzesek['Cím'] != torleskerdes:
                    torlesilista.append(bejegyzesek)
            if len(bejegyzéseklista) == len(torlesilista):
                print("Nem található ilyen cím a bejegyzések között.")
            else:
                with open('bejegyzesek.txt', 'w', encoding="utf-8") as kimenet:
                    for bejegyzesek in torlesilista:
                        kimenet.write(f"{bejegyzesek['Cím']};{bejegyzesek['Leírás']};{bejegyzesek['Dátum']}\n")
                print("A bejegyzés törölve.")
        #Bejegyzések módosítása
        elif bejegyzeskezelőkerdes == 3:
            kiemelés("Bejegyzés Módosító")
            bejegyzéseklista = []
            with open('bejegyzesek.txt', encoding="utf-8") as kimenet:
                for sor in kimenet:
                    bejegyzeselemek = sor.strip().split(';')
                    bejegyzesek = {'Cím': bejegyzeselemek[0], 'Leírás': bejegyzeselemek[1], 'Dátum': bejegyzeselemek[2]}
                    bejegyzéseklista.append(bejegyzesek)
            #Bejegyzés címek kíírása
            print("Bejegyzések(cím szerint):")
            for bejegyzesek in bejegyzéseklista:
                print(f"- {bejegyzesek['Cím']}")
            modositaskerdes = input("Melyik bejegyzést szeretnéd módosítani?\nVálasz: ")
            #Cím szerint kiválasztott bejegyzés módosítása
            for bejegyzesek in bejegyzéseklista:
                if bejegyzesek['Cím'] == modositaskerdes:
                    print(f"Címe: {bejegyzesek['Cím']}")
                    print(f"Leírása: {bejegyzesek['Leírás']}")
                    print(f"Dátuma: {bejegyzesek['Dátum']}")
                    #Ellenörzés hogy nem semmit adtunk meg és új érték megadás
                    ujcim = input(f"Add meg az új címet: ")
                    if ujcim.strip() == "":
                        ujcim = bejegyzesek['Cím']
                    bejegyzesek['Cím'] = ujcim
                    ujleiras = input(f"Add meg az új leírást: ")
                    if ujleiras.strip() == "":
                        ujleiras = bejegyzesek['Leírás']
                    bejegyzesek['Leírás'] = ujleiras
                    ujdatum = input(f"Add meg az új dátumot: ")
                    if ujdatum.strip() == "":
                        ujdatum = bejegyzesek['Dátum']
                    bejegyzesek['Dátum'] = ujdatum
            #Fájlba mentés
            with open('bejegyzesek.txt', 'w', encoding="utf-8") as kimenet:
                for bejegyzesek in bejegyzéseklista:
                    kimenet.write(f"{bejegyzesek['Cím']};{bejegyzesek['Leírás']};{bejegyzesek['Dátum']}\n")
            print("A bejegyzés módosítva.")
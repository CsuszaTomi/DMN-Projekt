#------------IMPORTOK------------#
import os
import datetime
import time

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
def regisztráció(felhasznalonev):
    for bejelenkezes in bejelentkezések:
        if bejelenkezes['Felhasználónév'] == felhasznalonev:
            return True
    return False
#terminál törlése
def terminaltorlo():
    os.system('cls' if os.name == 'nt' else 'clear')

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
    while True:
        kiemelés("Főmenü")
        kerdes = input("Mit szeretnél csinálni?\nRegisztrálni (1)\nBejegyzésteket kezelni (2)\nVálasztás: ")
        #Regisztráció
        if kerdes == "1":
            kiemelés("Regisztráció")
            bejelentkezések = []
            with open('bejeletkezések.txt') as bemenet:
                for sor in bemenet:
                    adatok = sor.strip().split(';')
                    bejelenkezes = {'Felhasználónév': adatok[0], 'Jelszó': adatok[1]}
                    bejelentkezések.append(bejelenkezes)
            felhasznaloreg = input("Add meg a felhasználó nevet: ")
            jelszoreg = input("Add meg a jelszót: ")
            if regisztráció(felhasznaloreg):
                kiemelés("Ez a felhasználónév már regisztrált!")
            elif regisztráció(felhasznaloreg) == False:
                with open("bejeletkezések.txt", 'a') as kimenet:
                    regisztra = {'Felhasználónév': felhasznaloreg, 'Jelszó': jelszoreg}
                    kimenet.write(f"{regisztra['Felhasználónév']};{regisztra['Jelszó']}\n")
                kiemelés("Sikeres regisztráció!")
            time.sleep(1)
        #Bejegyzések
        bejegyzeskezelőkerdes = 0
        if kerdes == "2":
            kiemelés("Bejegyzés Kezelő")
            bejegyzeskezelőkerdes = int(input("Mit szeretnél csinálni a bejegyzésekkel?\nÚjjat írni(1)\nTörölni(2)\nMódosítani(3)\nLezárni(4)\nListázni(5)\nVálasztás: "))
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
                time.sleep(1)
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
                    kiemelés("A bejegyzés törölve.")
                time.sleep(1)
            #Bejegyzések módosítása
            elif bejegyzeskezelőkerdes == 3:
                kiemelés("Bejegyzés Módosító")
                bejegyzéseklista = []
                with open('bejegyzesek.txt', encoding="utf-8") as kimenet:
                    for sor in kimenet:
                        bejegyzeselemek = sor.strip().split(';')
                        if len(bejegyzeselemek) == 4:
                            bejegyzesek = {'Cím': bejegyzeselemek[0], 'Leírás': bejegyzeselemek[1], 'Dátum': bejegyzeselemek[2], 'Lezárt': bejegyzeselemek[3]}
                        else:
                            bejegyzesek = {'Cím': bejegyzeselemek[0], 'Leírás': bejegyzeselemek[1], 'Dátum': bejegyzeselemek[2], 'Lezárt': 'Nem'}
                        bejegyzéseklista.append(bejegyzesek)
                #Bejegyzés címek kíírása
                print("Bejegyzések(cím szerint):")
                for bejegyzesek in bejegyzéseklista:
                    print(f"- {bejegyzesek['Cím']} (Lezárt: {bejegyzesek['Lezárt']})")
                modositaskerdes = input("Melyik bejegyzést szeretnéd módosítani?\nVálasz: ")
                #Cím szerint kiválasztott bejegyzés módosítása
                for bejegyzesek in bejegyzéseklista:
                    if bejegyzesek['Cím'] == modositaskerdes:
                        if bejegyzesek['Lezárt'] == 'Zárt':
                            print(f"{modositaskerdes} bejegyzés le van zárva, nem módosítható.")
                            break
                        else:
                            kiemelés(f"{modositaskerdes} módosítása")
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
                            print("A bejegyzés módosítva.")
                #Fájlba mentés
                with open('bejegyzesek.txt', 'w', encoding="utf-8") as kimenet:
                    for bejegyzesek in bejegyzéseklista:
                        kimenet.write(f"{bejegyzesek['Cím']};{bejegyzesek['Leírás']};{bejegyzesek['Dátum']};{bejegyzesek['Lezárt']}\n")
                time.sleep(1)
            #Bejegyzések lezárása módosítás ellen
            elif bejegyzeskezelőkerdes == 4:
                kiemelés("Bejegyzés Lezáró")
                bejegyzéseklista = []
                with open('bejegyzesek.txt', encoding="utf-8") as bemenet:
                    for sor in bemenet:
                        bejegyzeselemek = sor.strip().split(';')
                        if len(bejegyzeselemek) == 4:
                            bejegyzesek = {'Cím': bejegyzeselemek[0], 'Leírás': bejegyzeselemek[1], 'Dátum': bejegyzeselemek[2], 'Lezárt': bejegyzeselemek[3]}
                        else:
                            bejegyzesek = {'Cím': bejegyzeselemek[0], 'Leírás': bejegyzeselemek[1], 'Dátum': bejegyzeselemek[2], 'Lezárt': 'Nem'}
                        bejegyzéseklista.append(bejegyzesek)
                print("Bejegyzések (cím szerint):")
                for bejegyzesek in bejegyzéseklista:
                    print(f"- {bejegyzesek['Cím']} (Lezárt: {bejegyzesek['Lezárt']})")
                lazarokerdes = input("Melyik bejegyzést szeretnéd lezárni?\nVálasz: ")
                for bejegyzesek in bejegyzéseklista:
                    if bejegyzesek['Cím'] == lazarokerdes:
                        if bejegyzesek['Lezárt'] == 'Zárt':
                            print("Ez a bejegyzés már le van zárva!")
                        else:
                            bejegyzesek['Lezárt'] = 'Zárt'
                            print(f"{lazarokerdes} bejegyzés lezárva.")
                        break
                with open('bejegyzesek.txt', 'w', encoding="utf-8") as kimenet:
                    for bejegyzesek in bejegyzéseklista:
                        kimenet.write(f"{bejegyzesek['Cím']};{bejegyzesek['Leírás']};{bejegyzesek['Dátum']};{bejegyzesek['Lezárt']}\n")
                time.sleep(2)
            #Listázási lehetőségek
            elif bejegyzeskezelőkerdes == 5:
                kiemelés("Bejegyzés Listázó")
                bejegyzéseklista = []
                with open('bejegyzesek.txt', encoding="utf-8") as bemenet:
                    for sor in bemenet:
                        bejegyzeselemek = sor.strip().split(';')
                        if len(bejegyzeselemek) == 4:
                            bejegyzesek = {'Cím': bejegyzeselemek[0], 'Leírás': bejegyzeselemek[1], 'Dátum': bejegyzeselemek[2], 'Lezárt': bejegyzeselemek[3]}
                        else:
                            bejegyzesek = {'Cím': bejegyzeselemek[0], 'Leírás': bejegyzeselemek[1], 'Dátum': bejegyzeselemek[2], 'Lezárt': 'Nem'}
                        bejegyzéseklista.append(bejegyzesek)  
                listakerdes = int(input("Mi alapján szeretnéd listázni a bejegyzéseket?\n-Elvégzendő feladatok, hátralévő bejegyzések(1)\n-Aktuális hét feladatai, bejegyzései(2)\n-ABC sorrend szerint(3)\nVálasztás: ")) 
                if listakerdes == 1:
                    print("Hátralévő bejegyzések:")
                    for bejegyzesek in bejegyzéseklista:     
                        if bejegyzesek['Lezárt'] == "Nem":
                            print(f"- {bejegyzesek['Cím']} (Lezárt: {bejegyzesek['Lezárt']})")
                    time.sleep(2)
                if listakerdes == 2:
                    ma = datetime.date.today()
                    hetelsonapja = ma - datetime.timedelta(days=ma.weekday())  # hétfő
                    hetutolsonapja = hetelsonapja + datetime.timedelta(days=6)  # vasárnap
                    print("Aktuális hét feladatai, bejegyzései:")
                    for bejegyzesek in bejegyzéseklista:
                        bejegyzesdatum = datetime.datetime.strptime(bejegyzesek['Dátum'], '%Y.%m.%d').date()
                        if hetelsonapja <= bejegyzesdatum <= hetutolsonapja:
                            print(f"- {bejegyzesek['Cím']} (Dátum: {bejegyzesek['Dátum']})")
                    time.sleep(2)    
                elif listakerdes == 3:
                    print("Bejegyzések ABC sorrendben:")
                    rendezett_bejegyzesek = sorted(bejegyzéseklista, key=lambda x: x['Cím'])
                    for bejegyzes in rendezett_bejegyzesek:
                        print(f"- {bejegyzes['Cím']} (Lezárt: {bejegyzes['Lezárt']})")
                    time.sleep(2)    
        terminaltorlo()
        if kerdes == "":
            pass
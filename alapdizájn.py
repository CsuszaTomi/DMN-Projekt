#------------FÜGGVÉNYEK------------#
#dizájn elemek
def kiemeléshatár():
    print("=" * 40)
def kiemelés(message):
    kiemeléshatár()
    print(f"{message.center(40)}")
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
    kerdes = input("Mit szeretnél csinálni?\nRegisztrálni (r)\nBejegyzést írni (b)\nVálasztás: ")
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
    if kerdes == "b":
        kiemelés("Bejegyzés írása")
        uj_bejegyzes = input("Új bejegyzés létrehozása? (i/n): ")
        if uj_bejegyzes == "i":
            cim = input("Add meg a bejegyzés címét: ")
            leiras = input("Adj hozzá egy leírást: ")
            datum = input("Add meg a határidőt: ")
            with open('bejegyzesek.txt', 'a', encoding='utf-8') as bejegyzes:
                kiiras = {'Cím': cim, 'Leírás': leiras, 'Dátum': datum}
                bejegyzes.write(f"{kiiras['Cím']};{kiiras['Leírás']};{kiiras['Dátum']}\n")
            kiemelés("Bejegyzés mentve!")

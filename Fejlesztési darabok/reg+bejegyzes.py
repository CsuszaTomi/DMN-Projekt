#lista amibe a bejelentkezéseket tároljuk a fájlból kiszedés után
bejelentkezések = []
#fájl megnyitása
with open('bejeletkezések.txt') as bemenet:
    for sor in bemenet:
        adatok = sor.strip().split(';')
        bejelenkezes = {'Felhasználónév': adatok[0], 'Jelszó': adatok[1]}
        bejelentkezések.append(bejelenkezes)
#bejelentkezés ellenörzés
def bejelentkezes(felhasznalonev, jelszo):
    for bejelenkezes in bejelentkezések:
        if bejelenkezes['Felhasználónév'] == felhasznalonev and bejelenkezes['Jelszó'] == jelszo:
            return True
    return False
felhasznalonev = input("Adja meg a felhasználónevét: ")
jelszo = input("Adja meg a jelszavát: ")
siker = 0
if bejelentkezes(felhasznalonev, jelszo):
    print("Sikeres bejelentkezés!")
    siker = 1
else:
    print("Hibás felhasználónév vagy jelszó.")
    siker = 0
if siker == 1:
    kerdes = input("Mit szeretnél csinálni?\nRegisztrálni(r)\nBejegyzést írni(b)\n")
    #regisztráció
    if kerdes == "r":
        felhasznaloreg = input("Add meg a felhasználó nevet: ")
        jelszoreg = input("Add meg a jelszót: ")
        kimenet = open("bejeletkezések.txt",'a')
        regisztra = {'Felhasználónév': felhasznaloreg, 'Jelszó': jelszoreg}
        kimenet.write(f"\n{regisztra["Felhasználónév"]};{regisztra["Jelszó"]}\n")
        kimenet.close() 
    #bejegyzések
    if kerdes == "b":
        uj_bejegyzes  = input("Új bejegyzés létrehozása(i/n): ")
        if uj_bejegyzes == "i":
            cim = input("Add meg a bejegyzés címét: ")
            leiras = input("Adj hozzá egy leírást: ")
            datum = input("Add meg a meg határidőt: ")
            bejegyzes =  open('bejegyzesek.txt', 'a', encoding='utf-8')
            kiiras = {'Cím':cim,'Leírás':leiras,'Dátum':datum}
            bejegyzes.write(f"{kiiras["Cím"]};{kiiras["Leírás"]};{kiiras["Dátum"]}\n")
            bejegyzes.close()

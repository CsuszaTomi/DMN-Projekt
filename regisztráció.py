bejelentkezések = []
with open('bejeletkezések.txt') as bemenet:
    for sor in bemenet:
        adatok = sor.strip().split(';')
        bejelenkezes = {'Felhasználónév': adatok[0], 'Jelszó': adatok[1]}
        bejelentkezések.append(bejelenkezes)
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
    regisztracio = input("Szeretnél regisztrálni? ")
    if regisztracio == "igen" or "i":
        felhasznaloreg = input("Add meg a felhasználó nevet: ")
        jelszoreg = input("Add meg a jelszót: ")
        kimenet = open("bejeletkezések.txt",'a')
        regisztra = {'Felhasználónév': felhasznaloreg, 'Jelszó': jelszoreg}
        kimenet.write(f"\n{regisztra["Felhasználónév"]};{regisztra["Jelszó"]}\n")
        kimenet.close() 
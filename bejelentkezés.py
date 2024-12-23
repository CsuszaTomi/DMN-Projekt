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
if bejelentkezes(felhasznalonev, jelszo):
    print("Sikeres bejelentkezés!")
else:
    print("Hibás felhasználónév vagy jelszó.")
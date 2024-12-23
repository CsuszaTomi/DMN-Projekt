uj_bejegyzes  = input("Új bejegyzés létrehozása(i/n): ")
if uj_bejegyzes == "i":
    cim = input("Add meg a bejegyzés címét: ")
    leiras = input("Adj hozzá egy leírást: ")
    datum = input("Add meg a meg határidőt: ")
    bejegyzes =  open('bejegyzesek.txt', 'a', encoding='utf-8')
    kiiras = {'Cím':cim,'Leírás':leiras,'Dátum':datum}
    bejegyzes.write(f"{kiiras["Cím"]};{kiiras["Leírás"]};{kiiras["Dátum"]}\n")
    bejegyzes.close()

personen = [("Max", "01.01.2000"), ("Anna", 
"15.03.1998"), ("Tom", "10.07.2005")]

def aeltere_personen(personen):
    ergebnis = []
    for name, geburtstag in personen:
        jahr = int(geburtstag.split(".")[2])
        if jahr < 2000:
            ergebnis.append(name)
    return ergebnis

def neue_liste(personen):
    return [(geburtstag, name) for name, geburtstag in personen]

def doppelte_geschenke(personen):
    geburtstage = {}
    for name, geburtstag in personen:
        if geburtstag in geburtstage:
            geburtstage[geburtstag].append(name)
        else:
            geburtstage[geburtstag] = [name]
    return [geburtstag for geburtstag, namen in geburtstage.items() if len(namen) > 1]

aeltere_personen_ergebnis = aeltere_personen(personen)
neue_liste_ergebnis = neue_liste(personen)
doppelte_geschenke_ergebnis = doppelte_geschenke(personen)

print("Ältere Personen:", aeltere_personen_ergebnis)
print("Neue Liste:", neue_liste_ergebnis)
print("Doppelte Geburtstage:", doppelte_geschenke_ergebnis)
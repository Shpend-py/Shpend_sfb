# Liste von Tupeln, wobei jedes Tupel den Namen einer Person und ihren Geburtstag enthält
personen = [("Max", "01.01.2000"), ("Anna", "15.03.1998"), ("Tom", "10.07.2005"), ("Sara", "20.12.1995"), ("John", "15.03.1998")]

# Funktion, die die Namen der Personen zurückgibt, die vor dem Jahr 2000 geboren wurden
def aeltere_personen(personen):
    aeltere = []
    for name, geburtstag in personen:
        jahr = int(geburtstag.split(".")[2])
        if jahr < 2000:
            aeltere.append(name)
    return aeltere

# Funktion, die eine neue Liste von Tupeln zurückgibt, in der die Namen und Geburtstage der Personen vertauscht sind
def neue_liste(personen):
    neue_liste = [(geburtstag, name) for name, geburtstag in personen]
    return neue_liste

# Funktion, die prüft, ob es Personen mit demselben Geburtstag gibt und eine Liste der Geburtstage zurückgibt
def doppelte_geschenke(personen):
    geburtstags_dict = {}
    for name, geburtstag in personen:
        if geburtstag in geburtstags_dict:
            geburtstags_dict[geburtstag].append(name)
        else:
            geburtstags_dict[geburtstag] = [name]
    
    doppelte = [datum for datum, namen in geburtstags_dict.items() if len(namen) > 1]
    return doppelte

# Teste die Funktionen
print("Originale Liste der Personen:", personen)

# Teste die Funktion aeltere_personen(personen)
print("Personen, die vor dem Jahr 2000 geboren wurden:", aeltere_personen(personen))

# Teste die Funktion neue_liste(personen)
print("Liste mit vertauschten Tupeln:", neue_liste(personen))

# Teste die Funktion doppelte_geschenke(personen)
print("Geburtstage, an denen mehr als eine Person Geburtstag hat:", doppelte_geschenke(personen))

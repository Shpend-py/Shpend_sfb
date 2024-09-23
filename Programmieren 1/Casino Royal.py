# Eingabe der Adressinformationen
vorname = ("Bitte geben Sie Ihren Vornamen ein: ")
nachname = input("Bitte geben Sie Ihren Nachnamen ein: ")
strasse = input("Bitte geben Sie Ihre Straße ein: ")
nummer = input("Bitte geben Sie Ihre Hausnummer ein: ")
wohnort = input("Bitte geben Sie Ihren Wohnort ein: ")
 
# Ausgabe der formatierten Adressinformationen
print("\nIhre Adressangaben:")
print("Vorname: ", vorname)
print("Nachname: ", nachname)
print("Adresse: ", strasse, nummer)
print("Wohnort: ", wohnort)
 
 
# 2.1 Operator OR
bedingung_1 = True
bedingung_2 = False
 
ergebnis_or = bedingung_1 or bedingung_2
print("2.1 Ergebnis (Operator OR):", ergebnis_or)  # Ausgabe: True
 
# 2.2 Operator NOT
bedingung_1 = False
bedingung_2 = False
 
ergebnis_not = not bedingung_1 and not bedingung_2
print("2.2 Ergebnis (Operator NOT):", ergebnis_not)  # Ausgabe: True
 
# 2.3 Operator AND
bedingung_1 = True
bedingung_2 = False
 
ergebnis_and = bedingung_1 and bedingung_2
print("2.3 Ergebnis (Operator AND):", ergebnis_and)  # Ausgabe: False
 
 
import random
 
# Zufällige Zahl generieren
zufallszahl = random.randint(1, 15)
 
# Spielstart
print("Willkommen zum Zahlenraten-Spiel!")
 
# Schleife für das Spiel
while True:
    # Benutzereingabe abfragen
    benutzereingabe = input("Rate eine Zahl zwischen 1 und 15: ")
 
    # Prüfen, ob die Eingabe eine gültige Zahl ist
    if not benutzereingabe.isdigit():
        print("Bitte geben Sie eine ganze Zahl ein.")
        continue
 
    # Benutzereingabe in Integer umwandeln
    benutzereingabe = int(benutzereingabe)
 
    # Vergleichen der Eingabe mit der Zufallszahl
    if benutzereingabe == zufallszahl:
        print("Glückwunsch, Sie haben die Zahl getroffen!")
        break  # Das Spiel wird beendet, wenn die Zahl richtig geraten wurde
    else:
        print("Schade! War diesmal leider nichts! Probieren Sie es noch einmal.")
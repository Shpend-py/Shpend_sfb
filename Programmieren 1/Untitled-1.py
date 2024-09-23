import random


a = 3
b = 3

if a == b:
    print("Die Zahlen sind gleich")
else:
    print("Die Zahlen sind nicht gleich")
    
if a > b:
    print("a ist grösser als b")
else:
    print("b ist grösser als a")

if a % 2 == 0 and b % 2 == 0:
    print("Beide Zahlen sind gerade")
else:
    print("Mindestens eine der Zahlen ist ungerade")
    
if (a+b)>0:
    print("Beide Zahlen sind positiv")
else:
    print("Eine der beiden Zahlen ist mindestens negativ")

muenze = random.randint(1,2) #Random Zahl zwischen 1 und 10
if muenze == 1:
    print("Kopf")
else: 
    print("Zahl")
    
zahl1 = 13
zahl2 = 17

Summe = zahl1+zahl2
Differenz = zahl1-zahl2
Produkt = zahl1*zahl2
Quotient = zahl1/zahl2

print(f"Summe: {Summe}")
print(f"Summe: {Differenz}")
print(f"Summe: {Produkt}")
print(f"Summe: {Quotient}")

if zahl1 > zahl2:
    print("Zahl1 ist grösser als die Zahl2")
else:
    print("Die Zahl2 ist grösser als die Zahl1")

print(f"Modulo: {zahl1 % zahl2}")

Variable = zahl1**zahl2

#range(start, stop, step)
range(1,10)



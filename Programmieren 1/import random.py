import random

a = 2
b = 4
c = 6

if a == b and a > c:
    print("Die Zahlen sind gleich oder grösser c")
else:
    print("Die Zahlen sind nicht gleich oder a nicht grösser als c")

if c == a and a > b:
    print("a ist grösser als b und gleich c")
else:
    print("b ist grösser als a und a nicht gleich c")

#Verschiedene Suchergebnis
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
    
for tachorange in range(0, 100, 5):
  print(x)
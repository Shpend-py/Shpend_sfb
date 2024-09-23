import random

l = random.randint(1, 10) #Random Zahl zwischen 1 und 10
while True == l:
    benutzereingabe = input()
    
    try:
        zahl = int(benutzereingabe)
        print("Sie haben eine ganze Zahl eingegeben")
    except:
        print("Sie haben keine ganze Zahl eingegeben")
        
    if l == zahl:
        print("Sie haben gewonnen")
    else: 
        print("Sie haben ihre Altersvorsorge verspielt")
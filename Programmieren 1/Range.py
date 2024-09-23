for tachorange in range(0, 100, 5):
    tachorange1 = tachorange/1.6
    print(tachorange1, "mp/h are", tachorange, "km/h")
    
def KmhtoMph(mph):
    mph = kmh/1.6
    return mph

mph = KmhtoMph(30)
print(mph)

def MphtoKmh(kmh):
    kmh = mph/1.6
    return kmh

kmh = KmhtoMph(30)
print(kmh)

def parameterfunktion(param1=None, param2=None, param3=None):
    if param1 == None:
        param1 = "Standardwert für Param1"
    
    if param2 == None:
        param2 = 100
    
    if  param3 == None:
        param3 = [1,2,3]


    print(param1)
    print(param2)
    print(param3)

parameterfunktion(param1=12, param2=13, param3=14)



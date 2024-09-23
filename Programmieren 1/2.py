def typ_des_parameters(parameter):
    """
    Diese Funktion gibt den Typ des übergebenen Parameters zurück.
    
    :param parameter: Der Parameter, dessen Typ ermittelt werden soll.
    :return: Der Typ des Parameters.
    """
    return type(parameter)

# Testen der Funktion mit verschiedenen Datentypen
parameter_liste = [
    42,                             # int
    3.14,                           # float
    "Hallo, Welt!",                 # str
    True,                           # bool
    None,                           # NoneType
    [1, 2, 3],                      # list
    (4, 5, 6),                      # tuple
    {7, 8, 9},                      # set
    {"Schlüssel": "Wert"},          # dict
    b"bytes",                       # bytes
    bytearray(b"bytearray"),        # bytearray
    frozenset([10, 11, 12]),        # frozenset
    complex(1, 2)                   # complex
    ]

for parameter in parameter_liste:
    print(f"Der Typ des Parameters {parameter} ist: {typ_des_parameters(parameter)}")

"""   
Der Typ des Parameters 42 ist: <class 'int'>
Der Typ des Parameters 3.14 ist: <class 'float'>
Der Typ des Parameters Hallo, Welt! ist: <class 'str'>
Der Typ des Parameters True ist: <class 'bool'>
Der Typ des Parameters None ist: <class 'NoneType'>
Der Typ des Parameters [1, 2, 3] ist: <class 'list'>
Der Typ des Parameters (4, 5, 6) ist: <class 'tuple'>
Der Typ des Parameters {8, 9, 7} ist: <class 'set'>
Der Typ des Parameters {'Schlüssel': 'Wert'} ist: <class 'dict'>
Der Typ des Parameters b'bytes' ist: <class 'bytes'>
Der Typ des Parameters bytearray(b'bytearray') ist: <class 'bytearray'>
Der Typ des Parameters frozenset({10, 11, 12}) ist: <class 'frozenset'>
Der Typ des Parameters (1+2j) ist: <class 'complex'>
"""
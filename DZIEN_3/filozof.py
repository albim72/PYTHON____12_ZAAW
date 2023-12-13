odp = input("Czy Ziemia jest płaska? Czy chcesz znać odpowiedź? (t/n): ")
if odp.lower() == "t":
    required = True
else:
    required = False

def odpowiedz(self):
    return "Tak! Ziemia jest płaska!"

def brak(self):
    return "brak odpowiedzi..."

class SednoOdpowiedzi(type):
    def __init__(cls,clsname,bases,attrs):
        if required:
            cls.odpowiedz = odpowiedz
        else:
            cls.odpowiedz = brak

class Arystoteles(metaclass=SednoOdpowiedzi):
    pass

class Platon(metaclass=SednoOdpowiedzi):
    pass

class SwTomasz(metaclass=SednoOdpowiedzi):
    pass

class Kopernik(metaclass=SednoOdpowiedzi):
    pass

fill1 = Arystoteles()
print(f'Filozof {fill1.__class__.__name__} twierdzi: {fill1.odpowiedz()}')

fill2 = Platon()
print(f'Filozof {fill2.__class__.__name__} twierdzi: {fill2.odpowiedz()}')


fill3 = SwTomasz()
print(f'Filozof {fill3.__class__.__name__} twierdzi: {fill3.odpowiedz()}')


fill4 = Kopernik()
print(f'Filozof {fill4.__class__.__name__} twierdzi: {fill4.odpowiedz()}')

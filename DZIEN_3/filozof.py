odp = input("Czy Ziemia jest płaska? Czy chcesz znać odpowiedź? (t/n): ")
if odp.lower() == "t":
    required = True
else:
    required = False

def odpowiedz(self):
    return "Tak! Ziemia jest płaska!"

def odpowiedz_nowa(self):
    return "Nie! Ziemia jest elipsoidą!"

def brak(self):
    return "brak odpowiedzi..."

class SednoOdpowiedzi(type):
    def __init__(cls,clsname,bases,attrs):
        if required:
            if attrs.get('n'):
                cls.odpowiedz = odpowiedz_nowa
            else:
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
    # def odpowiedz(self):
    #     return "Nie i koniec!"
    n = True

class Einstein(metaclass=SednoOdpowiedzi):
    n = True

fill1 = Arystoteles()
print(f'Filozof {fill1.__class__.__name__} twierdzi: {fill1.odpowiedz()}')

fill2 = Platon()
print(f'Filozof {fill2.__class__.__name__} twierdzi: {fill2.odpowiedz()}')


fill3 = SwTomasz()
print(f'Filozof {fill3.__class__.__name__} twierdzi: {fill3.odpowiedz()}')


fill4 = Kopernik()
print(f'Filozof {fill4.__class__.__name__} twierdzi: {fill4.odpowiedz()}')


fill5 = Einstein()
print(f'Filozof {fill5.__class__.__name__} twierdzi: {fill5.odpowiedz()}')

#Skonstruuj rozwiązanie pozwalające Kopernikowi na wypowiedź: Nie! Ziemia jest elipsoidą!
#Pozostaw aktualną konstrukcję.
#Przebuduj metaklasę tak aby uwzględniała dowolnego nowego filozofa nowej ery...

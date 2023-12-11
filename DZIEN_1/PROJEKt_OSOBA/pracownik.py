from osoba import Osoba

class Pracownik(Osoba):
    def __init__(self, imie, wiek, waga, wzrost,firma,stanowisko,lata_pracy,wynagrodzenie):
        super().__init__(imie, wiek, waga, wzrost)
        self.firma = firma
        self.stanowisko = stanowisko
        self.lata_pracy = lata_pracy
        self.wynagrodzenie = wynagrodzenie
        self.kolor_oczu = "niebieskie"

    def __repr__(self):
        return super().__repr__() + (f"dane pracownika -> firma: {self.firma},"
                                     f"stanowisko: {self.stanowisko}, wynagrodzenie: {self.wynagrodzenie} zł")

    def czypracownik(self):
        return True
    
    
        
    

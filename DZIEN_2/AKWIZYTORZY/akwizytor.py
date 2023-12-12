from decimal import Decimal

class Akwizytor:
    """
    akwizytor - pracownik, którego wynagrodzenie jest wyłącznie prowizją od sprzedaży
    """
    
    def __init__(self,imie,nazwisko,nr_ubezpieczenia,sprzedaz,prowizja):
        self._imie = imie
        self._nazwisko = nazwisko
        self._nr_ubezpieczenia = nr_ubezpieczenia
        self.sprzedaz = sprzedaz
        self.prowizja = prowizja
        
    @property
    def imie(self):
        return self._imie
    
    @imie.setter
    def imie(self,noweimie):
        self._imie = noweimie

    @property
    def nazwisko(self):
        return self._nazwisko

    @nazwisko.setter
    def nazwisko(self, nowenazwisko):
        self._nazwisko = nowenazwisko

    @property
    def nr_ubezpieczenia(self):
        return self._nr_ubezpieczenia

    @nr_ubezpieczenia.setter
    def nr_ubezpieczenia(self, nowynr_ubezpieczenia):
        self._nr_ubezpieczenia = nowynr_ubezpieczenia
        
        
        
        

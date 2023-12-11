from funkcje.bfunkcje import *

class CDane:
    def __init__(self,lista,slownik):
        self.lista = lista
        self.slownik = slownik
        
    def czytaj_l(self):
        return czytaj_liste(self.lista)
    
    def czytaj_s(self):
        return czytaj_slownik(self.slownik)
        
    

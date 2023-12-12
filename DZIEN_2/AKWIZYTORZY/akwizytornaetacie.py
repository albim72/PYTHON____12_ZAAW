from akwizytor import Akwizytor
from decimal import Decimal

class AkwizytorNaEtacie(Akwizytor):
    """
        akwizytor - pracownik, którego wynagrodzenie jest sumą prowizji od sprzedaży oraz pensji
    """

    def __init__(self, imie, nazwisko, nr_ubezpieczenia, sprzedaz, prowizja, pensja):
        super().__init__(imie, nazwisko, nr_ubezpieczenia, sprzedaz, prowizja)
        self.pensja=pensja

    @property
    def pensja(self):
        return self._pensja

    @pensja.setter
    def pensja(self,kwota):
        if kwota <= Decimal('0.00'):
            raise ValueError('Wynagrodzenie ryczałtowe nie może być ujemne lub równe 0!')
        self._pensja = kwota

    def __repr__(self):
        return 'Etatowy: ' + super().__repr__() + f'\nryczałt:{self.pensja:.2f} zł'

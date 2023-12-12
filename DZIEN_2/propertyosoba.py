class Osoba:
    def __init__(self,imie,wiek,waga,wzrost):
        self.imie = imie
        self.wiek = wiek
        self.waga = waga
        self.wzrost = wzrost

    @property
    def waga(self):
        return self._waga

    @waga.setter
    def waga(self,nowawaga):
        self._waga = nowawaga


os1 = Osoba('Olaf',30,80,174)
print(os1.waga)

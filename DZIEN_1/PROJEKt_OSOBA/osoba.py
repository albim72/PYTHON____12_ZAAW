class Osoba:
    def __init__(self,imie,wiek,waga,wzrost):
        self.imie = imie
        self.wiek = wiek
        self.waga = waga
        self.wzrost = wzrost
        self.kolor_oczu = "brązowe"
        self.info()

    def __repr__(self):
        return (f'Reprezentacja tekstowa obiektu -> osoba {self.imie},'
                f'wiek: {self.wiek}, waga: {self.waga} kg, wzrost: {self.wzrost} cm,'
                f'kolor oczu: {self.kolor_oczu}')

    def info(self):
        print("Utworzno obiekt klasy Osoba...")

    def wiek_za_n_lat(self,n):
        return self.wiek + n

    def czypracownik(self):
        return False



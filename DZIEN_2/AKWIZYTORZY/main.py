from decimal import Decimal
from akwizytor import Akwizytor
from akwizytornaetacie import AkwizytorNaEtacie

class DuzaFirma:
    def __repr__(self):
        return "Właściciel firmy, otrzymuje wypłatę na podstawie zysków firmy z ubiegłego roku"

    def zarobek(self):
        return Decimal('10_000_000')


df = DuzaFirma()
s = Akwizytor('Jan','Kot',34567800,Decimal('514500'),Decimal('8.9'))
c = AkwizytorNaEtacie('Anna','Kowal',909348434,Decimal('488900'),Decimal('7.5'),Decimal('5600'))

pracownicy = [c,s,df]
for pr in pracownicy:
    print(pr)
    print(f'{pr.zarobek():,.2f} zł\n')

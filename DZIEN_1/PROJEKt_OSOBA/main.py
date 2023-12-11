from osoba import Osoba
from pracownik import Pracownik

os1 = Osoba("Jan",56,88,178)
os1.setoczy("niebieskie")
print(f"zmieniono kolor oczu na  :{os1.getoczy()} ")
print(os1)
n=12
print(f'wiek osoby za {n} lat -> {os1.wiek_za_n_lat(n)}')
print(f'czy osoba jest pracownikiem? ({os1.czypracownik()})')

print("_"*50)

pr1 = Pracownik("Karol",50,80,180,"ABC","dyrektor",12,11200)
pr1.setoczy("piwne")
print(pr1)
n=5
print(f'wiek pracownika za {n} lat -> {pr1.wiek_za_n_lat(n)}')
print(f'czy osoba jest pracownikiem? ({pr1.czypracownik()})')

from osoba import Osoba
from pracownik import Pracownik
from student import Student

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

print("_"*50)

s1 = Student("Olaf",22,77,177,63532,"informatyka stosowana", "informatyka",3)
print(s1)
n=3
print(f'wiek studenta za {n} lat -> {s1.wiek_za_n_lat(n)}')
print(f'czy osoba jest pracownikiem? ({s1.czypracownik()})')

print("_"*50)

s2 = Student("Olga",22,60,170,76757,"fizjoterapia", "fizjoterapia sportowa",
             3,"Medica","praktykant",1,3000)
print(s2)
n=3
print(f'wiek studenta za {n} lat -> {s2.wiek_za_n_lat(n)}')
print(f'czy osoba jest pracownikiem? ({s2.czypracownik()})')

print("_"*50)

s3 = Student("Paweł",23,88,190,4545546,"logistyka i transport",
             "transport",4,dyscyplina="kolarstwo górskie", lata_upr=5,best_wynik="70km, 2h i 10min")
print(s3)
n=3
print(f'wiek studenta za {n} lat -> {s3.wiek_za_n_lat(n)}')
print(f'czy osoba jest pracownikiem? ({s3.czypracownik()})')
print(s3.infosport())
print(f'bmi ciała wynosi: {s3.bmi():.2f} -> {s3.opis_bmi()}')



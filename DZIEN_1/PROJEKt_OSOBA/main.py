from osoba import Osoba

os1 = Osoba("Jan",56,88,178)
print(os1)
n=12
print(f'wiek osoby za {n} lat -> {os1.wiek_za_n_lat(n)}')
print(f'czy osoba jest pracownikiem? ({os1.czypracownik()})')

print("_"*50)

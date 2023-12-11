#import dane
# import dane as dn
from dane import nrfilii as filia
from dane import book as bk
from funkcje.bfunkcje import czytaj_liste as cl,czytaj_slownik as cs
from klasy.classdata import CDane

print("________________ wyświetlanie bezpośrednie _______________")
print(filia)
print(bk)

print("________________ wyświetlanie za pomocą funkcji _______________")
cl(filia)
cs(bk)

print("________________ wyświetlanie za pomocą obiektu _______________")
cd = CDane(filia,bk)
cd.czytaj_l()
cd.czytaj_s()

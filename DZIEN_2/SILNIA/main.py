#funkcja silnia: n!=1*2*3*...*n, dla n>=0
#max double: 1.8E+308
#n?? 171

import sys
from liczbujemna import UjemneN

sys.set_int_max_str_digits(0x10000000)
sys.setrecursionlimit(0x10000000)
def silnia(n):
    if n<0:
        raise UjemneN(n)
    wynik=1
    for i in range(1,n+1):
        wynik*=i
    return wynik

def silnia_rek(n):
    if n<0:
        raise UjemneN(n)
    if n==0:
        return 1
    else:
        return n*silnia_rek(n-1)

try:
    n = int(input("podaj wartość argumentu n funkcji silnia: "))
    wynik = silnia(n)
    wynik_r = silnia_rek(n)
    print(f'silnia z n={n} wynosi: {wynik}')
    print(f'silnia rekurencyjna z n={n} wynosi: {wynik_r}')
    print(f'typ wyniku: {type(wynik)}')
    print(f'typ wyniku rek: {type(wynik_r)}')
except UjemneN as un:
    print(un)
except ValueError as ve:
    print(ve)
except Exception as exc:
    print(exc)

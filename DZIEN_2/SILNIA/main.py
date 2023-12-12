#funkcja silnia: n!=1*2*3*...*n, dla n>=0
#max double: 1.8E+308
#n?? 171

import sys
from liczbujemna import UjemneN

sys.set_int_max_str_digits(0x10000000)
def silnia(n):
    if n<0:
        raise UjemneN(n)
    wynik=1
    for i in range(1,n+1):
        wynik*=i
    return wynik

try:
    n = int(input("podaj wartość argumentu n funkcji silnia: "))
    wynik = silnia(n)
    print(f'silnia z n={n} wynosi: {wynik}')
    print(f'typ wyniku: {type(wynik)}')
except UjemneN as un:
    print(un)
except ValueError as ve:
    print(ve)
except Exception as exc:
    print(exc)

liczby = (900,1001,-787,0,57,6,-7,56,5,4,12,-44,567,863,-345,-101,9,0,34,166,-234,127,890,-990,19,-4,87,1001)

def pokaz_statystyki(dane:list)->tuple:
    minimum:int = min(dane)
    maximum:int = max(dane)
    rozstep:int = maximum-minimum
    sr_arytm:float = sum(dane)/len(dane)
    return minimum,maximum,rozstep,sr_arytm

wynik = pokaz_statystyki(liczby)
print(type(wynik))
print(wynik)

mini,maxi,roz,artm = pokaz_statystyki(liczby)
print(f'wartość największa: {maxi},wartość najmniejsza: {mini}, rozstęp: {roz}, '
      f'średnia arytmetyczna: {artm}')

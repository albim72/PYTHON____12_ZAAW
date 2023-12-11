print("programowanie funkcyjne")

#przykład1
def witaj(imie)->str:
    return f'Miło Cię znowu widzieć {imie}'

def konkurs(imie,punkty,miejsce):
    return f'uczestnik konkursu {imie}, liczba punktów: {punkty}, miejsce: {miejsce}'

def bonus(punkty,bonus):
    if punkty > 50:
        return punkty + bonus
    else:
        return punkty

def osoba(funkcja,*args)->None:
    return funkcja(*args)

print(osoba(witaj,"Leon"))
print(osoba(konkurs,"Ola",78,5))
print(osoba(bonus,56,10))
print(osoba(bonus,33,10))

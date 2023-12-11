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

#przykład 2

def rejestracja(oplata):
    def lista(nr):
        return f"jesteś na liście zawodników {nr}. Opłacone."

    def brak():
        return "brak opłaty,uzupełnij w ciągu 3 dni."

    def error():
        return "błąd w opłacie lub rejestracji... powtórz"

    if oplata == 1:
        return lista
    elif oplata == 0:
        return brak
    else:
        return error

print(rejestracja(1)(45))
print(rejestracja(0)())
print(rejestracja(15)())

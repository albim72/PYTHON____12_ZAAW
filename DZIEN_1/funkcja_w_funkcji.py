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


#przykład 3
def startstop(funkcja):
    def wrapper(*args):
        print("*"*50)
        print("startowanie procesu....")
        funkcja(*args)
        print("zakończenie procesu...")
    return wrapper

def zawijanie(w_co):
    print(f'zawijanie czekoladek w {w_co}')

zw = startstop(zawijanie)
zw("sreberka")

@startstop
def dmuchanie(czego):
    print(f'dmuchanie {czego} na torcie urodzinowym.')


dmuchanie("świeczek")

@startstop
def fx(n):
    print(f'wynik = {2*n-1}')

fx(9)

#standardowe funkcje wyższego rzędu
liczby = [45,12,78,90,-23,0,34,56,78,111,-45,11,5,-3,100,-133,98,25,-4,4]

parzyste = list(filter(lambda x:x%2==0,liczby))
print(parzyste)

cube = list(map(lambda x:x**3,liczby))
print(cube)

#list comprhension
dane = [i**2 for i in range(120)]
print(dane)

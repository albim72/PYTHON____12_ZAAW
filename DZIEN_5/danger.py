import os

mojkod = '''
a=5
b=8
print(f'wynik={a*b}')
'''

print(mojkod)
exec(mojkod)

cd = input("czy chcesz coś napisać? -> pisz tutaj... ")
exec(cd)

print("___________________________________________")
def calculate_per(l):
    return 4*l

def calculate_area(l):
    return l**2

expr = input("podaj nazwę funkcji: ")

for l in range(10,50,10):
    if expr == 'calculate_per(l)':
        print(f'jeśli długość wynosi {l}, wartość obwodu działki = {eval(expr)}')
    elif expr == 'calculate_area(l)':
        print(f'jeśli długość wynosi {l}, wartość pola działki = {eval(expr)}')
    else:
        print('niewłaściwa funkcja')
        break

w = input('podaj wartość: ')
w = eval(w)
oblicz = w*5
print(oblicz)

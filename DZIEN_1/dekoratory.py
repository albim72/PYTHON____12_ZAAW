import time

def pomiarczasu(funkcja):
    def wrapper():
        starttime = time.time()
        funkcja()
        endtime = time.time()
        wynik = endtime-starttime
        print(f'czas wykonania funkcji: {wynik} s')
    return wrapper

def usypiacz(funkcja):
    def wrapper():
        time.sleep(3)
        return funkcja()
    return wrapper

@pomiarczasu
@usypiacz
def big_lista():
    sum([i**5 for i in range(10_000_000)])

big_lista()

#przypadek drugi
def debug(funkcja):
    def wrapper(*args):
        print(f'wołana funkcja to: {funkcja.__name__}')
        funkcja(*args)
    return wrapper

@debug
def info(i):
    print(f'kod: {i}')

info(9385893485)

#przypadek 4

def repeat(n):
    def wrapper(funkcja):
        def inner(*args):
            for i in range(n):
                funkcja(*args)
        return inner
    return wrapper


@repeat(n=5)
def policz(c,d):
    print(f'wynik = {c*d**2}')


policz(1,2)

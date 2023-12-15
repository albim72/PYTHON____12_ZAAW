import time
import concurrent.futures
from funkcja_prime import znajdz_sume_liczb_pierwszych

numbers = [(1,10_000),(3,50_000),(5_000,100_000),(4,900),(8_000,15_000),(95_000,133_000),(200,67_000)]

def synchronicznie():
    starttime = time.time()
    for pair in numbers:
        st= time.time()
        prime_suma = znajdz_sume_liczb_pierwszych(*pair)
        et = time.time()
        print(f'wynik = {prime_suma}, czas wykonania {et-st} s')
    endtime = time.time()

    print(f'całkowity czas wyznaczenia sum - synchronicznie: {endtime - starttime} s')

def run_heavy_function(params):
    return znajdz_sume_liczb_pierwszych(*params)

def asynchronicznie():
    starttime = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=8) as executor:
        wynik = executor.map(run_heavy_function,numbers)
    endtime = time.time()
    print(list(wynik))
    print(f'całkowity czas wyznaczenia sum - asynchronicznie: {endtime-starttime} s')

def main():
    synchronicznie()
    asynchronicznie()

if __name__ == '__main__':
    main()

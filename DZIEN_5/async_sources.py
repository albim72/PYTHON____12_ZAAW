import asyncio
import random

#funckja symulująca pobieranie danych
async def pobierz_dane(source):
    czas_oczekiwania = random.randint(1,5)
    await asyncio.sleep(czas_oczekiwania)
    return f'Dane z {source} po {czas_oczekiwania} s'

#główna funkcja, do pobierania danych
async def pobierz_dane_sources(sources):
    tasks =[pobierz_dane(source) for source in sources]
    wyniki = await asyncio.gather(*tasks)
    return wyniki

datasources = ['API_1','API_2','Baza_danych','XML','Strona_www']

async def main():
    wyniki = await pobierz_dane_sources(datasources)
    print('otrzymane wyniki')
    for wynik in wyniki:
        print(wynik)

asyncio.run(main())

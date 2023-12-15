import threading
import queue
import time

#funkcja do przetwarzania zadań
def przetwarzaj_zadania(nr_watku,kolejka_zadan):
    while True:
        zadanie = kolejka_zadan.get() #pobieranie zadania z kolejki
        if zadanie is None:
            break #zakoniczenie wątku  w pzypadku sygnału o zakończeniu pracy

        print(f'Wątek {nr_watku} przetwarza zadanie: {zadanie}')
        time.sleep(1)
        kolejka_zadan.task_done() #oznaczone jako wykonane

kolejka = queue.Queue()

liczba_watkow = 3

watki = []
for i in range(liczba_watkow):
    watek = threading.Thread(target=przetwarzaj_zadania,args=(i, kolejka))
    watek.start()
    watki.append(watek)

zadania = ['Zadanie A','Zadanie C','Zadanie C','Zadanie D','Zadanie E']

for zadanie in zadania:
    kolejka.put(zadanie)

kolejka.join()


#zamykamy wątki po wykonaniu pracy
for _ in range(liczba_watkow):
    kolejka.put(None)

for watek in watki:
    watek.join()

print("Wszystkie zadania zostały przetworzone.")

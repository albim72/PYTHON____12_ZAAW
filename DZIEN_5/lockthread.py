import threading

def worker(lock,shared_variable):
    lock.acquire()
    try:
        shared_variable += 1
        print(f'Wątek {threading.current_thread().name} zwiększył zmienną współdzieloną do {shared_variable}')
    finally:
        lock.release()


shared_variable = 0
lock = threading.Lock()
threads = []

for i in range(5):
    t = threading.Thread(target=worker,args=(lock,shared_variable))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f'Zmienna wspóldzielona po zakończeniu pracy wątków: {shared_variable}')

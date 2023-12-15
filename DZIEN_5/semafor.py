import threading
import time

semafor = threading.Semaphore(3)

def funkcja_watek(nr_watku):
    print(f'Wątek {nr_watku}  próbuje uzyskać dostęp')
    semafor.acquire()
    print(f'Wątek {nr_watku} uzyskał dostęp')
    time.sleep(3)
    semafor.release()
    print(f'Wątek {nr_watku} zwolnił zasób')

for i in range(5):
    threading.Thread(target=funkcja_watek,args=(i,)).start()

#!/usr/bin/python
# -*- config: utf-8 -*-

from multiprocessing import Process, Queue, cpu_count
from numpy import arange
import time

def somme(istart, istop, pile):
    psum = sum([i**2 for i in arange(istart, istop)])
    pile.put(psum)

if __name__=="__main__":
    
    n    = 10000000
    proc = cpu_count()//2
    pile = Queue()
    threads = []
    somme_totale = 0

    start_time = time.time()
    # Création des workers
    for i in range(proc):
        threads.append(Process(target=somme, args=(i*n/proc, (i+1)*n/proc, pile)))

    # Lancement
    #for i in range(proc):
    #    threads[i].start()
    for thread in threads:
        thread.start()

    # Attente fin de calcul
    for thread in threads:
        thread.join()

    for i in range(proc):
        somme_totale += pile.get()

    print("Somme totale : {}".format(somme_totale))
    print(" ===> {} secondes".format(time.time() - start_time))
from multiprocessing import Process, Queue, cpu_count
from numpy import arange


def partsum(istart, istop, pile):
    psum = sum([i**2 for i in arange(istart, istop)])
    pile.put(psum)


if __name__ == "__main__":
    n = 10000000.
    parts = cpu_count()//2
    pile = Queue()
    threads = []
    sum_tot = 0

    # Création des worker_threads
    for i in range(parts):
        threads.append(Process(target=partsum, args=(i*n/parts, (i+1)*n/parts, pile)))

    # Lancement des threads
    for i in range(parts):
        threads[i].start()

    # Attente de la fin du calcul
    for i in range(parts):
        threads[i].join()

    # Calcul du résultat
    for i in range(parts):
        sum_tot += pile.get()

    print("valeur finale de la somme :  {}".format(sum_tot))

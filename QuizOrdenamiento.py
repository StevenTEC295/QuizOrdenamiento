import time
from Quicksort import Quicksort
    
def generateArray(n):
    import random
    return random.sample(range(0, n), n)


def iteration(lenght):
    times = []
    for i in range(0,10):
        inicio = time.time()
        array = generateArray(lenght)
        print(Quicksort(array))
        fin = time.time()
        fin_inicio = fin-inicio
        print(fin_inicio)
        times.append(fin_inicio)
    return sum(times)/len(times)

if __name__ == "__main__":

    medTimes = []
    for i in range(1000,6000,1000):
        medTimes.append(iteration(i))
    print(medTimes)
    
    
    

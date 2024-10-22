import time
from Quicksort import Quicksort
from BubbleSort import bubble_sort
def generateArray(n):
    import random
    return random.sample(range(0, n), n)


def iterationQuickSort(lenght):
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

def iterationBubbleSort(lenght):
    times = []
    for i in range(0,10):
        inicio = time.time()
        array = generateArray(lenght)
        print(bubble_sort(array))
        fin = time.time()
        fin_inicio = fin-inicio
        print(fin_inicio)
        times.append(fin_inicio)
    return sum(times)/len(times)

if __name__ == "__main__":

    medTimesQuickSort = []
    medTimesBubbleSort = []
    for i in range(1000,6000,1000):
        medTimesQuickSort.append(iterationQuickSort(i))
    print(medTimesQuickSort)

    for i in range(1000,6000,1000):
        medTimesBubbleSort.append(iterationBubbleSort(i))
    print(medTimesQuickSort)

    print(medTimesBubbleSort)

    # Plotting the results
    import matplotlib.pyplot as plt
    Epochs = [1000,2000,3000,4000,5000]
    plt.plot(Epochs, medTimesQuickSort, label='QuickSort')
    plt.plot(Epochs, medTimesBubbleSort, label='BubbleSort')
    
    plt.title('Time of execution of QuickSort and BubbleSort')
    plt.xlabel('Epochs')
    plt.ylabel('Time Execution')
    plt.show()

    # Plotting the results only for QuickSort
    plt.plot(Epochs, medTimesQuickSort)
    plt.title('Time of execution of QuickSort')
    plt.xlabel('Epochs')
    plt.ylabel('Time Execution')
    plt.show()
    
    

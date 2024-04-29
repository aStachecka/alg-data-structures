#algorytmy sortowania
#heapsort

import random
import time


def heapify(T, n, i):
    max = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and T[l] > T[max]:
        max = l

    if r < n and T[r] > T[max]:
        max = r

    if max != i:
        T[i], T[max] = T[max], T[i]
        heapify(T, n, max)


def heapSort(T):
    n = len(T)
    for i in range(n // 2 - 1, -1, -1):
        heapify(T, n, i)

    for i in range(n - 1, 0, -1):
        T[i], T[0] = T[0], T[i]
        heapify(T, i, 0)


smallmediumT = [random.randint(1,1000) for _ in range(10,1000)]
startTimeSM = time.time()
heapSort(smallmediumT)
endTimeSM = time.time()
print(f"heapsort malej/sredniej tablicy zajelo: {endTimeSM - startTimeSM} s")

largeT = [random.randint(1,10000) for _ in range(100000, 1000000)]
startTimeL = time.time()
heapSort(largeT)
endTimeL = time.time()
print(f"heapsort duzej tablicy zajelo: {endTimeL - startTimeL} s")
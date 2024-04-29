#algorytmy sortowania
#mergesort

import time
import random


def mergeSort(T):
    if len(T) > 1:
        mid = len(T) // 2
        L = T[:mid]
        R = T[mid:]

        mergeSort(L)
        mergeSort(R)

        i, j, k = 0, 0, 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                T[k] = L[i]
                i += 1
            else:
                T[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            T[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            T[k] = R[j]
            j += 1
            k += 1


smallmediumT = [random.randint(1,1000) for _ in range(10,1000)]
startTimeSM = time.time()
mergeSort(smallmediumT)
endTimeSM = time.time()
print(f"mergesort malej/sredniej tablicy zajelo: {endTimeSM - startTimeSM} s")

largeT = [random.randint(1,10000) for _ in range(100000, 1000000)]
startTimeL = time.time()
mergeSort(largeT)
endTimeL = time.time()
print(f"mergesort duzej tablicy zajelo: {endTimeL - startTimeL} s")

#algorytmy sortowania
#quicksort

import time
import random


def quickSort(T, l, r):
    if l < r:
        pivot = T[r]
        i = l - 1

        for j in range(l, r):
            if T[j] <= pivot:
                i += 1
                T[i], T[j] = T[j], T[i]

        T[i + 1], T[r] = T[r], T[i + 1]
        pivotIndex = i + 1

        quickSort(T, l, pivotIndex - 1)
        quickSort(T, pivotIndex + 1, r)


smallmediumT = [random.randint(1, 1000) for _ in range(10, 1000)]
startTimeSM = time.time()
quickSort(smallmediumT, 0, len(smallmediumT) - 1)
endTimeSM = time.time()
print(f"quicksort dla malej/sredniej tablicy zajelo: {endTimeSM - startTimeSM} s")

largeT = [random.randint(1, 10000) for _ in range(100000, 1000000)]
startTimeL = time.time()
quickSort(largeT, 0, len(largeT) - 1)
endTimeL = time.time()
print(f"quicksort dla duzej tablicy zajelo: {endTimeL - startTimeL} s")
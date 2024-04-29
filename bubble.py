#algorytmy sortowania
#bubblesort

import random
import time

def bubble(T):
    for i in range(len(T)):
        for j in range(0, len(T)-i-1):
            if T[j] > T[j+1]:
                T[j], T[j+1] = T[j+1], T[j]


smallmediumT = [random.randint(1,1000) for _ in range(10,1000)]
startTimeSM = time.time()
bubble(smallmediumT)
endTimeSM = time.time()
print(f"bubblesort malej/sredniej tablicy zajelo: {endTimeSM - startTimeSM} s")

print("Sortowanie babelkowe nie jest uzywane dla duzych zbiorow danych.")
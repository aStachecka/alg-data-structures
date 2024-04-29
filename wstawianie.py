# algorytmy sortowania
# sortowanie przez wstawianie

import random
import time

def wstawianie(T):

    for k in range(1, len(T)):
        temp = T[k]
        i = k - 1
        while i >= 0 and temp > T[i]:
            T[i+1] = T[i]
            i -= 1
        T[i+1] = temp


smallmediumT = [random.randint(1,1000) for _ in range(10,1000)]
startTimeSM = time.time()
wstawianie(smallmediumT)
endTimeSM = time.time()
print(f"sort. przez wstawianie malej/sredniej tablicy zajelo: {endTimeSM - startTimeSM} s")

print("Sortowanie przez wstawianie nie jest uzywane dla duzych zbiorow danych.")

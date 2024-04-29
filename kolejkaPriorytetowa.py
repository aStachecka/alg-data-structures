#lab3
#implementacja kolejki z priorytetem

class KolejkaPriorytetowa:
    n = 6 #dlugosc kolejki
    tablica = [0] * n
    head = 0
    tail = 0

    def enqueue(self, element):
        self.tablica[self.tail] = str(element)
        self.tail += 1
        if self.tail>5:
            self.tail = 0

    def dequeue(self):
        eMax = self.tablica[0]
        for element in self.tablica:
            if element in self.tablica and int(element) > int(eMax):
                eMax = element

        print(eMax)
        ind = self.tablica.index(eMax)
        self.tablica[0], self.tablica[ind] = self.tablica[ind], self.tablica[0]
        self.tablica[0] = 0

    def find(self):
        element = input("Podaj element do wyszukania: ")
        f = 0
        for e in self.tablica:
            if e == element:
                f = 1
                ind = self.tablica.index(e)
                print("Znaleziono element na miejscu: " + str(ind + 1))
        if f == 0:
            print("Nie znaleziono takiego elementu.")





kp = KolejkaPriorytetowa()
kp.enqueue(10)
kp.enqueue(12)
kp.enqueue(475)
kp.enqueue(45)
kp.enqueue(68)
kp.dequeue()

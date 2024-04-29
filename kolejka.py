#lab3
#implementacja kolejki

class Kolejka:
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
        print(self.tablica[self.head])
        self.tablica[self.head] = 0
        self.head += 1
        if self.head>5:
            self.head = 0

    def find(self):
        element = input("Podaj element do wyszukania: ")
        f = 0
        for e in self.tablica:
            if e == element:
                return 1
        return 0



k = Kolejka()
k.enqueue(1)
k.enqueue(2)
k.enqueue(4)
k.enqueue(4)
k.enqueue(5)
k.enqueue(6)
print(k.tablica)
k.enqueue(7)
print(k.tablica)
k.dequeue()
k.dequeue()
print(k.tablica)
k.dequeue()
#k.dequeue()
#k.dequeue()
#k.dequeue()
#k.dequeue()
#k.dequeue()
print(k.tablica)
print(k.find())
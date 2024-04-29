# lab3, implementacja stosu

class Stos:
    size = 5
    top = 0
    tablica = [None] * size
    def _is_empty(self):
        if self.top == 0:
            return True
        else:
            return False

    def _is_full(self):
        if self.top == self.size:
            return True
        else:
            return False

    def push(self, element):
        if self._is_full():
            print("Nie mozna dodac elementu. Stos jest pelny.")
        else:
            self.tablica[self.top] = str(element)
            self.top += 1

    def pop(self):
        if self._is_empty():
            print("Nie mozna usunac elementu. Stos jest pusty.")
        else:
            print(self.tablica[self.top-1])
            self.tablica[self.top-1] = None
            self.top -= 1
    def find(self):
        element = input("Podaj element do wyszukania: ")
        f = 0
        for e in self.tablica:
            if e == element:
                f = 1
                ind = self.tablica.index(e)
                print("Znaleziono element na miejscu: "+str(ind+1))
        if f==0:
            print("Nie znaleziono takiego elementu.")


s = Stos()
s.push(1)
s.pop()
s.pop()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.pop()
print(s.tablica)
s.find()

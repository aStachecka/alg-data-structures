#lab3
#implementacja listy jednokierunkowej z wartownikiem

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class ListaWartownik():
    def __init__(self):
        self.wartownik = Node(None)

    def add(self, element, index):
        newNode = Node(element)
        currentNode = self.wartownik

        for i in range(index):
            if currentNode.next:
                currentNode = currentNode.next
            else:
                print("Nie mozna dodac elementu na miejsce o zadanym indeksie.")

        newNode.next = currentNode.next
        currentNode.next = newNode

    def remove(self, index):
        currentNode = self.wartownik

        for i in range(index - 1):
            if currentNode.next:
                currentNode = currentNode.next
            else:
                return

        if currentNode.next:
            currentNode.next = currentNode.next.next

    def find(self, element):
        currentNode = self.wartownik.next
        i = 1

        while currentNode:
            if currentNode.value == element:
                return print(f'Zadany element znajduje się na {i} pozycji')
            else:
                currentNode = currentNode.next
            i += 1

        return print(f'Nie znaleziono danego elementu')

    def printList(self):
        currentNode = self.wartownik.next
        while currentNode:
            print(currentNode.value, end=" -> ")
            currentNode = currentNode.next
        print("None")


lw = ListaWartownik()

lw.add(1, 0)
lw.add(3, 1)
lw.add(9, 2)
lw.printList()

lw.remove(2)
lw.printList()

lw.add(5, 2)
lw.printList()

lw.find(5)
lw.find(0)
#lab3
#implementacja listy dwukierunkowej

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class ListaDwukierunkowa():
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, item, index):
        newNode = Node(item)

        if index == 0:
            newNode.next = self.head
            if self.head:
                self.head.previous = newNode
            self.head = newNode
            if self.tail is None:
                self.tail = newNode
        else:
            currentNode = self.head
            for i in range(0, index - 1):
                if currentNode:
                    currentNode = currentNode.next

            if currentNode:
                newNode.next = currentNode.next
                if currentNode.next:
                    currentNode.next.previous = newNode
                currentNode.next = newNode
                newNode.previous = currentNode
                if newNode.next is None:
                    self.tail = newNode
            else:
                print("Nie mozna dodac elementu na pozycje o zadanym indeksie.")

    def remove(self, index):
        currentIndex = 1
        currentNode = self.head

        while currentNode is not None:
            if currentIndex == index:
                if currentNode.previous is not None:
                    currentNode.next.previous = currentNode.next
                else:
                    self.head = currentNode.next
                if currentNode.next is not None:
                    currentNode.next.previous = currentNode.previous
                else:
                    self.tail = currentNode.previous
            currentNode = currentNode.next
            currentIndex += 1

    def find(self, value):
        currentNode = self.head
        i = 1

        while currentNode:
            if currentNode.value == value:
                return print(f'Element znajduje się na {i} pozycji')
            else:
                currentNode = currentNode.next
            i += 1

        return print('Nie znaleziono elementu.')

    def printList(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value, end=" <-> ")
            currentNode = currentNode.next
        print("None")

    def printReversed(self):
        currentNode = self.tail
        while currentNode:
            print(currentNode.value, end=" <-> ")
            currentNode = currentNode.previous
        print("None")


ld = ListaDwukierunkowa()

ld.add(1, 0)
ld.add(2, 1)
ld.add(3, 2)
ld.add(4, 3)

ld.printList()
ld.printReversed()

ld.remove(2)
ld.printList()
ld.printReversed()

ld.add(3, 2)
ld.printList()
ld.printReversed()

ld.find(3)
ld.find(4)
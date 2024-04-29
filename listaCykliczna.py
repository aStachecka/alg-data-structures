#lab3
#implementacja listy cyklicznej

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class ListaCykliczna():
    def __init__(self):
        self.head = None

    def add(self, element, index):
        newNode = Node(element)

        if index == 0:
            newNode.next = self.head
            if newNode.next is None:
                newNode.next = newNode

            self.head = newNode

        else:
            currentNode = self.head
            for i in range(0, index - 1):
                if currentNode:
                    currentNode = currentNode.next
            if currentNode:
                newNode.next = currentNode.next
                currentNode.next = newNode
                if newNode.next is None:
                    newNode.next = self.head
            else:
                print("Nie mozna dodac elementu na pozycje o zadanym indeksie.")

    def remove(self, index):
        currentIndex = 1
        currentNode = self.head
        previousNode = None

        while currentNode:
            if currentIndex == index:
                if previousNode:
                    previousNode.next = currentNode.next

                    if currentNode == self.head:
                        temp = self.head
                        while temp.next != self.head:
                            temp = temp.next

                        temp.next = currentNode.next

                else:
                    self.head = currentNode.next
                    if currentNode == self.head:
                        self.head = None
                return

            previousNode = currentNode
            currentNode = currentNode.next
            currentIndex += 1

    def find(self, element):
        currentNode = self.head
        i = 1

        while currentNode:
            if currentNode.value == element:
                return print(f'Zadany element znajduje się na {i} pozycji')
            else:
                currentNode = currentNode.next
            i += 1

            if currentNode == self.head:
                return print(f'Nie znaleziono takiego elementu')

    def printList(self):
        currentNode = self.head

        while currentNode:
            print(currentNode.value, end=" -> ")
            currentNode = currentNode.next

            if currentNode == self.head:
                break

        print("None")


lc = ListaCykliczna()

lc.add(1, 0)
lc.add(2, 1)
lc.add(3, 2)

lc.printList()

lc.remove(3)
lc.printList()

lc.add(5, 2)
lc.printList()

lc.find(2)
lc.find(6)
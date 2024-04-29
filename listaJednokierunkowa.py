#lab3
#implementacja listy jednokierunkowej

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class ListaJednokierunkowa():
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, element, ind):
        newNode = Node(element)

        if ind == 0:
            newNode.next = self.head
            self.head = newNode

        else:
            currentNode = self.head
            for i in range(0, ind - 1):
                if currentNode:
                    currentNode = currentNode.next
            if currentNode:
                newNode.next = currentNode.next
                currentNode.next = newNode
            else:
                print("Nie mozna dodac elementu na pozycje o zadanym indeksie.")

    def remove(self, ind):
        currentInd = 1
        currentNode = self.head
        prevNode = None

        while currentNode:
            if currentInd == ind:
                if prevNode:
                    prevNode.next = currentNode.next
                else:
                    self.head = currentNode.next
                    return

            prevNode = currentNode
            currentNode = currentNode.next
            currentInd += 1

    def find(self, element):
        currentNode = self.head
        i = 1
        while currentNode:
            if currentNode.value == element:
                return print(f'Szukany element znajduje się na {i} pozycji')
            else:
                currentNode = currentNode.next
            i += 1

        return print(f'Nie znaleziono elementu {element} na liscie')

    def printList(self):
        currentNode = self.head

        while currentNode:
            print(currentNode.data, end=" -> ")
            currentNode = currentNode.next

        print("None")


lj = ListaJednokierunkowa()

lj.add(1, 0)
lj.add(2, 1)
lj.add(3, 2)
lj.add(4, 3)

lj.printList()
lj.remove(2)
lj.printList()

lj.add(5, 2)
lj.printList()

lj.find(3)
lj.find(4)
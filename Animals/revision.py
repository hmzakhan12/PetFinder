class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegining(self, data):
        newHead = Node(data, self.head)
        self.head = newHead

    def print(self):
        if self.head:
            n = self.head
            strng = ""
            while n:
                strng += str(n.data) + '-->'
                n = n.next
            print(strng)

        else:
            print("Linked list is empty")
            return

    def insertatEnd(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        else:
            n = self.head
            while n.next:
                n = n.next

            n.next = Node(data)

    def insertValues(self, lst):
        self.head = None
        for i in lst:
            self.insertatEnd(i)

    def getLength(self):
        if self.head is None:
            return 0
        else:
            counter = 0
            n = self.head
            while n:
                counter += 1
                n = n.next
            return counter

    def RemoveAt(self, ind):
        if self.getLength() == 0:
            print("list is empty")
            return
        else:
            n = self.head

            if ind == 0:
                self.head = self.head.next
            else:
                counter = 0

                while counter != ind - 1:
                    counter += 1
                    n = n.next

                n.next = n.next.next

    def insertAt(self,data,ind):
        if ind == 0:
            self.insertAtBegining(data)
            return
        else:
            counter = 0
            n = self.head

            while counter != ind - 1:
                counter += 1
                n = n.next

            new = Node(data, n.next)
            n.next = new





def get_hash(key):
    n = 0
    for i in key:
        n += ord(i)
    return n % 100

print(get_hash("March 28"))
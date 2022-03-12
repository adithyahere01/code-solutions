#create nodes
#create linkedlist
#add notes to linkedlist 
#print linkedlist

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            #getting the last node
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printList(self):
        if self.head is None:
            print("Linkedlist is Empty phew:)")
            return

        curNode = self.head
        while curNode:
            print(curNode.data)
            curNode = curNode.next


#node => data, next
firstNode = Node("adithya")
linkedlist = Linkedlist()
linkedlist.insert(firstNode)
secondNode = Node("Adhiban")
linkedlist.insert(secondNode)
thirdNode = Node("Adi")
linkedlist.insert(thirdNode)
linkedlist.printList()

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

    def setNext(self, next_node):
        self.next = next_node

    def hasNext(self):
        return self.next is not None

    def getNext(self):
        return self.next

    def getData(self):
        return self.data


class LinkedListFunc:
    def __init__(self, head):
        self.first = head

    def insert_at_end(self, next_node):
        tmp_node = self.first

        if(tmp_node):
            while tmp_node.hasNext():       
                tmp_node = tmp_node.getNext()
                
        tmp_node.setNext(next_node)

    def printList(self):
        tmp_node = self.first
        if (tmp_node):
            while tmp_node:
                print(str(tmp_node.getData()) + " -> ") 
                tmp_node = tmp_node.getNext()  
        

hd = Node(5)
ll = LinkedListFunc(hd)
ll.insert_at_end(Node(9))
ll.insert_at_end(Node(10))
ll.insert_at_end(Node(4))

ll.printList()
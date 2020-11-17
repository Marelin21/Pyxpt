class Node:
    def __init__(self, data = None, nextNode = None):
        self.data = data
        self.nextNode = nextNode
class Linkedlist:
    def __init__(self):
        self.head = None
    def insert_begining(self,data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("linkedlist is empty")
            return
        itr = self.head
        llstr = ''

        while itr :
            llstr += str(itr.data) + '-->'
            itr = itr.nextNode
        print(llstr)

if __name__ == '__main__':
    ll = Linkedlist()
    ll.insert_begining("5")
    ll.insert_begining("9")
    ll.insert_begining("10")
    ll.insert_begining("4")
    ll.print()



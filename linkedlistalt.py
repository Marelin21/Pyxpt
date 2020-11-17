class LinkedlistNode:
    def __init__(self, value, nextNode = None):
        self.value = value
        self.nextNode = nextNode

#"5"->"9"->"10"->"4"

node1 = LinkedlistNode("5")
node2 = LinkedlistNode("9")
node3 = LinkedlistNode("10")
node4 = LinkedlistNode("4")
node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4

currentNode = node1
while True:
    print("->", currentNode.value)
    if currentNode.nextNode is None :

        break
    currentNode = currentNode.nextNode


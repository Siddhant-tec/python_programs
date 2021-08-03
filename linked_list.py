class Node(object):
    def __init__(self):
        self.data = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.cur_node = None

    def add_node(self, data):
        new_node = Node
        new_node.data = data
        new_node.next = self.cur_node
        self.cur_node = new_node

    def display(self):
        node = self.cur_node
        while node:
            print(node.data)
            node = node.next


ll = LinkedList()
ll.add_node(2)
ll.add_node(3)
ll.add_node(4)
ll.add_node(5)
ll.display()

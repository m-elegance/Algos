class Node:
    def __init__(self, date, next_node=None):
        self.date = date
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, date):
        new_elem = Node(date)
        if self.head is None:
            self.head = new_elem
        else:
            curr = self.head
            while curr.next_node:
                curr = curr.next_node
            curr.next_node = new_elem

    def pop_back(self):
        curr = self.head
        if curr is None or curr.next_node is None:
            self.head = None
        else:
            while curr.next_node:
                temp = curr.next_node
                if temp.next_node is None:
                    break
                curr = curr.next_node
            curr.next_node = None

    def display(self):
        curr = self.head
        if curr is None:
            print("List is empty")
        else:
            while curr.next_node:
                print(curr.date, "->", end=" ")
                curr = curr.next_node
            print(curr.date)


sll = LinkedList()
sll.append(8)
sll.append(4)
sll.append(4)
sll.append(7)
sll.pop_back()
sll.pop_back()
sll.pop_back()

sll.display()

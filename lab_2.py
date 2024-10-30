# односвязанный
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def add_to_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def add_to_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.count += 1

    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def search_index(self, index):
        current = self.head
        counter = 0
        while index != counter:
            if not current.next:
                return None
            current = current.next
            counter += 1
        return current.data

    def delete(self, value):
        if not self.head:
            return None
        if self.head.data == value:
            self.head = self.head.next
            return None
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next

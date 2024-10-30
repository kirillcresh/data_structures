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
        if index >= self.count:
            return None
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
        self.count -= 1

    def add_index(self, index, data):
        if index < 0 or index > self.count:
            raise IndexError("Index out of bounds.")

        new_node = Node(data)
        if index == 0:
            self.add_to_head(data)
        elif index == self.count:
            self.add_to_tail(data)
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.count += 1

    def delete_index(self, index):
        if index < 0 or index >= self.count:
            raise IndexError("Index out of bounds.")

        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.count -= 1


class NodeDb:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add_to_head(self, data):
        new_node = NodeDb(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.count += 1

    def add_to_tail(self, data):
        new_node = NodeDb(data)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def search_index(self, index):
        if index < 0 or index >= self.count:
            return None
        if index > (self.count - 1) / 2:
            current = self.tail
            for _ in range(index):
                current = current.prev
        else:
            current = self.head
            for _ in range(index):
                current = current.next
        return current.data

    def delete(self, value):
        if not self.head:
            return
        if self.head.data == value:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self.count -= 1
            return
        current = self.head
        while current:
            if current.data == value:
                if current == self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                self.count -= 1
                return
            current = current.next

    def add_index(self, index, data):
        if index < 0 or index > self.count:
            raise IndexError("Index out of bounds.")

        new_node = NodeDb(data)
        if index == 0:
            self.add_to_head(data)
        elif index == self.count:
            self.add_to_tail(data)
        else:
            if index > (self.count - 1) / 2:
                current = self.tail
                for _ in range(index):
                    current = current.prev
            else:
                current = self.head
                for _ in range(index - 1):
                    current = current.next
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node
            self.count += 1

    def delete_index(self, index):
        if index < 0 or index >= self.count:
            raise IndexError("Index out of bounds.")

        if index == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        elif index == self.count - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            if index > (self.count - 1) / 2:
                current = self.tail
                for _ in range(index):
                    current = current.prev
            else:
                current = self.head
                for _ in range(index):
                    current = current.next
            current.prev.next = current.next
            current.next.prev = current.prev
        self.count -= 1

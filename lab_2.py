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

    def delete_index(self, index):  # NOSONAR
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


def get_add_head(type_list):
    if type_list == "sll":
        sll = SinglyLinkedList()
        for i in range(10000):
            sll.add_to_head(i)
    elif type_list == "dll":
        dll = DoublyLinkedList()
        for i in range(10000):
            dll.add_to_head(i)
    else:
        list_test = []
        for i in range(10000):
            list_test.insert(0, i)


def get_add_tail(type_list):
    if type_list == "sll":
        sll = SinglyLinkedList()
        for i in range(10000):
            sll.add_to_tail(i)
    elif type_list == "dll":
        dll = DoublyLinkedList()
        for i in range(10000):
            dll.add_to_tail(i)
    else:
        list_test = []
        for i in range(10000):
            list_test.append(i)


sll_test = SinglyLinkedList()
dll_test = DoublyLinkedList()
sll_test1 = SinglyLinkedList()
dll_test1 = DoublyLinkedList()
for x in range(1000):
    sll_test.add_to_tail(x)
    dll_test.add_to_tail(x)
    sll_test1.add_to_tail(x)
    dll_test1.add_to_tail(x)

list_test = [i for i in range(1000)]
list_test1 = [i for i in range(1000)]


def test_add_index(type_list):
    if type_list == "sll":
        for i in range(10000):
            sll_test.add_index(sll_test.count - 500, i)
    elif type_list == "dll":
        for i in range(10000):
            dll_test.add_index(dll_test.count - 500, i)
    else:
        len_list = len(list_test)
        for i in range(10000):
            list_test.insert(len_list - 500, i)


def test_find(type_list):
    if type_list == "sll":
        for i in range(1000):
            sll_test.search(i)
    elif type_list == "dll":
        for i in range(1000):
            dll_test.search(i)
    else:
        for i in range(1000):
            list_test.index(i)


def test_find_index(type_list):
    if type_list == "sll":
        for i in range(1000):
            sll_test.search_index(i)
    elif type_list == "dll":
        for i in range(1000):
            dll_test.search_index(i)
    else:
        for i in range(1000):
            list_test[i]


def test_delete(type_list):
    if type_list == "sll":
        for i in range(1000):
            sll_test.delete(i)
    elif type_list == "dll":
        for i in range(1000):
            dll_test.delete(i)
    else:
        for i in range(1000):
            list_test.remove(i)


def test_delete_index(type_list):
    if type_list == "sll":
        for i in range(999, 0, -1):
            sll_test1.delete_index(i)
    elif type_list == "dll":
        print(dll_test1.count)
        for i in range(999, 0, -1):
            dll_test1.delete_index(i)
    else:
        for i in range(999, 0, -1):
            list_test1.pop(i)


def get_list_method(method, type_list):
    if method == "Добавление в начало":
        get_add_head(type_list)
    if method == "Добавление в конец":
        get_add_tail(type_list)
    if method == "Добавление в середину":
        test_add_index(type_list)
    if method == "Поиск":
        test_find(type_list)
    if method == "Поиск по индексу":
        test_find_index(type_list)
    if method == "Удаление":
        test_delete(type_list)
    if method == "Удаление по индексу":
        test_delete_index(type_list)

class Node:
    def __init__(self, data, color="R"):
        self.data = data
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(data=None, color="B")
        self.root = self.NIL

    def insert(self, data):
        new_node = Node(data)
        new_node.left = self.NIL
        new_node.right = self.NIL
        self._insert(new_node)
        # Балансировка
        self._fix_insert(new_node)

    def _insert(self, new_node):
        y = None
        x = self.root
        while x != self.NIL:
            y = x
            if new_node.data < x.data:
                x = x.left
            else:
                x = x.right
        new_node.parent = y
        if y is None:
            self.root = new_node
        elif new_node.data < y.data:
            y.left = new_node
        else:
            y.right = new_node

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _rotate_right(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def _fix_insert(self, k):
        while k != self.root and k.parent.color == "R":
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.color == "R":
                    k.parent.color = "B"
                    u.color = "B"
                    k.parent.parent.color = "R"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self._rotate_left(k)
                    k.parent.color = "B"
                    k.parent.parent.color = "R"
                    self._rotate_right(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == "R":
                    k.parent.color = "B"
                    u.color = "B"
                    k.parent.parent.color = "R"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self._rotate_right(k)
                    k.parent.color = "B"
                    k.parent.parent.color = "R"
                    self._rotate_left(k.parent.parent)
        self.root.color = "B"

    def search(self, data):
        return self._search_tree_helper(self.root, data)

    def _search_tree_helper(self, node, key):
        if node == self.NIL or key == node.data:
            return node
        if key < node.data:
            return self._search_tree_helper(node.left, key)
        return self._search_tree_helper(node.right, key)
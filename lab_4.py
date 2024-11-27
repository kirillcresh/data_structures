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

    def delete(self, data):
        node_to_delete = self.search(data)
        if node_to_delete == self.NIL:
            return  # Узел не найден

        original_color = node_to_delete.color
        if node_to_delete.left == self.NIL:
            temp = node_to_delete.right
            self._transplant(node_to_delete, node_to_delete.right)
        elif node_to_delete.right == self.NIL:
            temp = node_to_delete.left
            self._transplant(node_to_delete, node_to_delete.left)
        else:
            successor = self._minimum(node_to_delete.right)
            original_color = successor.color
            temp = successor.right
            if successor.parent == node_to_delete:
                temp.parent = successor
            else:
                self._transplant(successor, successor.right)
                successor.right = node_to_delete.right
                successor.right.parent = successor
            self._transplant(node_to_delete, successor)
            successor.left = node_to_delete.left
            successor.left.parent = successor
            successor.color = node_to_delete.color

        if original_color == "B":
            self._fix_delete(temp)

    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def _fix_delete(self, x):
        while x != self.root and x.color == "B":
            if x == x.parent.left:
                sibling = x.parent.right
                if sibling.color == "R":
                    sibling.color = "B"
                    x.parent.color = "R"
                    self._rotate_left(x.parent)
                    sibling = x.parent.right
                if sibling.left.color == "B" and sibling.right.color == "B":
                    sibling.color = "R"
                    x = x.parent
                else:
                    if sibling.right.color == "B":
                        sibling.left.color = "B"
                        sibling.color = "R"
                        self._rotate_right(sibling)
                        sibling = x.parent.right
                    sibling.color = x.parent.color
                    x.parent.color = "B"
                    sibling.right.color = "B"
                    self._rotate_left(x.parent)
                    x = self.root
            else:
                sibling = x.parent.left
                if sibling.color == "R":
                    sibling.color = "B"
                    x.parent.color = "R"
                    self._rotate_right(x.parent)
                    sibling = x.parent.left
                if sibling.right.color == "B" and sibling.left.color == "B":
                    sibling.color = "R"
                    x = x.parent
                else:
                    if sibling.left.color == "B":
                        sibling.right.color = "B"
                        sibling.color = "R"
                        self._rotate_left(sibling)
                        sibling = x.parent.left
                    sibling.color = x.parent.color
                    x.parent.color = "B"
                    sibling.left.color = "B"
                    self._rotate_right(x.parent)
                    x = self.root
        x.color = "B"

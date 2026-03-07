# Binary Search Tree
from datetime import datetime


class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data == data:
            return # value already present

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        element = []

        # add from left subtree
        if self.left:
            element += self.left.in_order_traversal()

        # add root node
        element.append(self.data)

        # add right subtree
        if self.right:
            element += self.right.in_order_traversal()

        return element

    def pre_order_traversal(self):
        element = []

        element.append(self.data)

        if self.left:
            element += self.left.pre_order_traversal()

        if self.right:
            element += self.right.pre_order_traversal()

        return element

    def post_order_traversal(self):
        element = []

        if self.left:
            element += self.left.post_order_traversal()

        if self.right:
            element += self.right.post_order_traversal()

        element.append(self.data)

        return element

    def search(self, value):
        if self.data == value:
            return True

        if value < self.data:
            # search in left subtree
            if self.left:
                return self.left.search(value)
            else:
                return False
        else:
            # search in right subtree
            if self.right:
                return self.right.search(value)
            else:
                return False

    def find_min(self):
        if self.left:
            return self.left.find_min()
        return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        return self.data

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0

        return left_sum + right_sum + self.data

    def delete(self, value):
        if value < self.data:
            self.left = self.left.delete(value)
        elif value > self.data:
            self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    number_tree = build_tree(numbers)
    print('in_order_traversal ==> ', number_tree.in_order_traversal())
    print('pre_order_traversal ==> ', number_tree.pre_order_traversal())
    print('post_order_traversal ==> ', number_tree.post_order_traversal())
    print(number_tree.search(200))
    print(number_tree.find_min())
    print(number_tree.find_max())
    print(number_tree.calculate_sum())
    number_tree.delete(20)
    print('in_order_traversal ==> ', number_tree.in_order_traversal())
    number_tree.delete(9)
    print('in_order_traversal ==> ', number_tree.in_order_traversal())


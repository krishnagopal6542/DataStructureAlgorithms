import collections


class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data == data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def pretty_print(self):
        """Prints the binary tree in a pyramid-like structure with connecting lines."""
        if not self:
            return

        # BFS traversal to collect nodes level by level
        q = collections.deque([self])
        levels = []
        while q:
            level_size = len(q)
            level = []
            for _ in range(level_size):
                node = q.popleft()
                if node:
                    level.append(node)
                    q.append(node.left)
                    q.append(node.right)
                else:
                    level.append(None)
                    q.append(None)
                    q.append(None)
            if any(x is not None for x in level):  # stop when only Nones
                levels.append(level)
            else:
                break

        height = len(levels)
        max_width = 2 ** height * 2

        for i, level in enumerate(levels):
            spacing = max_width // (2 ** (i + 1))

            # Print node values
            line = ""
            for node in level:
                line += " " * (spacing - 1)
                line += str(node.data) if node else " "
                line += " " * spacing
            print(line)

            # Print connecting lines
            if i < height - 1:
                line = ""
                for node in level:
                    space_between = spacing * 2 - 1
                    if node:
                        line += " " * (spacing - 1)
                        line += "/" if node.left else " "
                        line += " " * (space_between - 1)
                        line += "\\" if node.right else " "
                        line += " " * (spacing - 1)
                    else:
                        line += " " * (space_between + spacing + 1)
                print(line)

    def search_element(self, val, path):
        path.append(self.data)
        if self.data == val:
            return True, path

        if val < self.data and self.left:
            return self.left.search_element(val, path)

        if val > self.data and self.right:
            return self.right.search_element(val, path)

        return False, []


def build_tree(elements):
    root = BinarySearchTree(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    num = [17, 4, 1, 20, 9, 23, 18, 34]
    number_tree = build_tree(num)
    print("\nPretty print of tree:")
    number_tree.pretty_print()
    print("number_tree.search_element ==> ", number_tree.search_element(9, []))

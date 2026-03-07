import collections

res = 0


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
        elif data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def in_order_traversal(self):
        in_order_element = []

        # visit left
        if self.left:
            in_order_element += self.left.in_order_traversal()

        # visit root node
        in_order_element.append(self.data)

        # visit right
        if self.right:
            in_order_element += self.right.in_order_traversal()

        return in_order_element

    def pre_order_traversal(self):
        pre_order_element = []

        # visit root node
        pre_order_element.append(self.data)

        # visit left
        if self.left:
            pre_order_element += self.left.pre_order_traversal()

        # visit right
        if self.right:
            pre_order_element += self.right.pre_order_traversal()
        return pre_order_element

    def post_order_traversal(self):
        post_order_element = []

        # visit left
        if self.left:
            post_order_element += self.left.post_order_traversal()

        # visit right
        if self.right:
            post_order_element += self.right.post_order_traversal()

        # visit root node
        post_order_element.append(self.data)
        return post_order_element

    def level_order_traversal_by_level(self):
        q = collections.deque()
        res = []

        q.append(self)

        while q:
            level = []
            q_len = len(q)
            for _ in range(q_len):
                node = q.popleft()
                if node:
                    level.append(node.data)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res

    def level_order_traversal(self):
        q = collections.deque()
        res = []

        q.append(self)

        while q:
            node = q.popleft()
            res.append(node.data)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return res

    def level_order_traversal_test(self):
        q = collections.deque()
        res = []

        q.append(self)

        while q:
            node = q.popleft()
            if node:
                res.append(node.data)
                q.append(node.left)
                q.append(node.right)

        return res

    def zigzag_level_order_traversal(self):
        q = collections.deque()
        zigzag_result = []

        q.append(self)

        flag = False

        while q:
            level = []
            q_len = len(q)
            if not flag:
                for _ in range(q_len):
                    node = q.popleft()
                    if node:
                        level.append(node.data)
                        if node.left:
                            q.append(node.left)
                        if node.right:
                            q.append(node.right)
                if level:
                    zigzag_result.append(level)

                flag = True
            else:
                stack = []
                stack_res = []
                for _ in range(q_len):
                    node = q.popleft()
                    if node:
                        stack.append(node.data)
                        if node.left:
                            q.append(node.left)
                        if node.right:
                            q.append(node.right)
                while stack:
                    stack_res.append(stack.pop())

                if stack_res:
                    zigzag_result.append(stack_res)

                flag = False

        return zigzag_result

    def zigzag_level_order_traversal_optimized(self):
        q = collections.deque()
        result = []

        q.append(self)
        left_to_right = True

        while q:
            level = collections.deque()
            q_len = len(q)
            for _ in range(q_len):
                node = q.popleft()
                if node:
                    level.append(node.data) if left_to_right else level.appendleft(node.data)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            result.append(list(level))
            left_to_right = not left_to_right

        return result

    def invert_binary_search_tree(self):
        q = collections.deque()
        res = []

        q.append(self)

        while q:
            level = collections.deque()
            q_len = len(q)
            for _ in range(q_len):
                node = q.popleft()
                if node:
                    level.appendleft(node.data)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.extend(list(level))

        return res

    def search(self, val, path):
        path.append(self.data)
        if self.data == val:
            return True, path

        if val < self.data and self.left:
            return self.left.search(val, path)

        elif val > self.data and self.right:
            return self.right.search(val, path)

        path.pop()
        return False, []

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0

        return self.data + left_sum + right_sum

    def height(self):
        left_height = self.left.height() if self.left else -1
        right_height = self.right.height() if self.right else -1

        return 1 + max(left_height, right_height)

    def diameter_of_binary_tree(self):
        left_height = self.left.height() if self.left else -1
        right_height = self.right.height() if self.right else -1
        res = max(res, 1 + max(left_height, right_height))

        return 1 + max(left_height, right_height)

    def delete_by_min_val(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_by_min_val(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete_by_min_val(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete_by_min_val(min_val)

        return self

    def delete_by_max_val(self, val):
        if val < self.data:
            if self.left:
                self.left.delete_by_max_val(val)
        elif val > self.data:
            if self.right:
                self.right.delete_by_max_val(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete_by_max_val(max_val)

        return self

    def right_view_of_tree(self):
        q = collections.deque()
        right_side = []

        q.append(self)

        while q:
            right_len = None
            q_len = len(q)

            for _ in range(q_len):
                node = q.popleft()
                if node:
                    right_len = node
                    q.append(node.left)
                    q.append(node.right)

            if right_len:
                right_side.append(right_len.data)

        return right_side

    def left_view_of_tree(self):
        q = collections.deque()
        left_side = []

        q.append(self)
        while q:

            q_len = len(q)

            for i in range(q_len):
                node = q.popleft()
                if i == 0:
                    left_side.append(node.data)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return left_side

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

    def all_path_sum(self, path):
        if not self:
            return 0

        path.append(str(self.data))

        # Leaf Node
        if not self.left and not self.right:
            print(f"Path to leaf: {' -> '.join(map(str, path))}")
            pathElement = ""
            for element in path:
                pathElement += element
            path.pop()
            return int(pathElement)

        else:
            pathSum = 0
            if self.left:
                pathSum += self.left.all_path_sum(path)
            if self.right:
                pathSum += self.right.all_path_sum(path)

        path.pop()
        return pathSum




def build_tree(elements):
    root = BinarySearchTree(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    # num = [17, 4, 1, 20, 9, 23, 18, 34]
    num = [1, 2, 3]
    number_tree = build_tree(num)
    print("\nPretty print of tree:")
    number_tree.pretty_print()

    print("in_order_traversal ==> ", number_tree.in_order_traversal())
    print("pre_order_traversal ==> ", number_tree.pre_order_traversal())
    print("post_order_traversal ==> ", number_tree.post_order_traversal())
    print("level_order_traversal ==> ", number_tree.level_order_traversal())
    print("level_order_traversal_by_level ==> ", number_tree.level_order_traversal_by_level())
    print("number_tree.zigzag_level_order_traversal ==> ", number_tree.zigzag_level_order_traversal())
    print("number_tree.zigzag_level_order_traversal == Optimized ==> ",
          number_tree.zigzag_level_order_traversal_optimized())
    print("number_tree.invert_binary_search_tree ==> ", number_tree.invert_binary_search_tree())

    # print("number_tree Delete==> ", number_tree.delete_by_max_val(20))
    print("in_order_traversal ==> ", number_tree.in_order_traversal())
    print("calculate_sum ==> ", number_tree.calculate_sum())
    print("number_tree,search ==> ", number_tree.search(19, []))
    print("find_min ==> ", number_tree.find_min())
    print("find_max ==> ", number_tree.find_max())
    print("height ==> ", number_tree.height())
    print("right_view_of_tree ==> ", number_tree.right_view_of_tree())
    print("left_view_of_tree ==> ", number_tree.left_view_of_tree())
    print("all_path_sum ==> ", number_tree.all_path_sum([]))

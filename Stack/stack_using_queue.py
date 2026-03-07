from collections import deque


class MyStack:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack.popleft()

    def empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        return False


if __name__ == '__main__':
    obj = MyStack()
    obj.push(2)
    param_2 = obj.pop()
    param_3 = obj.top()
    param_4 = obj.empty()

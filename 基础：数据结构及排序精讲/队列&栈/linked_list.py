# https://labuladong.online/zh/algo/data-structure-basic/linked-queue-st

from collections import deque


class MyLinkedStack:
    def __init__(self):
        self.list = deque()

    def push(self, val):
        self.list.append(val)

    def pop(self):
        return self.list.pop()

    def peek(self):
        return self.list[-1]

    def size(self):
        return len(self.list)


class MyLinkedQueue:
    def __init__(self):
        self.list = deque()

    def push(self, val):
        self.list.append(val)

    def pop(self):
        return self.list.popleft()

    def peek(self):
        return self.list[0]

    def size(self):
        return len(self.list)

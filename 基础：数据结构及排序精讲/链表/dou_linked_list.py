# https://labuladong.online/zh/algo/data-structure-basic/linkedlist-implement/


class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_last(self, val):
        node = Node(val)
        temp = self.tail.prev

        # temp <-> node
        temp.next = node
        node.prev = temp
        # node <-> tail
        node.next = self.tail
        self.tail.prev = node
        # temp <-> node <-> tail

        self.size += 1

    def add_first(self, val):
        node = Node(val)
        temp = self.head.next

        temp.prev = node
        node.next = temp
        self.head.next = node
        node.prev = self.head

        self.size += 1

    def add(self, index, val):
        self.check_position_index(index)

        if self.size == index:
            self.add_last(val)
            return

        p = self.get_node(index)
        temp = p.prev
        node = Node(val)

        temp.next = node
        node.prev = temp
        node.next = p
        p.prev = node

        self.size += 1

    def remove_fist(self):
        if self.size < 1:
            raise Exception("NoSuchElementException")

        x = self.head.next
        self.head.next = x.next
        x.prev = self.head

        self.size -= 1

        return x.val

    def remove_last(self):
        if self.size < 1:
            raise Exception("NoSuchElementException")

        x = self.tail.prev
        temp = x.prev

        temp.next = self.tail
        self.tail.prev = temp

        self.size -= 1

        return x.val

    def remove(self, index):
        self.check_element_index(index)

        if index == self.size - 1:
            return self.remove_last()

        if index == 0:
            return self.remove_fist()

        p = self.get_node(index)
        prev = p.prev
        next = p.next

        next.prev = prev
        prev.next = next

        self.size -= 1

        return p.val

    def get(self, index):
        self.check_element_index(index)
        p = self.get_node(index)

        return p.val

    def get_first(self):
        if self.size < 1:
            raise Exception("NoSuchElementException")
        return self.get(0)

    def get_last(self):
        if self.size < 1:
            raise Exception("NoSuchElementException")

        return self.tail.prev.val

    def set(self, index, val):
        self.check_element_index(index)

        p = self.get_node(index)
        old_val = p.val
        p.val = val

        return old_val

    def get_node(self, index):
        self.check_element_index(index)

        r = (
            range(0, index + 1)
            if index <= self.size // 2
            else range(self.size - 1, index - 1, -1)
        )
        temp = self.head.next if index <= self.size // 2 else self.tail.prev

        for _ in r:
            temp = temp.next if index <= self.size // 2 else temp.prev

        return temp

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def is_element_index(self, index):
        return 0 <= index < self.size

    def is_position_index(self, index):
        return 0 <= index <= self.size

    def check_position_index(self, index):
        if not self.is_position_index(index):
            raise IndexError(f"Index: {index}, Size: {self.size}")

    def check_element_index(self, index):
        if not self.is_element_index(index):
            raise IndexError(f"Index: {index}, Size: {self.size}")

    def display(self):
        print(f"size = {self.size}")
        print(f"head <-> ", end="")
        temp = self.head.next
        while temp != self.tail:
            print(f"{temp.val} <-> ", end="")
            temp = temp.next
        print("tail")


if __name__ == "__main__":
    list = MyLinkedList()
    list.add_last(1)
    list.add_last(2)
    list.add_last(3)
    list.add_first(0)
    list.add(2, 100)
    list.remove(3)

    list.display()

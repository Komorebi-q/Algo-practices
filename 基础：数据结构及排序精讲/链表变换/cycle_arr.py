# https://labuladong.online/zh/algo/data-structure-basic/cycle-array/


class CycleArray:
    def __init__(self, size=2):
        self.size = size
        self.arr = [None] * size
        self.start = 0
        self.end = 0
        self.count = 0

    def resize(self, new_size):
        new_arr = [None] * new_size

        for i in range(self.count):
            new_arr[i] = self.arr[(self.start + i) % self.size]
        self.arr = new_arr
        self.size = new_size
        self.start = 0
        self.end = self.count

    def add_first(self, val):
        if self.is_full():
            self.resize(self.size * 2)

        self.start = (self.start - 1 + self.size) % self.size
        self.arr[self.start] = val
        self.count += 1

    def add_last(self, val):
        if self.is_full():
            self.resize(self.size * 2)

        # end is open, so we need assign value first
        self.arr[self.end] = val
        self.end = (self.end + 1) % self.size
        self.count += 1

    def remove_first(self):
        if self.is_empty():
            return

        self.arr[self.start] = None
        self.start = (self.start + 1) % self.size
        self.count -= 1

        if self.count == self.size // 4:
            self.resize(self.size // 2)

    def remove_last(self):
        if self.is_empty():
            return

        self.end = (self.end - 1 + self.size) % self.size
        self.arr[self.end] = None
        self.count -= 1

        if self.count == self.size // 4:
            self.resize(self.size // 2)

    def get_first(self):
        if self.is_empty():
            return None
        return self.arr[self.start]

    def get_last(self):
        if self.is_empty():
            return None
        return self.arr[self.end]

    def get(self, index):
        if self.is_empty():
            return None

        return self.arr[(self.start + index) % self.size]

    def set(self, index, val):
        self.check_element_index(index)

        offset = (self.start + index) % self.size
        old_val = self.arr[offset]
        self.arr[offset] = val

        return old_val

    def insert(self, index, val):
        self.check_position_index(index)
        if index == 0:
            self.add_first(val)
            return
        if index == self.count:
            self.add_last(val)
            return

        if self.is_full():
            self.resize(self.size * 2)

        offset = (self.start + index) % self.size
        old_val = self.arr[offset]

        for i in range(1, self.count):
            self.arr[(offset + i) % self.size] = self.arr[(offset + i - 1) % self.size]

        self.arr[offset] = val
        self.count += 1

        return old_val

    def is_element_index(self, index):
        return 0 <= index < self.count

    def is_position_index(self, index):
        return 0 <= index <= self.count

    def check_element_index(self, index):
        if not self.is_element_index(index):
            raise IndexError(f"Index: {index}, Size: {self.size}")

    def check_position_index(self, index):
        if not self.is_position_index(index):
            raise IndexError(f"Index: {index}, Size: {self.size}")

    def is_full(self):
        return self.size == self.count

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.size

    def display(self):
        print(
            f"size = {self.size}, count = {self.count}, start = {self.start}, end = {self.end}"
        )
        print(self.arr)


if __name__ == "__main__":
    arr = CycleArray()
    arr.add_last(1)
    arr.display()
    arr.add_last(2)
    arr.display()
    arr.add_last(3)
    arr.display()
    arr.add_first(0)
    arr.display()
    arr.remove_first()
    arr.display()
    arr.remove_last()
    arr.display()
    arr.get(1)
    arr.display()
    arr.insert(1, 100)
    arr.display()

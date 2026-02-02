# https://labuladong.online/zh/algo/data-structure-basic/array-implement/


class MyArrayList:
    INIT_CAP = 1

    def __init__(self, init_capacity=None):
        self.data = [None] * (
            init_capacity if init_capacity is not None else self.INIT_CAP
        )
        self.size = 0

    def add_last(self, e):
        cap = len(self.data)
        if self.size == cap:
            self._resize(2 * cap)
        self.data[self.size] = e
        self.size += 1

    def add(self, index, e):
        self._check_position_index(index)

        cap = len(self.data)
        if cap == self.size:
            self._resize(2 * cap)

        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]

        self.data[index] = e
        self.size += 1

    def add_first(self, e):
        self.add(0, e)

    def remove_last(self):
        if self.size == 0:
            raise Exception("NoSuchElementException")
        cap = len(self.data)
        if self.size == cap // 4:
            self._resize(cap // 2)

        deleted_ele = self.data[self.size - 1]

        self.data[self.size - 1] = None
        self.size -= 1

        return deleted_ele

    def remove(self, index):
        self._check_element_index(index)
        cap = len(self.data)

        if self.size == cap // 4:
            self._resize(cap // 2)

        deleted_ele = self.data[index]

        for i in range(index, self.size):
            self.data[i] = self.data[i + 1]

        self.data[self.size - 1] = None
        self.size -= 1

        return deleted_ele

    def remove_first(self):
        return self.remove(0)

    def get(self, index):
        self._check_element_index(index)
        return self.data[index]

    def set(self, index, e):
        self._check_element_index(index)
        old_ele = self.data[index]
        self.data[index] = e

        return old_ele

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data

    def _is_element_index(self, index):
        return 0 <= index < self.size

    def _is_position_index(self, index):
        return 0 <= index <= self.size

    def _check_element_index(self, index):
        if not self._is_element_index(index):
            raise IndexError(f"Index: {index}, Size: {self.size}")

    def _check_position_index(self, index):
        if not self._is_position_index(index):
            raise IndexError(f"Index: {index}, Size: {self.size}")

    def display(self):
        print(f"size = {self.size}, cap = {len(self.data)}")
        print(self.data)


if __name__ == "__main__":
    arr = MyArrayList(init_capacity=3)

    for i in range(1, 6):
        arr.add_last(i)
    arr.display()
    arr.remove(3)
    arr.display()
    arr.add(1, 9)
    arr.display()
    arr.add_first(100)
    arr.display()
    val = arr.remove_last()
    arr.display()

    for i in range(arr.get_size()):
        print(arr.get(i))

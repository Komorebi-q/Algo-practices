# https://labuladong.online/zh/algo/data-structure-basic/bitmap/


class MyBitMap:
    def __init__(self, size):
        self.size = size
        array_size = size // 64 + 1
        self.words = [0] * array_size

    def get(self, bit_index):
        if bit_index < 0 or bit_index >= self.size:
            raise IndexError(f"Index: {bit_index}, Size: {self.size}")

        word_index = bit_index // 64
        bit_offset = bit_index % 64

        return (self.words[word_index] & (1 << bit_offset)) != 0

    def set(self, bit_index):
        if bit_index < 0 or bit_index >= self.size:
            raise IndexError(f"Index: {bit_index}, Size: {self.size}")

        word_index = bit_index // 64
        bit_offset = bit_index % 64

        self.words[word_index] |= 1 << bit_offset

    def clear(self, bit_index):
        if bit_index < 0 or bit_index >= self.size:
            raise IndexError(f"Index: {bit_index}, Size: {self.size}")

        word_index = bit_index // 64
        bit_offset = bit_index % 64
        self.words[word_index] &= ~(1 << bit_offset)


if __name__ == "__main__":
    bit_set = MyBitMap(1000)

    bit_set.set(10)
    bit_set.set(100)
    bit_set.set(500)

    print(bit_set.get(10))
    print(bit_set.get(100))
    print(bit_set.get(500))
    print(bit_set.get(80))
    
    bit_set.clear(10)
    print(bit_set.get(10))

# https://labuladong.online/zh/algo/data-structure-basic/bloom-filter/


class MyBitSet:
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


class SimpleBloomFilter:
    def __init__(self, bit_set_size, hash_function_num):
        # 位图的大小
        self.bit_set_size = bit_set_size
        # 位图
        self.bit_set = MyBitSet(bit_set_size)
        # 哈希函数的个数
        self.k = hash_function_num

    # 添加元素
    def add(self, element):
        # 获取 k 个不同的哈希值
        # 将这 k 个哈希值对应的位图中的位都设置为 1
        for i in range(self.k):
            hash_value = self._hash(element, i)
            self.bit_set.set(hash_value)

    # 判断元素是否存在
    def contains(self, element):
        # 获取 k 个不同的哈希值
        # 检查这 k 个哈希值对应的位图中的位是否全部为 1
        for i in range(self.k):
            hash_value = self._hash(element, i)
            if not self.bit_set.get(hash_value):
                return False
        return True

    # 模拟多个哈希函数，实际生产环境中应该使用更复杂的哈希算法
    def _hash(self, element, seed):
        # 这里简化处理，用内置的 hash 函数和递增的索引作为种子来模拟多个哈希函数
        # 在实际应用中，为了减少哈希冲突，应该使用更复杂的哈希函数
        # 同时，种子也应该选择无规律的大质数，而不是简单的递增索引
        return abs(hash(element) + seed) % self.bit_set_size


if __name__ == "__main__":
    # 创建一个位数组大小为 1000000，使用 3 个哈希函数的布隆过滤器
    bloom_filter = SimpleBloomFilter(1000000, 3)

    # 添加元素
    bloom_filter.add("apple")
    bloom_filter.add("banana")
    bloom_filter.add("orange")

    # 检查元素是否存在
    print("Contains apple:", bloom_filter.contains("apple"))       # True
    print("Contains banana:", bloom_filter.contains("banana"))     # True
    print("Contains grape:", bloom_filter.contains("grape"))       # False
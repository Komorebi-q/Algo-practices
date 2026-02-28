# https://labuladong.online/zh/algo/data-structure-basic/hashtable-chaining/


from re import I


class KVNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val


class TinyMyChainingHashMap:
    def __init__(self):
        self.table = [None] * 10

    def hash(self, key):
        return key % len(self.table)

    def get(self, key):
        index = self.hash(key)
        list = self.table[index]

        if list is None:
            return -1

        for node in list:
            if node.key == key:
                return node.val

        return -1

    def put(self, key, val):
        index = self.hash(key)

        if self.table[index] is None:
            self.table[index] = []
            self.table[index].append(KVNode(key, val))
            return

        _list = self.table[index]

        for node in _list:
            if node.key == key:
                node.val = val
                return

        _list.append(KVNode(key, val))

    def remove(self, key):
        index = self.hash(key)
        list = self.table[index]

        if list is None:
            return

        self.table[index] = [node for node in list if node.key != key]


class MyChainingHashMap:
    def __init__(self, init_capacity=4):
        self.size = 0
        self.capacity = max(init_capacity, 1)
        self.table = [[] for _ in range(self.capacity)]

    def put(self, key, val):
        if key is None:
            raise ValueError("key is None")

        index = self._hash(key)
        bucket = self.table[index]

        for node in bucket:
            if node.key == key:
                node.val = val
                return

        bucket.append(KVNode(key, val))
        self.size += 1

        if self.size >= self.capacity * 0.75:
            self._resize(self.capacity * 2)

    def get(self, key):
        if key is None:
            raise ValueError("key is None")

        index = self._hash(key)
        bucket = self.table[index]

        for node in bucket:
            if node.key == key:
                return node.val

        return None

    def remove(self, key):
        if key is None:
            raise ValueError("key is None")

        index = self._hash(key)
        bucket = self.table[index]
        for node in bucket:
            if node.key == key:
                bucket.remove(node)
                self.size -= 1

                if self.size <= self.capacity / 8:
                    self._resize(max(self.capacity // 4, 1))

                return
    
    def keys(self):
        keys = []
        
        for bucket in self.table:
            for node in bucket:
                keys.append(node.key)
        
        return keys
    
    def values(self):
        values = []
        for bucket in self.table:
            for node in bucket:
                values.append(node.val)
        return values
    
    def entries(self):
        entries = []
        
        for bucket in self.table:
            for node in bucket:
                entries.append((node.key, node.val))
        return entries

    def size(self):
        return self.size

    def _resize(self, new_capacity):
        new_map = MyChainingHashMap(new_capacity)

        for node in self.table:
            if node is not None:
                for kv in node:
                    new_map.put(kv.key, kv.val)

        self.table = new_map.table
        self.capacity = new_map.capacity

    def _hash(self, key):
        return hash(key) % self.capacity


# 测试代码
if __name__ == "__main__":
    map = MyChainingHashMap()
    map.put(1, 1)
    map.put(2, 2)
    map.put(3, 3)
    print(map.get(1))  # 1
    print(map.get(2))  # 2

    map.put(1, 100)
    print(map.get(1))  # 100

    map.remove(2)
    print(map.get(2))  # None
    print(map.keys()) # [1, 3]

    map.remove(1)
    map.remove(2)
    map.remove(3)
    print(map.get(1))  # None
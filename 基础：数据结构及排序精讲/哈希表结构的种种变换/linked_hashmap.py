# https://labuladong.online/zh/algo/data-structure-basic/hashtable-with-linked-list/


class MyLinkedHashMap:
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = self.Node(None, None)
        self.tail = self.Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = dict()

    def get(self, key):
        if key not in self.map:
            return None

        return self.map.get(key)

    def put(self, key, val):
        if key not in self.map:
            node = self.Node(key, val)
            self.add_last_node(node)
            self.map[key] = node
            return

        self.map[key].val = val

    def remove(self, key):
        if key not in self.map:
            return

        node = self.map[key]
        del self.map[key]
        self.remove_node(node)

    def contains_key(self, key):
        return key in self.map

    def keys(self):
        keys = []
        node = self.head.next

        while node != self.tail:
            keys.append(node.key)
            node = node.next

        return keys

    def add_last_node(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        self.tail.prev = node
        node.next = self.tail

    def remove_node(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev


if __name__ == "__main__":
    map = MyLinkedHashMap()
    map.put("a", 1)
    map.put("b", 2)
    map.put("c", 3)
    map.put("d", 4)
    map.put("e", 5)

    print(map.keys())  # ['a', 'b', 'c', 'd', 'e']
    map.remove("c")
    print(map.keys())  # ['a', 'b', 'd', 'e']

# https://labuladong.online/zh/algo/data-structure-basic/binary-tree-traverse-basic/

from collections import deque


class TreeNode: 
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def traverse_pre_order(root):
    if root is None:
        return 
    print(root.val, end=" ")
    traverse_pre_order(root.left)
    traverse_pre_order(root.right)

def traverse_in_order(root):
    if root is None:
        return 
    traverse_in_order(root.left)
    print(root.val, end=" ")
    traverse_in_order(root.right)

def traverse_post_order(root):
    if root is None:
        return 
    traverse_post_order(root.left)
    traverse_post_order(root.right)
    print(root.val, end=" ")

def traverse_level_order(root):
    if root is None:
        return
    q = deque()
    depth = 0
    q.append(root)
   
    while q:
       for _ in range(len(q)):
           node = q.popleft()
           print(f"depth {depth}: {node.val}")
           if node.left is not None:
               q.append(node.left)
           if node.right is not None:
               q.append(node.right)
       depth += 1
    
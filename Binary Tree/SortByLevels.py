'''
       1
      / \
     2    3
    / \  / \
   4   5 6  7

'''

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


def tree_by_levels(node):
    p, q = [], [node]
    while q:
        v = q.pop(0)
        if v is not None:
            p.append(v.val)
            q += [v.left,v.right]
    return p if not node is None else []


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(tree_by_levels(root))
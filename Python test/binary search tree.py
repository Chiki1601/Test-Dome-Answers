import collections

Node = collections.namedtuple('Node', ['left', 'right', 'value'])


def contains(root, value):
    if root is None:
        return False
    elif root.value == value:
        return True
    elif root.value >= value:
        return contains(root.left, value)
    else:
        return contains(root.right, value)


n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)

print(contains(n2, 3))

from AVL_Tree import AVLTree
from Circular_Queue import CircularDeque
# TODO: implement the right way

def BFS(root, deq, i=1) -> object:
    if root is None:
        return
    if root.height == 1:
        return
    i += 1
    if root.left is not None:
        deq.insertRear((root.left.val, i))
    if root.right is not None:
        deq.insertRear((root.right.val, i))
    BFS(root.left, deq, i)
    BFS(root.right, deq, i)
    return deq


def printLevelOrder(root):
    """
    Given root node, print the root tree level by level
    """
    deq = CircularDeque((2 ** root.height) - 1)
    deq.insertRear((root.val, 1))
    x = BFS(root, deq)
    d = {}
    for j in range(1, root.height + 1):
        d[j] = []
    while not x.isEmpty():
        d[x.getFront()[1]].append(x.getFront()[0])
        x.deleteFront()
    for j in range(1, root.height + 1):
        print(*d[j])
    print("\n")


def printLevelOrderNoCDQ(root):
    """
    Given root node, print the root tree level by level
    """
    x = CircularDeque(root.height)
    x.insertRear([root])
    for i in range(root.height):
        rear = (x.getRear())
        for j in range(len(rear)):
            if x.deque[i][j] is None:
                continue
            l = x.deque[i][j].left
            r = x.deque[i][j].right
            if rear is x.getRear():
                if l:
                    x.insertRear([x.deque[i][j].left])
                elif r:
                    x.insertRear([x.deque[i][j].right])
                if l and r:
                    x.getRear().append(x.deque[i][j].right)
            else:
                if l:
                    x.getRear().append(x.deque[i][j].left)
                if r:
                    x.getRear().append(x.deque[i][j].right)
    for i in x.deque:
        for j in i:
            print(j.val, end=" ")
        print()
    print()


myTree = AVLTree()
root = None
nums = [33, 13, 52, 9, 21, 61, 8, 11]
# nums = [20, 10, 30, 5, 25, 40, 35, 45]
# nums = [1,4,5,6,9,8]
for num in nums:
    root = myTree.insert(root, num)
# for i in range(1, 32):
#     root = myTree.insert(root, i)
printLevelOrder(root)
printLevelOrderNoCDQ(root)
# myTree.insert(root, 7)
myTree.delete(root,13)
printLevelOrder(root)
printLevelOrderNoCDQ(root)

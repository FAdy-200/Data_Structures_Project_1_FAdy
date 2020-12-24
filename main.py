from AVL_Tree import AVLTree
from Circular_Queue import CircularDeque

def printLevelOrder(root):
    deq = CircularDeque()
    """
    Given root node, print the root tree level by level
    """

    ##############################################################
    ##                      YOUR CODE HERE                      ##
    ##############################################################


myTree = AVLTree()
root = None
nums = [33, 13, 52, 9, 21, 61, 8, 11]
for num in nums:
    root = myTree.insert(root, num)
printLevelOrder(root)
myTree.delete(root, 13)
printLevelOrder(root)

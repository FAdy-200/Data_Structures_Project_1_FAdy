class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.height = 1


class AVLTree:
    def getHeight(self, root):
        """
        Return the height of root node
        """

        if not root: return 0
        return root.height

    def getBalance(self, root):
        """
        Check for root's balance
        """

        if not root: return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        """
        Get the node with lowest value (i.e., far left node)
        """

        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def insert(self, root, val, l=0, r=0):
        """
        Insert node with target value "val"
        """

        if not root:
            return TreeNode(val)
        elif val < root.val:
            l += 1
            r = 0
            root.left = self.insert(root.left, val, l, r)
        else:
            r += 1
            l = 0
            root.right = self.insert(root.right, val, l, r)
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
        root = self.__rotate(root, l, r)

        return root

    def delete(self, root, val, l=0, r=0):
        """
        Delete a node with target value "val"
        """

        if not root:
            return root
        elif val < root.val:
            l += 1
            r = 0
            root.left = self.delete(root.left, val)
        elif val > root.val:
            r += 1
            l = 0
            root.right = self.delete(root.right, val)
        else:
            if root.left is None:
                temp, root = root.right, None
                return temp
            elif root.right is None:
                temp, root = root.left, None
                return temp
            temp = self.getMinValueNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)
        if root is None:
            return root
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
        root = self.__rotate(root, l, r)

        return root

    def __rotate(self, root, l, r):

        if root.left is not None:
            if root.right is not None:
                if (root.left.height - root.right.height) > 1:
                    if root.left.height == 3 and root.right.height == 1 and l == 2:
                        root.left = self.rotateLeft(root.right)
                    root = self.rotateRight(root)
                elif root.left.height - root.right.height < -1:
                    if root.left.height == 1 and root.right.height == 3 and r == 2:
                        root.right = self.rotateRight(root.right)
                    root = self.rotateLeft(root)
            elif root.height > 2:
                root = self.rotateRight(root)
        elif root.height > 2:
            root = self.rotateLeft(root)
        return root

    def rotateLeft(self, root):
        """
        Left rotate the root tree
        """
        rr = root.right
        root.right = rr.left
        rr.left = root
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
        rr.height = 1 + max(self.getHeight(rr.left),
                            self.getHeight(rr.right))
        return rr

    def rotateRight(self, root):
        """
        Right rotate the root tree
        """
        rr = root.left
        root.left = rr.right
        rr.right = root
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
        rr.height = 1 + max(self.getHeight(rr.left),
                            self.getHeight(rr.right))
        return rr


root = TreeNode(val=20)
t = AVLTree()
# x = [i for i in range(2, 32)]
x = [10, 30, 25, 5, 40, 35, 45, 34, 11]
# x = [4,9,1,5,8,7]
for i in x:
    root = t.insert(root, i)
root = t.delete(root, 34)
root = t.delete(root, 45)
root = t.delete(root, 40)


def inorder(root, x=None):
    if x is None:
        x = []
    if root is None:
        return
    else:
        l = inorder(root.left, x)
        x.append(root.val)
        r = inorder(root.right, x)
        return x


# print(inorder(root))

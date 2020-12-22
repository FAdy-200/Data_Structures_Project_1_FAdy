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

    def insert(self, root, val,r=None):
        """
        Insert node with target value "val"
        """

        if not root:
            return TreeNode(val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
        if root.left is not None:
            if root.right is not None:
                if (root.left.height - root.right.height) > 1:
                    root = self.rotateRight(root)
                    # self.insert(r, root.val, r)
                elif root.left.height - root.right.height < -1:
                    root = self.rotateLeft(root)
                    # self.insert(r, root.val, r)
            elif root.height > 2:
                root = self.rotateRight(root)
                # self.insert(r, root.val, r)
        elif root.height > 2:
            root = self.rotateLeft(root)
            # self.insert(r, root.val, r)


        return root
    # def reOrder(self,root,node,):
    def delete(self, root, val):
        """
        Delete a node with target value "val"
        """

        if not root:
            return root
        elif val < root.val:
            root.left = self.delete(root.left, val)
        elif val > root.val:
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
        return rr


root = TreeNode(val=20)
t = AVLTree()
# x = [i for i in range(2, 8)]
x = [10,30,25,5,40,35,45]
# x = [4,9,1,5,8,7]
for i in x:
    if i == 7:
        print("Sd")
    root = t.insert(root, i, root)
# root = t.insert(root,34)
print()

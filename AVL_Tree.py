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

    def insert(self, root, val):
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

        ##############################################################
        ##                      YOUR CODE HERE                      ##
        ##############################################################

        return root

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

        ##############################################################
        ##                      YOUR CODE HERE                      ##
        ##############################################################

        return root

    def rotateLeft(self, root):
        """
        Left rotate the root tree
        """

        ##############################################################
        ##                      YOUR CODE HERE                      ##
        ##############################################################

    def rotateRight(self, root):
        """
        Right rotate the root tree
        """

        ##############################################################
        ##                      YOUR CODE HERE                      ##
        ##############################################################

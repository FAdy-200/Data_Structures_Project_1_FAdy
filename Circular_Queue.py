class CircularDeque:
    def __init__(self, capacity: int):
        """
        Initialize your data structure here.
        Set the maximum size of the deque to be capacity.
        """
        self.capacity = capacity
        self.deque = [None] * capacity
        self.rear = self.front = -1

    def insertRear(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque.
        Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.rear += 1
        self.rear = self.rear % self.capacity
        self.deque[self.rear] = value
        if self.rear == 0 and self.front < 0:
            self.front = 0
        return True

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque.
        Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.front -= 1
        if self.front < 0: self.front = self.capacity - 1
        if self.rear < 0: self.rear = self.capacity - 1
        self.deque[self.front] = value
        return True

    def deleteRear(self) -> bool:
        """
        Deletes an item from the rear of Deque.
        Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.rear -= 1
        if self.rear < 0: self.rear = self.capacity - 1
        if self.rear == self.front - 1:
            self.rear = -1
            self.front = -1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque.
        Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.front += 1
        self.front = self.front % self.capacity
        if (self.rear == self.front + 1) or (self.front == 0 and self.rear == self.capacity - 1):
            self.rear = -1
            self.front = -1
        return True

    def getRear(self):
        """
        Get the rear item from the deque.
        """
        if self.isEmpty():
            return None
        return self.deque[self.rear]

    def getFront(self):
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return None
        return self.deque[self.front]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return True if self.front == - 1 else False

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        rear = (self.rear + 1) % self.capacity  # a more delicate solution
        if rear == self.front:
            return True
        return False

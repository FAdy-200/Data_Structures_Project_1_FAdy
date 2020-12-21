class CircularDeque:
    def __init__(self, capacity: int):
        """
        Initialize your data structure here.
        Set the maximum size of the deque to be capacity.
        """
        self.capacity = capacity
        self.deque = [None] * capacity
        self.front = self.rear = -1

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque.
        Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.front += 1
        self.front = self.front % self.capacity
        self.deque[self.front] = value
        if self.front == 0 and self.rear < 0:
            self.rear = 0
        return True

    def insertRear(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque.
        Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.rear -= 1
        if self.rear < 0: self.rear = self.capacity - 1
        if self.front < 0: self.front = self.capacity - 1
        self.deque[self.rear] = value
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque.
        Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.front -= 1
        if self.front < 0: self.front = self.capacity - 1
        if self.front == self.rear - 1:
            self.front = -1
            self.rear = -1
        return True

    def deleteRear(self) -> bool:
        """
        Deletes an item from the rear of Deque.
        Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.rear += 1
        self.rear = self.rear % self.capacity
        if (self.front == self.rear + 1) or (self.rear == 0 and self.front == self.capacity - 1):
            self.front = -1
            self.rear = -1
        return True

    def getFront(self):
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return None
        return self.deque[self.front]

    def getRear(self):
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return None
        return self.deque[self.rear]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return True if self.front == - 1 else False

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        front = (self.front+1) % self.capacity
        if front == self.rear:
            return True
        return False

class CircularDeque:
    def __init__(self, capacity: int):
        """
        Initialize your data structure here.
        Set the maximum size of the deque to be capacity.
        """
        self.capacity = capacity
        self.deque = [0] * capacity
        self.front = self.rear = -1

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque.
        Return true if the operation is successful.
        """

    def insertRear(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque.
        Return true if the operation is successful.
        """

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque.
        Return true if the operation is successful.
        """

    def deleteRear(self) -> bool:
        """
        Deletes an item from the rear of Deque.
        Return true if the operation is successful.
        """

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return True if self.front == -1 else False

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        if (
            self.front == 0 and self.rear == self.capacity - 1
        ) or self.rear + 1 == self.front:
            return True
        return False


# capacity, value = 10, 1
# cq = CircularDeque(capacity)
# param_1 = cq.insertFront(value)
# param_2 = cq.insertRear(value)
# param_3 = cq.deleteFront()
# param_4 = cq.deleteRear()
# param_5 = cq.getFront()
# param_6 = cq.getRear()
# param_7 = cq.isEmpty()
# param_8 = cq.isFull()

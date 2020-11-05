"""This problem was asked by Apple.
Implement a queue using two stacks. 
Recall that a queue is a FIFO (first-in, first-out) 
data structure with the following methods: enqueue, which 
inserts an element into the queue, and dequeue, which removes it.
."""


class Queue:

    def __init__(self):
        """
        Initialize the bounding boxes

        Args:
            self: (todo): write your description
        """
        self.inbounds = []
        self.outbounds = []

    def enqueue(self, data):
        """
        Enqueue data to the queue.

        Args:
            self: (todo): write your description
            data: (array): write your description
        """
        self.inbounds.append(data)

    def dequeue(self):
        """
        Dequeue all the items from the queue.

        Args:
            self: (todo): write your description
        """
        if not self.outbounds:
            while self.inbounds:
                self.outbounds.append(self.inbounds.pop())
        return self.outbounds.pop()


# Testing the Queue.
queue = Queue()
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
print(queue.inbounds)

queue.dequeue()
print(queue.inbounds)
print(queue.outbounds)

queue.dequeue()
print(queue.inbounds)
print(queue.outbounds)

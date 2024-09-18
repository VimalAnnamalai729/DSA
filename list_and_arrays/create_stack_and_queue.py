# Creating Stack with List Operations.
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return not bool(self.stack)

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        if self.is_empty():
            raise IndexError("Can't pop the value from empty stack.")
        return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError("Can't peek an empty stack.")


s = Stack()
s.push(1)
s.push(3)
print(s.stack)
s.pop()
print(s.stack)
print(s.peek())


# Creating Stack with Linked List operations.from

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedStack:
    def __init__(self):
        pass


# Creating Queue

from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Can't pop in empty queue")
        return self.queue.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("Can't peek in empty queue")
        return self.queue[0]

    def size(self):
        return len(self.queue)


# Example usage:
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Front item:", q.peek())  # Output: Front item: 10
print("Dequeued:", q.dequeue())  # Output: Dequeued: 10
print("Queue size:", q.size())  # Output: Queue size: 2

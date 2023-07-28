class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
            return

        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None

        item = self.queue[self.front]

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        return item

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return

        index = self.front
        while True:
            print(self.queue[index], end=" ")
            if index == self.rear:
                break
            index = (index + 1) % self.size

        print()


# Test the CircularQueue implementation
if __name__ == "__main__":
    queue = CircularQueue(5)

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)

    queue.display()  

    queue.dequeue()
    queue.dequeue()

    queue.enqueue(6)
    queue.enqueue(7)

    queue.display()  

class CircularQueue:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.queue = [None] * self.capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, song):
        if self.is_full():
            self._resize()
        self.queue[self.rear] = song
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        print(f"{song} added to the queue")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        song = self.queue[self.front]
        self.queue[self.front] = None  # Clear the slot
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        print(f"{song} is removed from the queue")
        return song

    def _resize(self):
        new_capacity = self.capacity * 2
        new_queue = [None] * new_capacity
        for i in range(self.size):
            new_queue[i] = self.queue[(self.front + i) % self.capacity]
        self.queue = new_queue
        self.front = 0
        self.rear = self.size
        self.capacity = new_capacity

if __name__ == "__main__":
    n = int(input())
    queue = CircularQueue()
    
    for _ in range(n):
        command = input().split()
        operation = command[0]

        if operation == "ENQUEUE":
            song_name = " ".join(command[1:])
            queue.enqueue(song_name)
        elif operation == "DEQUEUE":
            queue.dequeue()

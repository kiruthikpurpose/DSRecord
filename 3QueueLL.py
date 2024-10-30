class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.qsize = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.qsize += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Stack Underflow")
        temp_node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.qsize -= 1
        return temp_node.data

    def front_peek(self):
        if self.is_empty():
            raise Exception("Stack Underflow")
        return self.front.data

    def is_empty(self):
        return self.front is None

    def size(self):
        return self.qsize

if __name__ == '__main__':

    n = int(input())
    queue = Queue()
    results = []

    for i in range(n):
        query = input().split()

        if query[0] == "enqueue":
            queue.enqueue(int(query[1]))

        elif query[0] == "dequeue":
            results.append(queue.dequeue())

        elif query[0] == "size":
            results.append(queue.size())

        elif query[0] == "front":
            results.append(queue.front_peek())

    for result in results:
        print(result)
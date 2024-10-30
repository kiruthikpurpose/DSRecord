class Deque:
    def __init__(self):
        self.values = []

    def append(self, value):
        self.values.append(value)

    def appendleft(self, value):
        self.values.insert(0, value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack Underflow.")
        return self.values.pop()

    def popleft(self):
        if self.is_empty():
            raise IndexError("Stack Underflow.")
        return self.values.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack Underflow.")
        return self.values[-1]

    def peekleft(self):
        if self.is_empty():
            raise IndexError("Stack Underflow.")
        return self.values[0]

    def is_empty(self):
        return len(self.values) == 0

    def size(self):
        return len(self.values)

if __name__ == '__main__':
    n = int(input())
    deque = Deque()
    results = []

    for i in range(n):
        query = input().split()

        if query[0] == "append":
            deque.append(int(query[1]))

        elif query[0] == "appendleft":
            deque.appendleft(int(query[1]))

        elif query[0] == "pop":
            results.append(deque.pop())

        elif query[0] == "popleft":
            results.append(deque.popleft())

        elif query[0] == "peek":
            results.append(deque.peek())

        elif query[0] == "peekleft":
            results.append(deque.peekleft())

        elif query[0] == "size":
            results.append(deque.size())

    for result in results:
        print(result)
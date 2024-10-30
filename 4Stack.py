class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.stack_size = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.stack_size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack Underflow")
        temp = self.top
        self.top = self.top.next
        self.stack_size -= 1
        return temp.data

    def peek(self):
        if self.is_empty():
            raise Exception("Stack Underflow")
        return self.top.data

    def is_empty(self):
        return self.top is None

    def size(self):
        return self.stack_size

if __name__ == '__main__':
    stack = Stack()
    results = []
    n = int(input())

    for i in range(n):
        query = input().split()
        
        if query[0] == "push":
            stack.push(int(query[1]))

        elif query[0] == "pop":
            results.append(stack.pop())

        elif query[0] == "peek":
            results.append(stack.peek())

        elif query[0] == "isEmpty":
            results.append(stack.is_empty())

        elif query[0] == "size":
            results.append(stack.size())

    for result in results:
        print(result)

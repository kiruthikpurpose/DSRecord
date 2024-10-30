class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, value):
        self.items.append(value)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        self.items.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0


if __name__ == "__main__":
    n = int(input())
    stack = Stack()
    results = []
    
    for _ in range(n):
        command = input().split()
        operation = command[0]
        
        if operation == "push":
            stack.push(int(command[1]))
        elif operation == "pop":
            stack.pop()
        elif operation == "peek":
            results.append(stack.peek())
    
    for result in results:
        print(result)

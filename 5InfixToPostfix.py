class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise Exception("Stack Underflow")
        temp = self.top
        self.top = self.top.next
        return temp.data

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

def precedence(operator):
    if operator == "+" or operator == "-":
        return 1
    if operator == "*" or operator == "/":
        return 2
    if operator == "^":
        return 3
    return 0

def infix_to_postfix(expression):
    stack = LinkedListStack()
    results = []

    for char in expression:
        if char.isalnum():
            results.append(char)
        elif char == "(":
            stack.push(char)
        elif char == ")":
            while not stack.is_empty() and stack.peek() != "(":
                results.append(stack.pop())
            stack.pop()
        else:
            while not stack.is_empty() and precedence(char) <= precedence(stack.peek()):
                results.append(stack.pop())
            stack.push(char)
    
    while not stack.is_empty():
        results.append(stack.pop())

    return ''.join(results)

if __name__ == '__main__':
    expression = input()
    print(infix_to_postfix(expression))

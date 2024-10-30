class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isEmpty():
            return None
        else:
            popped_element = self.top.data
            self.top = self.top.next
            return popped_element
        
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.top.data

def checkbalance(expr):
    stack = Stack()
    for char in expr:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            if stack.isEmpty():
                return False
            popped_element = stack.pop()
            if not((popped_element == "(" and char == ")") or (popped_element == "{" and char == "}") or (popped_element == "[" and char == "]")):
                return False
    return stack.isEmpty()
    
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        expr = input()
        print("Balanced" if checkbalance(expr) else "Not Balanced")
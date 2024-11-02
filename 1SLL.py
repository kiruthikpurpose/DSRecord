class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_after_node(self, prev_data, data):
        current = self.head
        while current:
            if current.data == prev_data:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def delete_tail(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

    def delete_node_with_value(self, value):
        if not self.head:
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next

    def print_list(self):
        current = self.head
        if not current:
            print("The list is empty.")
            return
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" ".join(elements))

def main():
    linked_list = LinkedList()
    n = int(input())
    for _ in range(n):
        operation = list(map(int, input().strip().split()))
        if operation[0] == 1:
            linked_list.insert_at_beginning(operation[1])
        elif operation[0] == 2:
            linked_list.insert_at_end(operation[1])
        elif operation[0] == 3:
            linked_list.insert_after_node(operation[1], operation[2])
        elif operation[0] == 4:
            linked_list.print_list()
        elif operation[0] == 5:
            linked_list.delete_tail()
        elif operation[0] == 6:
            linked_list.delete_node_with_value(operation[1])

if __name__ == "__main__":
    main()

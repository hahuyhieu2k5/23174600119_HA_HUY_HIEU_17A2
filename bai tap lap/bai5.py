class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Ngăn xếp rỗng")
            return None

    def is_empty(self):
        return len(self.items) == 0

    def count(self):
        return len(self.items)

# Ví dụ sử dụng
stack = Stack()
stack.push(2.1)
stack.push(3.9)
print(f"Số phần tử trong ngăn xếp: {stack.count()}")

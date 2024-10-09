class Stack:
    def __init__(self, size):
        """Khởi tạo ngăn xếp với kích thước tối đa."""
        self.size = size
        self.items = []

    def push(self, item):
        """Thêm phần tử vào ngăn xếp."""
        if not self.is_full():
            self.items.append(item)
        else:
            print("Ngăn xếp đã đầy")

    def pop(self):
        """Lấy phần tử trên cùng ra khỏi ngăn xếp."""
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Ngăn xếp rỗng")
            return None

    def is_empty(self):
        """Kiểm tra xem ngăn xếp có rỗng hay không."""
        return len(self.items) == 0

    def is_full(self):
        """Kiểm tra xem ngăn xếp có đầy hay không."""
        return len(self.items) == self.size

    def print_stack(self):
        """In nội dung ngăn xếp."""
        print("Nội dung ngăn xếp:", self.items)


if __name__ == "__main__":
    stack = Stack(6)
    stack.push(2.1)
    stack.push(3.9)
    stack.print_stack()  # In nội dung ngăn xếp

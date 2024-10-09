class Date:
    def __init__(self, day=27, month=10, year=2005):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year}"

class Employee:
    def __init__(self, name, birth_date, join_date):
        self.name = name
        self.birth_date = birth_date
        self.join_date = join_date

    def display(self):
        return f"{self.name}, {self.birth_date.display()}, {self.join_date.display()}"

# Ví dụ sử dụng
employees = [
    Employee("Nguyễn Tiến D", Date(), Date(15, 9, 2023)),
    Employee("Trịnh P", Date(19, 2, 2005), Date(15, 7, 2023))
]

print("Danh sách nhân viên:")
for emp in employees:
    print(emp.display())

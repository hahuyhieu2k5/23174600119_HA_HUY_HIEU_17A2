class Date:
    def __init__(self, day=27, month=10, year=2005):
        self.day, self.month, self.year = day, month, year

    def display(self):
        print(f"{self.day:02d}/{self.month:02d}/{self.year}")

    def next(self):
        days_in_month = [31, 28 + (self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0)), 31, 30] * 3
        self.day += 1
        if self.day > days_in_month[self.month - 1]:
            self.day, self.month = 1, self.month + 1
            if self.month > 12:
                self.month, self.year = 1, self.year + 1

# Ví dụ sử dụng
date = Date()
date.display()
date.next()
date.display()

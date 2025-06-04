import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []
        self.daily_limit = None

    def set_daily_limit(self, limit):
        if limit <= 0:
            print("한도는 0보다 커야 합니다.\n")
            return False
        self.daily_limit = limit
        print(f"일일 지출 한도를 {self.daily_limit}원으로 지정했습니다.\n")
        return True

    def add_expense(self, category, description, amount):
        current_date = datetime.date.today().isoformat()
        new_expense = Expense(current_date, category, description, amount)
        self.expenses.append(new_expense)

        total_today = sum(e.amount for e in self.expenses if e.date == current_date)
        print("지출이 등록되었습니다.\n")

        if self.daily_limit is not None and total_today > self.daily_limit:
            print(f"주의: 오늘 지출이 한도({self.daily_limit}원)를 넘었습니다. 현재 지출: {total_today}원\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출 금액: {total}원\n")

    def show_daily_limit(self):
        if self.daily_limit is None:
            print("일일 지출 한도가 설정되지 않았습니다.\n")
        else:
            print(f"현재 일일 지출 한도는 {self.daily_limit}원입니다.\n")

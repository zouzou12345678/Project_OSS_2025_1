from datetime import datetime, timedelta

class Budget:
    # ... 其他已有代码保持不变 ...

    def list_expenses_in_last_days(self, days_count):
        if not self.expenses:
            print("지출 기록이 없습니다.\n")
            return

        기준일 = datetime.today().date() - timedelta(days=days_count)
        대상_지출 = []

        for 지출 in self.expenses:
            지출일 = datetime.strptime(지출.date, "%Y-%m-%d").date()
            if 지출일 >= 기준일:
                대상_지출.append(지출)

        if not 대상_지출:
            print(f"\n최근 {days_count}일 간 지출 내역이 존재하지 않습니다.\n")
            return

        print(f"\n[최근 {days_count}일 지출 내역]")
        for 번호, 지출 in enumerate(대상_지출, start=1):
            print(f"{번호}. {지출}")
        print()

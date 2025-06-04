from budget import Budget

def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 내역 확인")
        print("3. 총 지출 확인")
        print("4. 최근 N일 지출 조회")
        print("5. 일일 지출 한도 설정")
        print("6. 설정된 일일 한도 확인")
        print("7. 종료")
        choice = input("선택 > ")

        if choice == "1":
            category = input("카테고리 입력: ")
            description = input("내용 입력: ")
            try:
                amount = int(input("금액 입력(원): "))
                if amount <= 0:
                    print("금액은 0보다 커야 합니다.\n")
                    continue
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_expense(category, description, amount)

        elif choice == "2":
            budget.list_expenses()

        elif choice == "3":
            budget.total_spent()

        elif choice == "4":
            try:
                days = int(input("최근 며칠간 지출을 보시겠습니까? 숫자 입력: "))
                if days <= 0:
                    print("숫자는 0보다 커야 합니다.\n")
                    continue
                budget.list_expenses_recent_days(days)
            except ValueError:
                print("잘못된 입력입니다.\n")

        elif choice == "5":
            try:
                limit = int(input("설정할 일일 지출 한도 입력(원): "))
                if limit <= 0:
                    print("한도는 0보다 커야 합니다.\n")
                    continue
                budget.set_daily_limit(limit)
            except ValueError:
                print("잘못된 입력입니다.\n")

        elif choice == "6":
            budget.show_daily_limit()

        elif choice == "7":
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")

if __name__ == "__main__":
    main()

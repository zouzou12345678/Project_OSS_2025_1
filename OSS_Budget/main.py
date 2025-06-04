def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 내역 보기")
        print("3. 총 지출 합계 보기")
        print("4. 최근 며칠간 지출 조회")  # 메뉴 문구 살짝 바꿈
        print("5. 종료")
        선택 = input("선택하세요 > ")

        if 선택 == "1":
            카테고리 = input("카테고리 입력 (예: 식비, 교통 등): ")
            설명 = input("설명 입력: ")
            try:
                금액 = int(input("금액(원) 입력: "))
            except ValueError:
                print("금액이 올바르지 않습니다.\n")
                continue
            budget.add_expense(카테고리, 설명, 금액)

        elif 선택 == "2":
            budget.list_expenses()

        elif 선택 == "3":
            budget.total_spent()

        elif 선택 == "4":
            try:
                기간 = int(input("조회할 기간(일수)을 입력하세요: "))
                if 기간 < 0:
                    print("0 이상의 숫자를 입력해 주세요.\n")
                    continue
                budget.list_expenses_in_last_days(기간)
            except ValueError:
                print("숫자만 입력해 주세요.\n")

        elif 선택 == "5":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")

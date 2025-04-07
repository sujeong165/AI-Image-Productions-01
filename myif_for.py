def print_cute_ascii_art(choice):
    """선택된 번호에 따라 아스키 아트를 출력하는 함수"""

    if choice == 1:
        # 1번 캐릭터 (고양이)
        print("""
        /\\_/\\
       ( o.o )
        > ^ <
        """)
    elif choice == 2:
        # 2번 캐릭터 (토끼)
        print("""
         (\\_/)
        (=';'=)
        (")_(")
        """)
    elif choice == 3:
        # 3번 캐릭터 (강아지)
        print("""
        __
        o-''|\\_____/)
         \\_/|_)     )
            \\  __  /
            (_/ (_/
        """)
    else:
        print("잘못 입력했습니다. 1, 2, 3 중 하나를 입력해주세요.")


# 메인 프로그램
print("그림 출력 프로그램")
print("-----------------")
print("1. 고양이")
print("2. 토끼")
print("3. 강아지")
print("-----------------")

# 총 5번 반복
for i in range(5):
    print(f"\n[{i+1}/5] 번째 선택")
    try:
        n = int(input("선택: "))
        print_cute_ascii_art(n)
    except ValueError:
        print("숫자를 입력해주세요.")

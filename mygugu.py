# 두 숫자를 입력받아 사칙연산을 수행하는 프로그램
# 구구단과 사칙연산 계산기

print("===== 파이썬 계산 프로그램 =====")
print("1. 사칙연산 계산기")
print("2. 구구단 출력")
choice = int(input("원하는 기능을 선택하세요(1 또는 2): "))

if choice == 1:
    # 사칙연산 계산기
    num1 = float(input("첫 번째 숫자를 입력하세요: "))
    num2 = float(input("두 번째 숫자를 입력하세요: "))
    
    print(f"\n===== 계산 결과 =====")
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} * {num2} = {num1 * num2}")
    
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print(f"{num1} / {num2} = 0으로 나눌 수 없습니다.")
        
elif choice == 2:
    # 구구단 출력
    dan = int(input("출력할 구구단의 단을 입력하세요(2~9): "))
    
    if 2 <= dan <= 9:
        print(f"\n===== {dan}단 =====")
        for i in range(1, 10):
            print(f"{dan} x {i} = {dan * i}")
    else:
        print("2부터 9 사이의 숫자를 입력해주세요.")
        
else:
    print("잘못된 선택입니다. 1 또는 2를 입력해주세요.")


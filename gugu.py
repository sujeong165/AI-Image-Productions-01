# 사용자로부터 숫자 입력 받기
dan = int(input("출력할 구구단의 단을 입력하세요: "))

# 입력받은 단의 구구단 출력하기
print(f"===== {dan}단 =====")
for i in range(1, 10):
    print(f"{dan} x {i} = {dan * i}")

# 만약에 입력받은 값 0 (0과 같다면) -> 결과 0
v = input("입력값: ")

# 숫자인지 문자인지 알고 싶을 경우에 사용하는 방법
print(type(v))
print("숫자로 변환")
v = int(v)
print(type(v))
#if v == 0: #문자열로 비교
if v == 0: #숫자로 비교
    print("0이다.")

# 입력받은 값 0 아님 -> 0 아님
if v != 0:
    print("0이 아니다.")

# 만약에 입력받은 값 0 (0과 같다면) -> 0 출력 , 아니면 0 아님 출력 (정석 방식)
if v == 0: #숫자로 비교
    print("0이다.")
else:
    print("0이 아니다.")
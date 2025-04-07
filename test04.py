#함수 만들기
def hello():
    print(("hello world"))

#함수 호출(실행)하기
hello()

def hello_name(name):
    print(f"안뇽 {name}아!")


#함수 호출(실행)하기
name = input("이름 입력: ")
hello_name(name)

def cal(n1, n2, op): #1, 2, + (이렇게입력)
    r = 0 # 결과값
    if op =="+":
        r = n1 + n2
    elif op == "-":
        r = n1 + n2
    else:
        print("잘못입력")
    return r #결과값을 전달

r = cal(2, 1, "+")
print(f"두수를 더한 값{r}")
cal(2, 1, "-")
print(f"두수를 뺀 값{r}")


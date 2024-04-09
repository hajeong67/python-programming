x = input("입력값 1: ")
y = input("입력값 2: ")
a = input("입력값 3: ")

try:
    x = float(x)
    y = float(y)
    a = float(a)

    if a == 0:
        raise ValueError("a는 0이 될 수 없습니다.")

    z = (pow(x, y)) * (pow(a, -2))
    print("x의 y 제곱한 값에 1/a를 제곱한 결과값은", z, "이다.")

except ValueError as ve:
    print("오류 발생:", ve)
except Exception as e:
    print("알 수 없는 오류 발생:", e)
# tanh 함수
# e의 x제곱을 계산하는 함수
def exp(x):
    return 2.718281828459045 ** x


# tanh 함수 정의
def tanh1(x):
    return (exp(x) - exp(-x)) / (exp(x) + exp(-x))


x1 = float(input("tanh 함수를 위한 입력값: "))
print("tanh 함수의 결과: ", tanh1(x1))


# ReLU 함수
def relu(y):
    if y > 0:
        return y
    else:
        return 0


y1 = float(input("relu 함수를 위한 입력값: "))
print("입력한 숫자에 대한 ReLU 결과: ", relu(y1))

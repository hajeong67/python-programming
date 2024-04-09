import numpy as np

def count_numbers(start_value, end_value, step=3):
    if start_value > end_value:
        print("시작 값은 끝 값보다 작아야 합니다.")
    else:
        numbers = np.arange(start_value, end_value + 1, step)
        for num in numbers:
            print(num)

try:
    while True:
        start_input = input("시작값을 입력하세요: ")
        end_input = input("끝값을 입력하세요: ")

        # start_input과 end_input이 비어있는 경우를 위한 기본값 설정
        start_input = start_input if start_input else '1'
        end_input = end_input if end_input else '1000'

        try:
            start = int(start_input)
            end = int(end_input)

            print("입력한 시작값:", start)
            print("입력한 끝값:", end)
            break
        except ValueError:
            print("시작값과 끝값은 정수를 입력해야 합니다. 다시 시도해주세요.")

    count_numbers(start, end)  # step은 기본값 3 이용
except ValueError as e:
    print("오류 발생:", e)

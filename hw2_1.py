def re_search_ex1(*args):
    total = 0

    for arg in args:
        # 인수가 정수일 경우
        if isinstance(arg, int):
            total += arg
        # 인수가 리스트나 튜플일 경우
        elif isinstance(arg, (list, tuple)):
            for item in arg:
                # 리스트나 튜플 내부의 요소가 정수일 경우
                if isinstance(item, int):
                    total += item

    # 결과를 파일에 저장
    try:
        with open("homework2.txt", "w") as file:
            file.write(str(total))
    except Exception as e:
        print("파일 저장 중 오류가 발생했습니다: ", e)
        return 0

    return total  # 총 합 리턴


# 사용자 입력 받기
# 입력시에 숫자, 리스트, 튜플 중 하나씩만 입력 가능하고, 엔터를 누르면 또 다시 3개 중 하나 입력 가능하다.
# 입력을 끝내려면 'end'를 입력하면 된다.
def get_user_input():
    inputs = []
    print("입력을 종료하려면 'end'을 입력하세요.")
    while True:
        user_input = input("정수, 리스트, 튜플 중 하나를 입력하세요 (예: 5, [1, 2], (3, 4)): ")
        if user_input.lower() == 'end':
            break
        try:
            evaluated_input = eval(user_input)
            if isinstance(evaluated_input, (int, list, tuple)):
                inputs.append(evaluated_input)
            else:
                print("정수, 리스트, 튜플만 입력 가능합니다.")
        except:
            print("유효하지 않은 입력입니다.")

    return inputs


# 사용자 입력을 기반으로 함수 호출
user_inputs = get_user_input()
result = re_search_ex1(*user_inputs)
print("총 합: ", result)

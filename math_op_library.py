class MathOp:
    def input_numbers(self, operation):
        while True:
            inputs = input(f"{operation} 연산을 위한 숫자를 입력해주세요. : ")
            try:
                numbers = [float(num) for num in inputs.split(" ")]
                if operation == "div" and 0 in numbers[1:]:
                    raise ValueError("0으로 나눌 수 없습니다. 숫자를 다시 입력해주세요.")
                return numbers
            except ValueError as e:
                print(f"유효하지 않은 입력입니다. Error: {e}")

    def addOp(self, numbers):
        return sum(numbers)

    def subOp(self, numbers):
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
        return result

    def mulOp(self, numbers):
        result = 1
        for num in numbers:
            result *= num
        return result

    def divOp(self, numbers):
        result = numbers[0]
        for num in numbers[1:]:
            if num == 0:
                continue
            result /= num
        return result

    def remOp(self, a, b):
        # % 연산자 이용하지 않고 나머지 연산하기
        quotient = a / b
        remainder = a - (b * int(quotient))
        return remainder

    def operate(self):
        operation = input("연산을 선택해주세요. add, sub, mul, div, rem: ").lower()
        if operation == "rem":
            a = float(input("dividend: "))
            b = float(input("divisor: "))
            while b == 0:
                print("0으로 나눌 수 없습니다. divisor를 다시 입력해주세요.")
                b = float(input("divisor: "))
            result = self.remOp(a, b)
        else:
            numbers = self.input_numbers(operation)
            if operation == "add":
                result = self.addOp(numbers)
            elif operation == "sub":
                result = self.subOp(numbers)
            elif operation == "mul":
                result = self.mulOp(numbers)
            elif operation == "div":
                result = self.divOp(numbers)
            else:
                raise ValueError("유효하지 않은 입력입니다.")
        print("Result:", result)

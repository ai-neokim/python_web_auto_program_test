###   사칙연산 클래스 만들기   ###

class FourCal:
    def __init__(self, first, second) :
        self.first = first
        self.second = second
    def setdata(self, first, second) :
        self.first = first
        self.second = second
    def add(self) :
        result = self.first + self.second
        return result
    def mul(self) :
        result = self.first * self.second
        return result
    def sub(self) :
        result = self.first - self.second
        return result
    def div(self) :
        result = self.first / self.second
        return result


# 클래스의 인스턴스 생성
calculator = FourCal(10, 5)

# 덧셈 수행
result_add = calculator.add()
print("덧셈 결과:", result_add)

# 곱셈 수행
result_mul = calculator.mul()
print("곱셈 결과:", result_mul)

# 뺄셈 수행
result_sub = calculator.sub()
print("뺄셈 결과:", result_sub)

# 나눗셈 수행
result_div = calculator.div()
print("나눗셈 결과:", result_div)
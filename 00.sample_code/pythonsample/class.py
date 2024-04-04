
###  클래스 잘 모르겠다 진짜 !!  ###

#전역변수 result1 / result2 를 초기화 
result1 = 0
result2 = 0

def add1(num):
    global result1 #result1을 전역변수로 사용하기 위해 global 키워드 사용 
    result1 += num #전역변수 result1 에 num 을 더하여 갱신  
    return result1

def add2(num):
    global result2 #result2을 전역변수로 사용하기 위해 global 키워드 사용 
    result2 += num #전역변수 result2 에 num 을 더하여 갱신  
    return result2


print(add1(3)) # add1 함수 호출하여 num에 3 전달, result1에 3을 더한 후 반환하여 출력 (결과: 3)
print(add1(4)) # add1 함수 호출하여 num에 4 전달, result1에 4을 더한 후 반환하여 출력 (결과: 7)
print(add2(3)) # add2 함수 호출하여 num에 3 전달, result2에 3을 더한 후 반환하여 출력 (결과: 3)
print(add2(7)) # add2 함수 호출하여 num에 7 전달, result2에 7을 더한 후 반환하여 출력 (결과: 10)


""" Calculator 클래스는 계산기의 기능은 모델링 한 것 
- __init__ 메서드 : 클래스의 인스턴스를 초기화 , 아래 코드에서 self.result(계산 결과 저장) 멤버 변수를 0으로 초기화 
- add 메서드 : 매개변수 num 을 인스턴스 self.result 에 더하고 결과 반환 """



# Calculator 클래스의 인스턴스 생성 시 result 멤버 변수 초기화 
class Calculator:
    def __init__(self):
        self.result = 0


# Calculator 클래스의 add 메서드 호출 시 num을 result에 더하여 갱신 
    def add(self, num):
        self.result += num
        return self.result
    
cal1 = Calculator() # Calculator 클래스의 인스턴스 cal1 생성
cal2 = Calculator() # Calculator 클래스의 인스턴스 cal2 생성

###################################################################################################

###   사칙연산 클래스 만들기   ###

class FourCal:
    def setdata(self,first,second):
        self.first = first
        self.second = second

a = FourCal()
a.setdata(4,2)



#자료형 (숫자, 문자, 불리)

print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

#문자형

print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)

#불리 (참/ 거짓)

print(5>10)
print(5<10)
print(True)
print(False)
print(not True) #not 뒤에 있는 값의 반대를 출력
print(not False)
print(not (5>10))

#변수 (반려동물 소개) 
#변수 = 값을 저장하는 

animal = "강아지"
name = "단지"
age = 11
hobby = "먹기"
is_adult = age >= 3

print("우리집 "+ animal + "의 이름은 "+ name + "예요")
print(name + "는 " + str(age) + "살이고, " + hobby + "를 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))  #정수형은 문자형처럼 보이게 앞에 str 붙이기 

print("우리집 " , animal, "의 이름은 " , name, "예요")
print(name,"는 " , age , "살이고, " , hobby, "를 아주 좋아해요")
print(name, "는 어른일까요? " , is_adult)  #+가 아닌 ,로 표기할 때는 정수 앞에 str 안 붙여도 됨 / , 로 들어갈 경우 띄어쓰기가 들어가서 "단지 는" 이렇게 보여짐

""" Q ) 변수를 이용하여 다음 문장 출력 
변수명 : station 

변수값 : 사당, 신도림, 인천공항 순서대로 입력 

출력 문장 : XX행 열차가 들어오고 있습니다. """

station1 = "사당"
print(station1 , "행 열차가 들어오고 있습니다.")

station2 = "신도림"
print(station2 , "행 열차가 들어오고 있습니다.")

station3 = "인천공항"
print(station3 , "행 열차가 들어오고 있습니다.")


#연산자 

print(1+1) #2
print(3-2) #1
print(5*2) #10
print(6/3) #2 

print(2**3) #8
print(5%3) #나머지 구하기 2
print(5//3) #몫 구하기 1

print(10>3) #True
print(4>=7) #False
print(10>=3) #True

print(3==3) #앞뒤 값이 같다 True
print(4==2) #False
print(3+4==7) #True

print(1 != 3) #앞뒤 값이 다르다 !=not True
print(not (1 != 3)) #False


# A and B / A,B 값이 다 True 여야 True / and = & 

print((3>0) and (3<5)) #True
print((3>0) & (3<5)) #True 

# A or B / A,B 값 중 하나만 True 여도 True / or = | (ctrl + \)

print((3>0) or (3>5)) #True
print((3>0) | (3>5)) #True #



print(5>4>3) #True
print(5>4>7) #False

print(2+3*4) #14
print((2+3)*4) #20

number = 2+3*4 #14
print(number)

number = number +2 #16
print(number)

number += 2 #18
print(number)

number *= 2 #36
print(number)

number /= 2 #18
print(number)

number -= 2 #16
print(number)

number %= 5 #1
print(number)

#숫차 처리 함수 

print(abs(-5)) #5 / 절대값
print(pow(4, 2)) #4^2 = 4*4 = 16 / 앞 숫자를 뒷 숫자 만큼 곱함 
print(max(5, 12)) #12 / 최대값 
print(min(5, 12)) #5 / 최소값
print(round(3.14)) #3 / 반올림
print(round(4.99)) #5 / 반올림

from math import * #math 라이브러리 안에 모든 import 값을 이용하겠다는 선언 
print(floor(4.99)) #내림 / 4
print(ceil(3.14)) #올림 / 4
print(sqrt(16)) #제곱근 / 4


#랜덤 함수
from random import * #random 라이브러리 안에 모든 import 값을 이용하겠다는 선언 
print(random()) #0.0 ~ 1.0. 미만의 임의의 값을 생성 , 매번 실행 마다 값이 달라짐 
print(random()* 10) #0.0 ~ 10.0 미만의 임의의 값을 생성 , 매번 실행 마다 값이 달라짐 


#정수 랜덤 
print(int(random()*10)) #0 ~ 10 미만의 임의의 값을 생성 , 매번 실행 마다 값이 달라짐 
print(int(random()*10)) #0 ~ 10 미만의 임의의 값을 생성 , 매번 실행 마다 값이 달라짐 
print(int(random()*10)) #0 ~ 10 미만의 임의의 값을 생성 , 매번 실행 마다 값이 달라짐 

#0 제외 랜덤
print(int(random()*10) + 1) #1 ~ 10 이하의 임의의 값을 생성 , 매번 실행 마다 값이 달라짐 
print(int(random()*10) + 1) #1 ~ 10 이하의 임의의 값을 생성 , 매번 실행 마다 값이 달라짐
print(int(random()*10) + 1) #1 ~ 10 이하의 임의의 값을 생성 , 매번 실행 마다 값이 달라짐
print(int(random()*10) + 1) #1 ~ 10 이하의 임의의 값을 생성 , 매번 실행 마다 값이 달라짐
print(int(random()*10) + 1) #1 ~ 10 이하의 임의의 값을 생성 , 매번 실행 마다 값이 달라짐
print(int(random()*10) + 1) #1 ~ 10 이하의 임의의 값을 생성 , 매번 실행 마다 값이 달라짐

#로또 랜덤 
print(int(random()*45) + 1) #1 ~ 45 이하의 임의의 값을 생성 , 매번 실행 마다 값이 달라짐
print(int(random()*45) + 1) #1 ~ 45 이하의 임의의 값을 생성 , 매번 실행 마다 값이 달라짐
print(int(random()*45) + 1) #1 ~ 45 이하의 임의의 값을 생성 , 매번 실행 마다 값이 달라짐
print(int(random()*45) + 1) #1 ~ 45 이하의 임의의 값을 생성 , 매번 실행 마다 값이 달라짐
print(int(random()*45) + 1) #1 ~ 45 이하의 임의의 값을 생성 , 매번 실행 마다 값이 달라짐
print(int(random()*45) + 1) #1 ~ 45 이하의 임의의 값을 생성 , 매번 실행 마다 값이 달라짐

#쉽게 작성 방법 (미만)
print(randrange(1,46)) #1 ~ 46 미만의 임의의 값 생성
print(randrange(1,46)) #1 ~ 46 미만의 임의의 값 생성 
print(randrange(1,46)) #1 ~ 46 미만의 임의의 값 생성 
print(randrange(1,46)) #1 ~ 46 미만의 임의의 값 생성 
print(randrange(1,46)) #1 ~ 46 미만의 임의의 값 생성 
print(randrange(1,46)) #1 ~ 46 미만의 임의의 값 생성 

#쉽게 작성 방법 (이하)
print(randint(1,45)) #1 ~ 45 이아희 임의의 값 생성 
print(randint(1,45)) #1 ~ 45 이아희 임의의 값 생성
print(randint(1,45)) #1 ~ 45 이아희 임의의 값 생성
print(randint(1,45)) #1 ~ 45 이아희 임의의 값 생성
print(randint(1,45)) #1 ~ 45 이아희 임의의 값 생성
print(randint(1,45)) #1 ~ 45 이아희 임의의 값 생성

""" Q) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다. 
월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다. 
아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오

조건1 : 랜덤으로 날짜를 뽑아야 함 
조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함 
조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외 


(출력문 예제)
오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다. """ 


#유튜브 답변 

from random import *
date = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월" , date ,"일로 선정되었습니다.")


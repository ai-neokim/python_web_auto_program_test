#문자열 

sentence = '나는 소년입니다.'
print(sentence)

sentence2 = "파이썬은 쉬워요"
print(sentence2)

sentence3 = """
나는 소년입니다.
파이썬은 쉬워요 
"""
print(sentence3)

#슬라이싱 / python 은 숫자를 0부터 셈 

jumin = "981208-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) #0부터 2직전까지 (0,1)
print("월 : " + jumin[2:4])
print("일 : "+ jumin[4:6])

print("생년월일 : " + jumin[:6]) #처음부터 6직전까지 
print("뒤 7자리 : " + jumin[7:]) #7부터 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) #맨 뒤에서 부터 숫자를 세면 -1 부터 시작 / -7부터 끝까지 

#문자열 처리 함수 

python = "Python is Amazing"
print(python.lower()) #모든 문자를 소문자로 
print(python.upper()) #모든 문자를 대문자로 
print(python[0].isupper()) #대괄호 안에 있는 문자가 대문자 인지 구별 / True
print(len(python)) #python 의 문자 길이(갯수) (띄어쓰기도 포함)

#특정 글자를 다른 글자로 변경하고 싶을 때
print(python.replace("Python", "Java"))


#python 변수에서 n 이라는 글자가 몇번재 인지 알려줌
index = python.index("n")
print(index)

#앞에 index 값은 5, 5 +1 = 6 번째 이후로 부터 n 글자가 몇번째 인지 
index = python.index("n", index + 1)
print(index)

#index 와 동일하게 글자 위치 알려 줌
print(python.find("n"))

#python 변수에 없는 값을 대입 하면 -1 을 반환 해줌 
print(python.find("Java"))


#python 변수에 없는 값을 대입하면 오류라고 뜨고 프로그램 종료 해버림 
#뒤에 다른 선언 함수가 있어도 더 이상 출력되지 않고 종료 

""" print(python.index("Java")) """

#python 이란 변수에서 n 이 총 몇번 등장하는지 
print(python.count("n"))


#문자열 포맷

#방법1 /  % 뒤의 값을 %()에 넣음
print("나는 %d살 입니다." %20) #d 는 정수값만 
print("나는 %s 을 좋아해요" %"파이썬") #s 는 문자열만  
print("Apple 은 %c 로 시작해요" % "A") #c 는 한 글자만 받음 

# 정수형도 %s 로 넣어도 됨

# % 값이 복수개 일 때 
print("나는 %s 색과 %s 색을 좋아해요" % ("파란" , "분홍")) 

#방법2 / format 사용 
print("나는 {} 살 입니다." . format(20))
print("나는 {}색과  {}색을 좋아해요" . format("파란", " 분홍"))
print("나는 {0}색과  {1}색을 좋아해요" . format("파란", " 분홍"))
print("나는 {1}색과  {0}색을 좋아해요" . format("파란", " 분홍"))

#방법3 / format 에 변수 선언
print("나는 {age}살이며,  {color}색을 좋아해요" . format(age = 20, color = "분홍"))
print("나는 {age}살이며,  {color}색을 좋아해요" . format(color = "분홍" , age = 20))

#방법4 / (v3.6이상~) / 직접변수 사용 
age = 20
color = "분홍"
print(f"나는 {age}살이며, {color}색을 좋아해요")

#탈출 문자 

#\n 줄바꿈 
print("백문이 불여일견 \n백견이 불여일타") 

#print 문 안에 큰따옴표 출력 방법
#큰 따옴표 앞쪽에 역슬래시 (작은 따옴표도 가능)
print("저는 \"나누리\" 입니다.")

# \\ : 문장 내에서 하나의 슬래시로 변경 됨
#print("C:\Users\Core\Norizzang\NORIzzang") > 이렇게 출력하면 오류 남 
print("C:\\Users\\Core\\Norizzang\\NORIzzang")  #슬래시를 두개 하면 정상 출력 됨

#\r 커서를 맨 앞으로 이동 
print("Red Apple\rPine")  #PineApple

#\b 백스페이스 역할 (한 글자 삭제)
print("Redd\bApple") #RedApple

#\t 탭 
print("Red\tApple") #Red  Apple

"""Q) 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오 

http://naver.com
규칙1 : http:// 부분은 제외 => naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성

예) 생성된 비밀번호 : nav51!"""

# adress = "http://naver.com"
# print(adress[7:11])
# print(len(adress[7:11]))
# print((adress[7:11]).count("e"))
# print("!")

#선생님 답변

url = "http://naver.com"
my_str = url.replace("http://","") #규칙1
print(my_str)
my_str = my_str[:my_str.index(".")] #규칙 2 , my_str[0:5] -> 0~5 직전까지 
print(my_str)

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) +"!"
print("{0} 의 비밀번호는 {1} 입니다." .format(url,password))


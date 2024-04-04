#리스트 []

#지하철 칸 별로 10명, 20명, 30명 

subway1 = 10
subway2 = 20
subway3 = 30

subway = [10,20,30] #위에 따로 따로 변수 지정한 것과 같음
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

#조세호가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호")) #1

#하하가 다음 정류장에서 다음 칸에 탐
subway.append("하하") #append 를 하면 맨 뒤에 붙음
print(subway)

#정형돈을 유재석과 조세호 사이에 태워라 
subway.insert(1, "정형돈") #위치를 1번째로 한다는 말
print(subway)

#지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop()) #하하 제외
print(subway)

print(subway.pop()) #박명수 제외
print(subway)

print(subway.pop()) #조세호 제외
print(subway)

#같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석") #맨 뒤에 유재석 추가 
print(subway)
print(subway.count("유재석")) 

#순서 정렬 
num_list = [5,2,4,3,1]
num_list.sort() #순서대로 정렬 하는 거  
print(num_list)

#순서 뒤집기 
num_list.reverse() #순서 뒤집기 
print(num_list)

#모두 지우기 
num_list.clear() #빈 리스트 
print(num_list)

#다양한 자료형과 함께 사용
num_list = [5,2,4,3,1]
mix_list = ["조세호", 20, True]

num_list.extend(mix_list) #리스트 확장, 하나의 리스트로 합치는 것도 가능
print(num_list)

#사전 
cabinet = {3:"유재석", 100:"김태호"} #열쇠키가3이고 유재석이 쓰는 중 
print(cabinet[3]) #유재석
print(cabinet[100]) #김태호

print(cabinet.get(3)) #유재석
print(cabinet.get(100)) #김태호

#할당이 안된 키를 선언할 때 
#>> print(cabinet[5]) #KeyError: 5 라고 뜨며 프로그램 종료 됨 다음 hi 호출 되지 않음
print("hi")

print(cabinet.get(5)) #None 이라고 뜨며 프로그램 종료되지 않고 뒤에 hi 호출 됨
print("hi")

#값을 확인 하는 방법
print(3 in cabinet) #3이라는 키가 캐비닛이라는 변수에 있는지 ? #True
print(5 in cabinet) #False

#새 손님
cabinet = {"A-3": "유재석", "B-100" : "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

print(cabinet)
cabinet["A-3"] = "김종국" #A-3을 유재석 > 김종국으로 값을 변경 
cabinet["c-20"] = "조세호" #신규 손님
print(cabinet)

#간 손님 
del cabinet["A-3"] #지울 값의 키를 넣어주면 값이 지워짐 
print(cabinet)

#Key 만 정보 출력 
print(cabinet.keys())

#value 만 정보 출력 
print(cabinet.values())

#Kye , Value 쌍으로 출력 
print(cabinet.items())

#목욕탕 폐점 
cabinet.clear() #모든 값을 다 지울 수 있음 
print(cabinet) 

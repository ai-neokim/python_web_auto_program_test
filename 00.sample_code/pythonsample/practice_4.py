#튜플 
#리스트와 다르게 내용 변경이나 추가를 할 수 없지만 속도가 리스트보다 빠름 
#변경 되지 않는 목록을 사용할 때 편리 

menu = ("돈까스" , "치즈까스") 
print(menu[0])
print(menu[1])

#>>> menu.add("생선까스") 
#'tuple' object has no attribute 'add' 튜플은 add 불가하다는 오류 문구 

name = "김종국"
age = 20
hobby = "코딩"
print(name,age,hobby)

(name,age,hobby) = ("김종국", 20, "코딩") 
print(name,age,hobby)

#set (집합)
#중복 안 됨, 순서 없음

my_set = {1,2,3,3,3}
print(my_set) #1,2,3


java = {"유재석", "김태호", "조세호"}
python = {"유재석","박명수"} 
# python = set(["유재석", "박명수"]) 이렇게 적어도 되는데 이유는 모르겠음 

#교집합 
#java 와 python 모두 할 수 있는 개발자
print(java & python) 
print(java.intersection(python))

#합집합
#java 나 python 둘 중 하나 가능한 개발자 

#출력 시 순서가 아무렇게나 나옴 
print(java | python) 
print(java.union(python))

#차집합 
#java는 할 줄 알지만 python 은 할 줄 모르는 개발자
print(java - python)
print(java.difference(python))

#python 을 할 줄 아는 사람이 늘어남 
python.add("김태호")
print(python)

#java 를 까먹어서 대상 제외 
java.remove("김태호")
print(java)
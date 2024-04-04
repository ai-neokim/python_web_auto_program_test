# 쓰레드 라이브러리
import threading

# 시간 설정 함수
def my_func():
    print('함수 실행')
    threading.Timer(1,my_func).start()

# 시간함수 호출
my_func()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time      # 시간 지연을 위한 time 라이브러리
import pyautogui # 키보드와 마우스의 행동을 자동으로 움직이는 라이브러리
import pyperclip # 클립보드를 사용하기 위한 라이브러리
                 # pyautogui 라이브러리는 한글 입력을 직접 지원하지 않으므로, 클립보드에 원하는 한글 텍스트를 저장한 뒤 꺼내서 사용함



# 네이버 브라우저 호출하기
url = "https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/"
browser = webdriver.Chrome("C:\workplace\Python\chromedriver_win32\chromedriver.exe")
browser.implicitly_wait(10)
browser.maximize_window()
browser.get(url)

# 아이디 입력창
id = browser.find_element(By.CSS_SELECTOR,"#id")
id.click()
pyperclip.copy("")           # 네이버 이메일을 입력합니다.(필수 입력 사항)
pyautogui.hotkey("ctrl","v")
time.sleep(2)

# 비밀번호 입력창
pw = browser.find_element(By.CSS_SELECTOR,"#pw")
pw.click()
pyperclip.copy("")          # 네이버 패스워드를 입력합니다.(필수 입력 사항)
pyautogui.hotkey("ctrl","v")
time.sleep(2)

# 로그인 버튼
login_btn = browser.find_element(By.CSS_SELECTOR,"#log\.login")
login_btn.click()
time.sleep(2)

##################################
######### 브라우저 나타내기 #######
##################################

# 뉴스탭 이동하기
news_btn_1 = browser.find_element(By.LINK_TEXT,"뉴스")
news_btn_1.click()
#time.sleep(2)

# 마우스 현재 위치 출력
print('마우스 사이즈 출력')
print(pyautogui.size())
time.sleep(1)
print('마우스 위치 출력')
time.sleep(1)
print(pyautogui.position())
time.sleep(1)

pyautogui.moveTo(458,243)
pyautogui.click()
time.sleep(20)

# 뉴스탭 이동하기
#news_btn_2 = browser.find_element(By.CSS_SELECTOR,"a.lnb_menu.nclicks(lnb.eco)")
#news_btn_2.click()
#time.sleep(2)

###############################
####### 화면 좌표값 확인 #######
###############################

# print('test')
# while True:
#     print(pyautogui.position())
#     time.sleep(0.1)

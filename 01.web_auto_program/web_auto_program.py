# mysql 라이브러리
import pymysql 

# mail 전송 라이브러리
import smtplib
from email.message import EmailMessage

# 셀레니움 라이브러리
from selenium import webdriver # 셀레니움 웹드라이버
from selenium.webdriver.common.by import By
import time      # 시간 지연을 위한 time 라이브러리
import pyautogui # 키보드와 마우스의 행동을 자동으로 움직이는 라이브러리
import pyperclip # 클립보드를 사용하기 위한 라이브러리
                 # pyautogui 라이브러리는 한글 입력을 직접 지원하지 않으므로, 클립보드에 원하는 한글 텍스트를 저장한 뒤 꺼내서 사용함

# 시간 라이브러리
import time
from datetime import datetime

# 운영체제 라이브러리
import os

# ini 파일 읽기
import configparser

# 쓰레드 라이브러리
import threading

# DB 데이터 전역변수
global error_cd 
global error_msg

global send_id
global recv_id
global email_title
global email_contents
global send_pw

#전역변수 초기화
#[scrpt_1]
scrpt_1_step_basic_cd_1 = '0'
scrpt_1_step_basic_cd_2 = '0'
scrpt_1_step_basic_cd_3 = '0'
scrpt_1_step_detail_cd_1 = '0'
scrpt_1_step_detail_cd_2 = '0'
scrpt_1_step_detail_cd_3 = '0'

#[scrpt_2]
scrpt_2_step_basic_cd_1 = '0'
scrpt_2_step_basic_cd_2 = '0'
scrpt_2_step_basic_cd_3 = '0'
scrpt_2_step_detail_cd_1 = '0'
scrpt_2_step_detail_cd_2 = '0'
scrpt_2_step_detail_cd_3 = '0'

#[scrpt_3]
scrpt_3_step_basic_cd_1 = '0'
scrpt_3_step_basic_cd_2 = '0'
scrpt_3_step_basic_cd_3 = '0'
scrpt_3_step_detail_cd_1 = '0'
scrpt_3_step_detail_cd_2 = '0'
scrpt_3_step_detail_cd_3 = '0'

# DB 데이터 전역변수 초기화
error_cd = '0'
error_msg = ''

send_id = ''
send_pw = ''
recv_id = ''
email_title = ''
email_contents = ''

def get_config_time():
    config_read = configparser.ConfigParser()
    root_path = os.path.abspath("./")
    config_read.read(root_path + '/config.ini',encoding='utf-8')    
    
    sleep_time = config_read.get('time','sleep_time')
    start_time = config_read.get('time','start_time')
    end_time = config_read.get('time','end_time')
    repeat_yn = config_read.get('time','repeat_yn')

    return sleep_time,start_time,end_time,repeat_yn


def get_config_script_1():

    config_read = configparser.ConfigParser()
    root_path = os.path.abspath("./")
    config_read.read(root_path + '/config.ini',encoding='utf-8')    
    
    scrpt_1_step_basic_cd_1 = config_read.get('scrpt_1','scrpt_1_step_basic_cd_1')
    scrpt_1_step_basic_cd_2 = config_read.get('scrpt_1','scrpt_1_step_basic_cd_2')
    scrpt_1_step_basic_cd_3 = config_read.get('scrpt_1','scrpt_1_step_basic_cd_3')

    scrpt_1_step_detail_cd_1 = config_read.get('scrpt_1','scrpt_1_step_detail_cd_1')
    scrpt_1_step_detail_cd_2 = config_read.get('scrpt_1','scrpt_1_step_detail_cd_2')
    scrpt_1_step_detail_cd_3 = config_read.get('scrpt_1','scrpt_1_step_detail_cd_3')

    print('[scrpt_1_step_basic_cd_1]' + str(scrpt_1_step_basic_cd_1))
    print('[scrpt_1_step_basic_cd_2]' + str(scrpt_1_step_basic_cd_2))
    print('[scrpt_1_step_basic_cd_3]' + str(scrpt_1_step_basic_cd_3))
    print('[scrpt_1_step_detail_cd_1]' + str(scrpt_1_step_detail_cd_1))
    print('[scrpt_1_step_detail_cd_2]' + str(scrpt_1_step_detail_cd_2))
    print('[scrpt_1_step_detail_cd_3]' + str(scrpt_1_step_detail_cd_3))

    return scrpt_1_step_basic_cd_1,scrpt_1_step_detail_cd_1,scrpt_1_step_basic_cd_2,scrpt_1_step_detail_cd_2,scrpt_1_step_basic_cd_3,scrpt_1_step_detail_cd_3

def get_config_script_2():

    config_read = configparser.ConfigParser()
    root_path = os.path.abspath("./")
    config_read.read(root_path + '/config.ini',encoding='utf-8')    
    
    scrpt_2_step_basic_cd_1 = config_read.get('scrpt_2','scrpt_2_step_basic_cd_1')
    scrpt_2_step_basic_cd_2 = config_read.get('scrpt_2','scrpt_2_step_basic_cd_2')
    scrpt_2_step_basic_cd_3 = config_read.get('scrpt_2','scrpt_2_step_basic_cd_3')

    scrpt_2_step_detail_cd_1 = config_read.get('scrpt_2','scrpt_2_step_detail_cd_1')
    scrpt_2_step_detail_cd_2 = config_read.get('scrpt_2','scrpt_2_step_detail_cd_2')
    scrpt_2_step_detail_cd_3 = config_read.get('scrpt_2','scrpt_2_step_detail_cd_3')

    print('[scrpt_2_step_basic_cd_1]' + str(scrpt_2_step_basic_cd_1))
    print('[scrpt_2_step_basic_cd_2]' + str(scrpt_2_step_basic_cd_2))
    print('[scrpt_2_step_basic_cd_3]' + str(scrpt_2_step_basic_cd_3))
    print('[scrpt_2_step_detail_cd_1]' + str(scrpt_2_step_detail_cd_1))
    print('[scrpt_2_step_detail_cd_2]' + str(scrpt_2_step_detail_cd_2))
    print('[scrpt_2_step_detail_cd_3]' + str(scrpt_2_step_detail_cd_3))

    return scrpt_2_step_basic_cd_1,scrpt_2_step_detail_cd_1,scrpt_2_step_basic_cd_2,scrpt_2_step_detail_cd_2,scrpt_2_step_basic_cd_3,scrpt_2_step_detail_cd_3

def get_config_script_3():

    config_read = configparser.ConfigParser()
    root_path = os.path.abspath("./")
    config_read.read(root_path + '/config.ini',encoding='utf-8')    
    
    scrpt_3_step_basic_cd_1 = config_read.get('scrpt_3','scrpt_3_step_basic_cd_1')
    scrpt_3_step_basic_cd_2 = config_read.get('scrpt_3','scrpt_3_step_basic_cd_2')
    scrpt_3_step_basic_cd_3 = config_read.get('scrpt_3','scrpt_3_step_basic_cd_3')

    scrpt_3_step_detail_cd_1 = config_read.get('scrpt_3','scrpt_3_step_detail_cd_1')
    scrpt_3_step_detail_cd_2 = config_read.get('scrpt_3','scrpt_3_step_detail_cd_2')
    scrpt_3_step_detail_cd_3 = config_read.get('scrpt_3','scrpt_3_step_detail_cd_3')

    print('[scrpt_3_step_basic_cd_1]' + str(scrpt_3_step_basic_cd_1))
    print('[scrpt_3_step_basic_cd_2]' + str(scrpt_3_step_basic_cd_2))
    print('[scrpt_3_step_basic_cd_3]' + str(scrpt_3_step_basic_cd_3))
    print('[scrpt_3_step_detail_cd_1]' + str(scrpt_3_step_detail_cd_1))
    print('[scrpt_3_step_detail_cd_2]' + str(scrpt_3_step_detail_cd_2))
    print('[scrpt_3_step_detail_cd_3]' + str(scrpt_3_step_detail_cd_3))

    return scrpt_3_step_basic_cd_1,scrpt_3_step_detail_cd_1,scrpt_3_step_basic_cd_2,scrpt_3_step_detail_cd_2,scrpt_3_step_basic_cd_3,scrpt_3_step_detail_cd_3

def get_config_email():

    config_read = configparser.ConfigParser()
    root_path = os.path.abspath("./")
    config_read.read(root_path + '/config.ini',encoding='utf-8')    

    send_id = config_read.get('email','send_id')
    send_pw = config_read.get('email','send_pw')
    recv_id = config_read.get('email','recv_id')
    email_title = config_read.get('email','email_title')
    email_contents = config_read.get('email','email_contents')

    print('[send_id]' + str(send_id))
    print('[send_pw]' + str(send_pw))
    print('[recv_id]' + str(recv_id))
    print('[email_title]' + str(email_title))
    print('[email_contents]' + str(email_contents))

    return send_id,send_pw,recv_id,email_title,email_contents

def script_1(step_basic_cd_1,step_detail_cd_1,send_id,send_pw,recv_id,email_title,email_contents):  
    # 네이버 브라우저 호출하기
    url = "https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/"
    browser = webdriver.Chrome("C:\workplace\Python\chromedriver_win32\chromedriver.exe")
    browser.implicitly_wait(10)
    browser.maximize_window()
    browser.get(url)

    # 아이디 입력창
    id = browser.find_element(By.CSS_SELECTOR,"#id")
    id.click()
    #id.send_keys("neokim_api@naver.com")
    pyperclip.copy("neokim_api@naver.com")
    pyautogui.hotkey("ctrl","v")
    time.sleep(2)

    # 비밀번호 입력창
    pw = browser.find_element(By.CSS_SELECTOR,"#pw")
    pw.click()
    #pw.send_keys("1q2w3e4r%t")
    pyperclip.copy("1q2w3e4r%t")
    pyautogui.hotkey("ctrl","v")
    time.sleep(2)

    # 로그인 버튼
    login_btn = browser.find_element(By.CSS_SELECTOR,"#log\.login")
    login_btn.click()
    time.sleep(2)

    ##################################
    ######### 브라우저 나타내기 #######
    ##################################
    # 현재 마우스 커서의 위치
    #locate = pyautogui.position()

    # 뉴스탭 이동하기
    try:
        pyautogui.moveTo(875,356)
        pyautogui.click()
        time.sleep(2)
        print('뉴스탭 이동 성공')
        step_basic_cd_1 = step_basic_cd_1
        step_detail_cd_1 = step_detail_cd_1
        error_cd = '0000'
        error_msg = '뉴스탭 이동 성공'
        
        db_insert(send_id,recv_id,email_title,email_contents,step_basic_cd_1,step_detail_cd_1,error_cd,error_msg)

        #mail_send(send_id,send_pw,recv_id,email_title,email_contents,step_basic_cd_1,step_detail_cd_1,error_cd,error_msg)   
        #return step_basic_cd_1,step_detail_cd_1,error_cd,error_msg

    except:
        print('뉴스탭 이동 오류')
        step_basic_cd_1 = step_basic_cd_1
        step_detail_cd_1 = step_detail_cd_1
        error_cd = '9999'
        error_msg = '뉴스탭 이동 실패'

        db_insert(send_id,recv_id,email_title,email_contents,step_basic_cd_1,step_detail_cd_1,error_cd,error_msg)

        if error_cd != '0000': # 오류화면
            mail_send(send_id,send_pw,recv_id,email_title,email_contents,step_basic_cd_1,step_detail_cd_1,error_cd,error_msg) # 메일 보내기 함수


    # 정치탭 이동하기
    try:
        pyautogui.moveTo(385,249)
        pyautogui.click()
        time.sleep(2)
        print('정치탭 이동 성공')
        step_basic_cd_1 = '2'
        step_detail_cd_1 = '(385,249)'
        error_cd = '0000'
        error_msg = '정치탭 이동 성공'    
        db_insert(send_id,recv_id,email_title,email_contents,step_basic_cd_1,step_detail_cd_1,error_cd,error_msg)
        #mail_send(send_id,send_pw,recv_id,email_title,email_contents,step_basic_cd_1,step_detail_cd_1,error_cd,error_msg)   
        #return step_basic_cd_1,step_detail_cd_1,error_cd,error_msg    
    except:
        print('정치탭 이동 오류')
        step_basic_cd_1 = step_basic_cd_1
        step_detail_cd_1 = step_detail_cd_1
        error_cd = '9999'
        error_msg = '정치탭 이동 실패'  
        db_insert(send_id,recv_id,email_title,email_contents,step_basic_cd_1,step_detail_cd_1,error_cd,error_msg)

        if error_cd != '0000': # 오류화면
            mail_send(send_id,send_pw,recv_id,email_title,email_contents,step_basic_cd_1,step_detail_cd_1,error_cd,error_msg) # 메일 보내기 함수


    # 정치 헤드라인 뉴스 이동하기
    try:
        pyautogui.moveTo(678,454)
        pyautogui.click()
        time.sleep(2)
        print('정치 헤드라인 뉴스 이동 성공')
        step_basic_cd_1 = '3'
        step_detail_cd_1 = '(678,454)'
        error_cd = '0000'
        error_msg = '정치 헤드라인 뉴스 이동 성공'   
        db_insert(send_id,recv_id,email_title,email_contents,step_basic_cd_1,step_detail_cd_1,error_cd,error_msg)     
        #mail_send(send_id,send_pw,recv_id,email_title,email_contents,step_basic_cd_1,step_detail_cd_1,error_cd,error_msg)   
        #return step_basic_cd_1,step_detail_cd_1,error_cd,error_msg
    except:
        print('정치 헤드라인 뉴스 이동 오류')
        step_basic_cd_1 = '3'
        step_detail_cd_1 = '(678,454)'
        error_cd = '9999'
        error_msg = '정치 헤드라인 뉴스 이동 실패'     
        db_insert(send_id,recv_id,email_title,email_contents,step_basic_cd_1,step_detail_cd_1,error_cd,error_msg)   

        if error_cd != '0000': # 오류화면
            mail_send(send_id,send_pw,recv_id,email_title,email_contents,step_basic_cd_1,step_detail_cd_1,error_cd,error_msg) # 메일 보내기 함수

##############################################
def script_2(step_basic_cd_2,step_detail_cd_2,send_id,send_pw,recv_id,email_title,email_contents):  
    # 네이버 브라우저 호출하기
    url = "https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/"
    browser = webdriver.Chrome("C:\workplace\Python\chromedriver_win32\chromedriver.exe")
    browser.implicitly_wait(10)
    browser.maximize_window()
    browser.get(url)

    # 아이디 입력창
    id = browser.find_element(By.CSS_SELECTOR,"#id")
    id.click()
    #id.send_keys("neokim_api@naver.com")
    pyperclip.copy("neokim_api@naver.com")
    pyautogui.hotkey("ctrl","v")
    time.sleep(2)

    # 비밀번호 입력창
    pw = browser.find_element(By.CSS_SELECTOR,"#pw")
    pw.click()
    #pw.send_keys("1q2w3e4r%t")
    pyperclip.copy("1q2w3e4r%t")
    pyautogui.hotkey("ctrl","v")
    time.sleep(2)

    # 로그인 버튼
    login_btn = browser.find_element(By.CSS_SELECTOR,"#log\.login")
    login_btn.click()
    time.sleep(2)

    ##################################
    ######### 브라우저 나타내기 #######
    ##################################
    # 현재 마우스 커서의 위치
    #locate = pyautogui.position()

    # 뉴스탭 이동하기
    try:
        pyautogui.moveTo(875,356)
        pyautogui.click()
        time.sleep(2)
        print('뉴스탭 이동 성공')
        step_basic_cd_2 = '1'
        step_detail_cd_2 = '(875,356)'
        error_cd = '0000'
        error_msg = '뉴스탭 이동 성공'
        
        db_insert(send_id,recv_id,email_title,email_contents,step_basic_cd_2,step_detail_cd_2,error_cd,error_msg)

    except:
        print('뉴스탭 이동 오류')
        step_basic_cd_2 = '1'
        step_detail_cd_2 = '(875,356)'
        error_cd = '9999'
        error_msg = '뉴스탭 이동 실패'

        db_insert(send_id,recv_id,email_title,email_contents,step_basic_cd_2,step_detail_cd_2,error_cd,error_msg)

        if error_cd != '0000': # 오류화면
            mail_send(send_id,send_pw,recv_id,email_title,email_contents,step_basic_cd_2,step_detail_cd_2,error_cd,error_msg) # 메일 보내기 함수

    locate_1 = pyautogui.position()
    print('[locate_1]' + str(locate_1))

    # 경제탭 이동하기
    try:
        pyautogui.moveTo(448,231)
        pyautogui.click()
        time.sleep(2)
        print('경제탭 이동 성공')
        step_basic_cd_2 = '2'
        step_detail_cd_2 = '(448,231)'
        error_cd = '0000'
        error_msg = '경제탭 이동 성공'    
        db_insert(send_id,recv_id,email_title,email_contents,step_basic_cd_2,step_detail_cd_2,error_cd,error_msg)
        #mail_send(send_id,send_pw,recv_id,email_title,email_contents,step_basic_cd_1,step_detail_cd_1,error_cd,error_msg)   
        #return step_basic_cd_1,step_detail_cd_1,error_cd,error_msg    
    except:
        print('경제탭 이동 오류')
        step_basic_cd_2 = '2'
        step_detail_cd_2 = '(448,231)'
        error_cd = '9999'
        error_msg = '경제탭 이동 실패'  
        db_insert(send_id,recv_id,email_title,email_contents,step_basic_cd_2,step_detail_cd_2,error_cd,error_msg)

        if error_cd != '0000': # 오류화면
            mail_send(send_id,send_pw,recv_id,email_title,email_contents,step_basic_cd_2,step_detail_cd_2,error_cd,error_msg) # 메일 보내기 함수

    locate_2 = pyautogui.position()
    print('[locate_2]' + str(locate_2))

    # 경제 헤드라인 뉴스 이동하기
    try:
        pyautogui.moveTo(893,450)
        pyautogui.click()
        time.sleep(2)
        print('경제 헤드라인 뉴스 이동 성공')
        step_basic_cd_2 = '3'
        step_detail_cd_2 = '(893,450)'
        error_cd = '0000'
        error_msg = '경제 헤드라인 뉴스 이동 성공'   
        db_insert(send_id,recv_id,email_title,email_contents,step_basic_cd_2,step_detail_cd_2,error_cd,error_msg)     
        #mail_send(send_id,send_pw,recv_id,email_title,email_contents,step_basic_cd_1,step_detail_cd_1,error_cd,error_msg)   
        #return step_basic_cd_1,step_detail_cd_1,error_cd,error_msg
    except:
        print('경제 헤드라인 뉴스 이동 오류')
        step_basic_cd_2 = '3'
        step_detail_cd_2 = '(893,450)'
        error_cd = '9999'
        error_msg = '경제 헤드라인 뉴스 이동 실패'     
        db_insert(send_id,recv_id,email_title,email_contents,step_basic_cd_2,step_detail_cd_2,error_cd,error_msg)   

        if error_cd != '0000': # 오류화면
            mail_send(send_id,send_pw,recv_id,email_title,email_contents,step_basic_cd_2,step_detail_cd_2,error_cd,error_msg) # 메일 보내기 함수

##############################################
def script_3(step_basic_cd_3,step_detail_cd_3,send_id,send_pw,recv_id,email_title,email_contents):  
    # 네이버 브라우저 호출하기
    url = "https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/"
    browser = webdriver.Chrome("C:\workplace\Python\chromedriver_win32\chromedriver.exe")
    browser.implicitly_wait(10)
    browser.maximize_window()
    browser.get(url)

    # 아이디 입력창
    id = browser.find_element(By.CSS_SELECTOR,"#id")
    id.click()
    #id.send_keys("neokim_api@naver.com")
    pyperclip.copy("neokim_api@naver.com")
    pyautogui.hotkey("ctrl","v")
    time.sleep(2)

    # 비밀번호 입력창
    pw = browser.find_element(By.CSS_SELECTOR,"#pw")
    pw.click()
    #pw.send_keys("1q2w3e4r%t")
    pyperclip.copy("1q2w3e4r%t")
    pyautogui.hotkey("ctrl","v")
    time.sleep(2)

    # 로그인 버튼
    login_btn = browser.find_element(By.CSS_SELECTOR,"#log\.login")
    login_btn.click()
    time.sleep(2)

    ##################################
    ######### 브라우저 나타내기 #######
    ##################################
    # 현재 마우스 커서의 위치


    # 뉴스탭 이동하기
    try:
        pyautogui.moveTo(875,356)
        pyautogui.click()
        time.sleep(2)
        print('뉴스탭 이동 성공')
        step_basic_cd_3 = '1'
        step_detail_cd_3 = '(875,356)'
        error_cd = '0000'
        error_msg = '뉴스탭 이동 성공'
        
        db_insert(send_id,recv_id,email_title,email_contents,step_basic_cd_3,step_detail_cd_3,error_cd,error_msg)


    except:
        print('뉴스탭 이동 오류')
        step_basic_cd_3 = '1'
        step_detail_cd_3 = '(875,356)'
        error_cd = '9999'
        error_msg = '뉴스탭 이동 실패'

        db_insert(send_id,recv_id,email_title,email_contents,step_basic_cd_3,step_detail_cd_3,error_cd,error_msg)

        if error_cd != '0000': # 오류화면
            mail_send(send_id,send_pw,recv_id,email_title,email_contents,step_basic_cd_3,step_detail_cd_3,error_cd,error_msg) # 메일 보내기 함수


    # 사회탭 이동하기
    try:
        pyautogui.moveTo(518,264)
        pyautogui.click()
        time.sleep(2)
        print('사회탭 이동 성공')
        step_basic_cd_3 = '2'
        step_detail_cd_3 = '(518,264)'
        error_cd = '0000'
        error_msg = '사회탭 이동 성공'    
        db_insert(send_id,recv_id,email_title,email_contents,step_basic_cd_3,step_detail_cd_3,error_cd,error_msg)

    except:
        print('사회탭 이동 오류')
        step_basic_cd_3 = '2'
        step_detail_cd_3 = '(518,264)'
        error_cd = '9999'
        error_msg = '사회탭 이동 실패'  
        db_insert(send_id,recv_id,email_title,email_contents,step_basic_cd_3,step_detail_cd_3,error_cd,error_msg)

        if error_cd != '0000': # 오류화면
            mail_send(send_id,send_pw,recv_id,email_title,email_contents,step_basic_cd_3,step_detail_cd_3,error_cd,error_msg) # 메일 보내기 함수


    # 사회 헤드라인 뉴스 이동하기
    try:
        pyautogui.moveTo(834,451)
        pyautogui.click()
        time.sleep(2)
        print('사회 헤드라인 뉴스 이동 성공')
        step_basic_cd_3 = '3'
        step_detail_cd_3 = '(834,451)'
        error_cd = '0000'
        error_msg = '사회 헤드라인 뉴스 이동 성공'   
        db_insert(send_id,recv_id,email_title,email_contents,step_basic_cd_3,step_detail_cd_3,error_cd,error_msg)     

    except:
        print('사회 헤드라인 뉴스 이동 오류')
        step_basic_cd_3 = '3'
        step_detail_cd_3 = '(834,451)'
        error_cd = '9999'
        error_msg = '사회 헤드라인 뉴스 이동 실패'     
        db_insert(send_id,recv_id,email_title,email_contents,step_basic_cd_3,step_detail_cd_3,error_cd,error_msg)   

        if error_cd != '0000': # 오류화면
            mail_send(send_id,send_pw,recv_id,email_title,email_contents,step_basic_cd_3,step_detail_cd_3,error_cd,error_msg) # 메일 보내기 함수



def db_insert(send_id,recv_id,email_title,email_contents,step_basic_cd_1,step_detail_cd_1,error_cd,error_msg):
    now = datetime.now()
    print('db_insert')
    #date_time = time.strftime('%Y-%m-%d_%H:%M:%S')
    date_time = time.strftime('%Y-%m-%d %H:%M:%S')
    date_time_2 = datetime.strptime(date_time,'%Y-%m-%d %H:%M:%S')

    print('[now.date]', now.date())
    print('[now.time]', now.time())

    sdate = str(now.date())
    print('[date_time]' + date_time)
    yyyy = time.strftime('%Y')
    mm = time.strftime('%m')
    dd = time.strftime('%d')
    
    #os.system("pause")
    # 전역 변수
    conn, cur = None, None
    data1, data2, data3, data4 = "","","",""


    # 시나리오 변수
    sql_1 = "" # 시나리오_1(뉴스)
    sql_2 = "" # 시나리오_2(경제)
    sql_3 = "" # 시나리오_3(영화)
    sql_4 = "" # 시나리오_4
    sql_5 = "" # 시나리오_5

    # connect database
    conn = pymysql.connect(host='127.0.0.1', user='root', password='12345678',db='appium',charset='utf8')

    # create cursor
    cur = conn.cursor()

    # insert 쿼리문
    sql_1 = """INSERT INTO appium_tb (send_id,recv_id,email_title,email_contents,step_basic_cd,step_detail_cd,error_cd,error_msg,reg_time)
                 VALUES(%s,%s,%s,%s,%s,%s,%s,%s,now())"""

    # 쿼리 실행
    cur.execute(sql_1, (send_id,recv_id,email_title,email_contents,step_basic_cd_1,step_detail_cd_1,error_cd,error_msg))
    conn.commit()
    conn.close()

def mail_send(send_id,send_pw,recv_id,email_title,email_contents,step_basic_cd_1,step_detail_cd_1,error_cd,error_msg):
    print('mail_send')
    #STMP 서버의 url과 port 번호
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 465

    # 1.SMTP 서버 연결
    smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)

    print('[send_id]' + send_id)
    print('[send_pw]' + str(send_pw))
    print('[recv_id]' + str(recv_id))
    print('[email_title]' + str(email_title))
    print('[email_contents]' + str(email_contents))

    #EMAIL_ADDR = send_id
    #EMAIL_PASSWORD = send_pw

    EMAIL_ADDR = send_id
    EMAIL_PASSWORD = send_pw
    # 2.SMTP 서버에 로그인
    smtp.login(EMAIL_ADDR,EMAIL_PASSWORD)

    # 3.MIME 형태의 이메일 메시지 작성
    email_title = '네이버 appium 화면 오류'
    email_contents = '[진행기본단계]' + str(step_basic_cd_1) + '[진행상세단계]' + str(step_detail_cd_1) + '[오류코드]' + str(error_cd) + '[오류메시지]' + error_msg

    message = EmailMessage()
    message.set_content(email_contents)
    message["Subject"] = email_title
    message["From"]= EMAIL_ADDR
    message["To"]= recv_id

    # 4.서버로 메일 보내기
    smtp.send_message(message)

    # 5.메일로 보내면 서버와 연결 끊기
    smtp.quit()

# main 함수
def main():
    print('프로그램 시작')
    # ini 파일 (script_1)
    script_1_step_basic_cd_1,script_1_step_detail_cd_1,script_1_step_basic_cd_2,script_1_step_detail_cd_2,script_1_step_basic_cd_3,script_1_step_detail_cd_3 = get_config_script_1()

    # # ini 파일 (script_2)
    script_2_step_basic_cd_1,script_2_step_detail_cd_1,script_2_step_basic_cd_2,script_2_step_detail_cd_2,script_2_step_basic_cd_3,script_2_step_detail_cd_3 = get_config_script_2()

    # # ini 파일 (script_3)
    script_3_step_basic_cd_1,script_3_step_detail_cd_1,script_3_step_basic_cd_2,script_3_step_detail_cd_2,script_3_step_basic_cd_3,script_3_step_detail_cd_3 = get_config_script_3()        

    # # ini 파일 (email)
    i_send_id,i_send_pw,i_recv_id,i_email_title,i_email_contents = get_config_email()
    
    # # # ini 파일 (timer)
    sleep_time,start_time,end_time,repeat_yn = get_config_time()

    # # #naver_login() # 네이버 로그인
    # # ######################
    # # #### 네이버 로그인 ####
    # # ######################
    # #r_step_basic_cd_1,r_step_detail_cd_1,r_error_cd,r_error_msg = script_1(step_basic_cd_1,step_detail_cd_1) # 정치 뉴스
    # script_1(script_1_step_basic_cd_1,script_1_step_detail_cd_1,i_send_id,i_send_pw,i_recv_id,i_email_title,i_email_contents) # 정치 뉴스
    # time.sleep(1)
    # script_2(script_2_step_basic_cd_1,script_2_step_detail_cd_1,i_send_id,i_send_pw,i_recv_id,i_email_title,i_email_contents) # 경제 뉴스
    # time.sleep(1)
    # script_3(script_3_step_basic_cd_1,script_3_step_detail_cd_1,i_send_id,i_send_pw,i_recv_id,i_email_title,i_email_contents) # 사회 뉴스
    
    ##########################
    ####### Time 설정 ########
    ##########################
    today = datetime.now()
    today_time = today.strftime("%H")

    if repeat_yn == 'Y':
        
        if int(str(today_time)) <= int(str(start_time)):

            print('반복 수행함')
            # ini 파일 (script_1)
            script_1_step_basic_cd_1,script_1_step_detail_cd_1,script_1_step_basic_cd_2,script_1_step_detail_cd_2,script_1_step_basic_cd_3,script_1_step_detail_cd_3 = get_config_script_1()

            # ini 파일 (script_2)
            script_2_step_basic_cd_1,script_2_step_detail_cd_1,script_2_step_basic_cd_2,script_2_step_detail_cd_2,script_2_step_basic_cd_3,script_2_step_detail_cd_3 = get_config_script_2()

            # ini 파일 (script_3)
            script_3_step_basic_cd_1,script_3_step_detail_cd_1,script_3_step_basic_cd_2,script_3_step_detail_cd_2,script_3_step_basic_cd_3,script_3_step_detail_cd_3 = get_config_script_3()        

            # ini 파일 (email)
            i_send_id,i_send_pw,i_recv_id,i_email_title,i_email_contents = get_config_email()
            
            # # ini 파일 (timer)
            sleep_time,start_time,end_time,repeat_yn = get_config_time()

            # #naver_login() # 네이버 로그인
            # ######################
            # #### 네이버 로그인 ####
            # ######################
            #r_step_basic_cd_1,r_step_detail_cd_1,r_error_cd,r_error_msg = script_1(step_basic_cd_1,step_detail_cd_1) # 정치 뉴스
            script_1(script_1_step_basic_cd_1,script_1_step_detail_cd_1,i_send_id,i_send_pw,i_recv_id,i_email_title,i_email_contents) # 정치 뉴스
            time.sleep(1)
            script_2(script_2_step_basic_cd_1,script_2_step_detail_cd_1,i_send_id,i_send_pw,i_recv_id,i_email_title,i_email_contents) # 경제 뉴스
            time.sleep(1)
            script_3(script_3_step_basic_cd_1,script_3_step_detail_cd_1,i_send_id,i_send_pw,i_recv_id,i_email_title,i_email_contents) # 사회 뉴스
                
            threading.Timer(int(sleep_time),main).start()
        elif (int(str(today_time)) <= int(str(start_time))) and (int(str(today_time)) == int(str(end_time))):
            print('반복 수행안함')
            threading.Timer(int(sleep_time),main).cancel()

    print('프로그램 진행중')        

# 프로그램 시작점
if __name__ == '__main__':
    
    # 메인함수 호출
    main()
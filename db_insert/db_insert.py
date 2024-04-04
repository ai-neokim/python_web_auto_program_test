# mysql 라이브러리
import pymysql 

# 전역 변수
conn, cur = None, None
data1, data2, data3, data4 = "","","",""

# 시나리오 변수
sql_1 = "" # 시나리오_1
sql_2 = "" # 시나리오_2
sql_3 = "" # 시나리오_3
sql_4 = "" # 시나리오_4
sql_5 = "" # 시나리오_5

# connect database
conn = pymysql.connect(host='127.0.0.1', user='root', password='12345678',db='appium',charset='utf8')

# create cursor
cur = conn.cursor()

# insert 쿼리문
sql_1 = "INSERT INTO appium_tb VALUES('test108@gmail.com','test109@gmail.com','test-title','test-content','6','1','1001','기본스텝-6,상세스텝-1에서 에러 메시지 발생함')"
sql_2 = "INSERT INTO appium_tb VALUES('test108@gmail.com','test109@gmail.com','test-title','test-content','7','1','1001','기본스텝-7,상세스텝-1에서 에러 메시지 발생함')"
sql_3 = "INSERT INTO appium_tb VALUES('test108@gmail.com','test109@gmail.com','test-title','test-content','8','1','1001','기본스텝-8,상세스텝-1에서 에러 메시지 발생함')"
sql_4 = "INSERT INTO appium_tb VALUES('test108@gmail.com','test109@gmail.com','test-title','test-content','9','1','1001','기본스텝-9,상세스텝-1에서 에러 메시지 발생함')"
sql_5 = "INSERT INTO appium_tb VALUES('test108@gmail.com','test109@gmail.com','test-title','test-content','10','1','1001','기본스텝-10,상세스텝-1에서 에러 메시지 발생함')"

# 쿼리 실행
cur.execute(sql_1)
cur.execute(sql_2)
cur.execute(sql_3)
cur.execute(sql_4)
cur.execute(sql_5)
conn.commit()
conn.close()



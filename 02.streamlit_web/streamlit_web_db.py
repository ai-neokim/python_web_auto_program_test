import pymysql
import pandas as pd

conn, cur = None, None

# connect database
conn = pymysql.connect(host='127.0.0.1', user='root', password='12345678',db='appium',charset='utf8')

# create cursor
cur = conn.cursor()

sql = "SELECT * FROM appium.appium_tb where script_cd is not null and reg_time >= '2023-07-06 14:00:00'  "

cur.execute(sql)

rows = cur.fetchall()

conn.close() # DB 연결 종료

print(rows)
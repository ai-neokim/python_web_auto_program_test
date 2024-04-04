
import smtplib
from email.message import EmailMessage

#STMP 서버의 url과 port 번호
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465

# 1.SMTP 서버 연결
smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)

EMAIL_ADDR = ''      # 구글 이메일을 입력합니다. (필수 입력 사항)
EMAIL_PASSWORD = ''  # 구글 패스워드를 입력합니다.(필수 입력 사항)

# 2.SMTP 서버에 로그인
smtp.login(EMAIL_ADDR,EMAIL_PASSWORD)

# 3.MIME 형태의 이메일 메시지 작성
message = EmailMessage()
message.set_content('이메일 내용-1')
message["Subject"] = "이메일 제목-1"
message["From"]=EMAIL_ADDR
message["To"]='neokim.api@gmail.com'

# 4.서버로 메일 보내기
smtp.send_message(message)

# 5.메일로 보내면 서버와 연결 끊기
smtp.quit()

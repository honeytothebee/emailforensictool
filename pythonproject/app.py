import imaplib
import email
from email.header import decode_header, make_header
import subprocess




gmail = imaplib.IMAP4_SSL('imap.gmail.com') #SSL을 이용하여 암호화된 소켓을 통해 IMAP4 서버 접속

gmail.login('xxxxx@gmail.com', 'xxxxxxx') #앱 비밀번호 16자리 및 id 입력 하는 부분.

gmail.select('inbox')
status, messages = gmail.uid('search', None, 'ALL') #메일에 고유번호 부여, status -> 상태, messages -> 메시지 수

messages = messages[0].split() #메시지를 나눔

recent = messages[-1] #최신 메일 -> -1

for uid in messages:
  
  res, msg = gmail.uid('fetch', uid, "(RFC822)") #fetch - 메시지 가져오기, recent - 메시지 UID, RFC822 - 이 형식으로 가져오기
  raw = msg[0][1] 
  read = raw.decode('utf-8') #utf-8 로 raw email 디코딩
  
  file = open('~/bobprojectpython/emailcrawlraw/emailraw.txt', 'w') #읽을 수 있는 이메일 텍스트 파일로 저장
  w = file.write(read)
  w = file.write("\n============================================================================\n")
  file.close()


  mail_mes = email.message_from_string(read) #string 형태로 가져오기


  sender = str(make_header(decode_header(mail_mes.get('From')))) #from 보낸사람


  title = str(make_header(decode_header(mail_mes.get('Subject')))) #제목
 
  if mail_mes.is_multipart(): #멀티파트인지 확인하기
    for part in mail_mes.walk():
      contype = part.get_content_type()
      condispo = str(part.get('Content-Disposition'))
      if contype == 'text/plain' and 'attachment' and 'text/html' not in condispo:
       body = part.get_payload(decode = True).decode('utf-8')
       break
   
  else:
   body = mail_mes.get_payload(decode = True).decode('utf-8')
  

  

  file = open('~/bobprojectpython/emailcrawlclean/emailclean.txt', 'a')
  w = file.write(sender)
  w = file.write("\n")
  w = file.write(title)
  w = file.write("\n")
  w = file.write(body)
  w = file.write("\n")
  
  file.close()

gmail.logout()

file.close()

def scriptpy():
  path = "~/bobprojectpython/compare.py"
  subprocess.run(["python3", path])

scriptpy()



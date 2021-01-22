import smtplib
from email.mime.text import MIMEText
from email.header import Header
sender=input('请输入登录邮箱：')
password = input('请输入邮箱授权码：')
to_addrs=[]
while 1:
    a=input('请输入收件人邮箱：')
    to_addrs.append(a)
    b=input('是否继续输入，n退出，任意键继续：')
    if b=='n':
        break
smtp_server='smtp.qq.com'
text= ''' '''#添加文本                              
msg = MIMEText(text,'plain','utf-8')
msg['From'] = Header(sender)
msg['To'] = Header(','.join(to_addrs))
msg['Subject'] = Header('python test')
server = smtplib.SMTP()
server.connect(smtp_server, 25) #host=smtp.qq.com , port=25 or SSLPORT=465
server.login(sender, password) #授权码=yelnnqvxqyjabaeg
server.sendmail(sender, to_addrs, msg.as_string()) 
server.quit() 


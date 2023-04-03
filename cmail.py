import smtplib
from smtplib import SMTP
from email.message import EmailMessage
def sendmail(to,otp):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('keerthipriya.m2002@gmail.com','vczcmzsjsilkcswd')
    msg=EmailMessage()
    msg['From']='keerthipriya.m2002@gmail.com'
    msg['Subject']='Account Sign up OTP'
    msg['To']=to
    body=f'Your one time otp for registration is {otp}'
    msg.set_content(body)
    server.send_message(msg)
    server.quit()

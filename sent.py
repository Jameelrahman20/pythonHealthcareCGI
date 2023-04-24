#!C:\Python311\python.exe
print("Content-type:text/html\n\r")

import cgi

form=cgi.FieldStorage()


admin_emailid=form.getvalue("a1")
patient_emailid=form.getvalue("a2")
sub1=form.getvalue("s1")
sub2=form.getvalue("s2")
sub3=form.getvalue("s3")
sub4=form.getvalue("s4")
msg1=form.getvalue("m1")
msg2=form.getvalue("m2")
msg3=form.getvalue("m3")
msg4=form.getvalue("m4")


import smtplib
import schedule
import time


email=admin_emailid
password='hcxscfroxdufwcvu'


def morning_email():
    subject = sub1
    message = msg1
    send_email(subject, message)

def noon_email():
    subject = sub2
    message = msg2
    send_email(subject, message)

def night_email():
    subject = sub3
    message = msg3
    send_email(subject, message)

def next_appointment():
    subject = sub4
    message = msg4
    send_email(subject, message)



def send_email(subject, message):
    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email,password)
        to_email=patient_emailid
        body='\r\n'.join(['To: %s' % to_email,
                            'From: %s' % email,
                            'Subject: %s' % subject,
                            '', message])
        server.sendmail(email, to_email, body)
        print('Email sent successfully')
    except Exception as e:
        print('Something went wrong:', e)
    finally:
        server.quit()


schedule.every().day.at("15:36").do(morning_email)
schedule.every().day.at("15:37").do(noon_email)
schedule.every().day.at("15:38").do(night_email)
schedule.every().day.at("15:39").do(next_appointment)


while True:
    schedule.run_pending()
    time.sleep(1)




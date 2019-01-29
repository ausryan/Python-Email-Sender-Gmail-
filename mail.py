#A simple way of sending emails with Python (via Gmail)
#Ryan
#Version 1.0
#29/01/2019

import smtplib

senderemail = "gmail@gmail.com"
senderpassword = "gmailPassword"
sendtoemail = "sendtoemail@gmail.com"


def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(senderemail, senderpassword)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(senderemail, sendtoemail, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")


subject = "Test Email"
msg = "This is a test email sent from Python!"

send_email(subject, msg)

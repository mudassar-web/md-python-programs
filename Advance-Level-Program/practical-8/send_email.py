import smtplib
import password

TO = 'receiver@gmail.com'

SUBJECT = 'PYTHON 3.4 TEST EMAIL'

TEXT = """Here is a message from python.
\nLots of thing can be done with python.\nPython Love.\nHAPPY CODING!!!!!"""

# Gmail Sign In
gmail_sender = 'sender@gmail.com'

gmail_passwd = password.pwd

server = smtplib.SMTP('smtp.gmail.com', 587)

server.ehlo()

server.starttls()

server.login(gmail_sender, gmail_passwd)

BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % gmail_sender,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])

try:
    server.sendmail(gmail_sender, [TO], BODY)
    print ('email sent')
except:
    print ('error in sending mail')
server.quit()
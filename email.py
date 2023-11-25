# mvbqugcixfirvifl

"""import ssl,smtplib

from email.message import EmailMessage

email_sender = 'ansalr.email@gmail.com'
email_password = 'xcvbnmjhgfdd'

email_reciver = 'robinsonresa3005@gmail.com'

subject = "test subject 001"
body = " it's is working "

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_reciver,em.as_string()) """

import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('ansalr.email@gmail.com','rosemohen8@')
server.sendmail( 'ansalr.email@gmail.com','robinsonresa3005@gmail.com','test mail 001')
print('mail send!!!')

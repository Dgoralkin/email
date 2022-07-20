# Demo @ https://www.youtube.com/watch?v=JRCJ6RtE3xU&list=WL&index=19

import os
import smtplib
from email.message import EmailMessage

# EMAIL_ADDRESS = 'g.c.s@gmail.com'
# EMAIL_PSSWRD = 'G...22'

EMAIL_ADDRESS = os.environ.get('Gmail_smtp_username')
EMAIL_PSSWRD = os.environ.get('Gmail_smtp_psswrd')

msg = EmailMessage()
msg['Subject'] = 'This is an Email Demo with environ.get'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'goralkin@gmail.com'
msg.set_content('This is Demo How emails sent from Python!')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PSSWRD)
    smtp.send_message(msg)
    
    
    
'''    
# To run on a localhost type in Shell: python -m smtpd -c DebuggingServer -n localhost:1025
with smtplib.SMTP('localhost', 1025) as smtp:
    
    subject = 'This is an Email Demo with environ.get'
    body = 'How emails sent from Python?'
    msg = f'Subject: {subject}\n\n{body}'
    smtp.sendmail(EMAIL_ADDRESS, 'goralkin@gmail.com', msg)
''' 

# To attach files:
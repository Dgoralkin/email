# In this tutorial:

# To Send Email with HTML
# To Send Email and one image
# To Send Email and several images
# To Send Email and file attachment
# To run localhost Email server
# Demo @ https://www.youtube.com/watch?v=JRCJ6RtE3xU&list=WL&index=19

import os
import smtplib
import imghdr
from email.message import EmailMessage


EMAIL_ADDRESS = os.environ.get('Gmail_smtp_username') # EMAIL_ADDRESS = 'g.c.s@gmail.com'
EMAIL_PSSWRD = os.environ.get('Gmail_smtp_psswrd') # EMAIL_PSSWRD = 'G...22'

CONTACTS = ['goralkin@gmail.com', 'gbikes01@gmail.com'] # OPTIONAL
msg = EmailMessage()
msg['Subject'] = 'This is an Email Demo with environ.get, HTML and IMG or FILE attachement'
msg['From'] = EMAIL_ADDRESS
msg['To'] = ', '.join(CONTACTS) # OPTIONAL:Send to One Address: 'goralkin@gmail.com'
msg.set_content('Image attached')

# To Send Email with HTML
msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:red;">This is a HTML sample!!!</h1><hr>
    </body>
</html>
""", subtype='html')
    
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PSSWRD)
    smtp.send_message(msg)
    
    

#                   To add several Images to mail    =>    To Send one image Check below
'''
FILES = ['image.jpg', 'Gmail.png']
for image in FILES:
    with open(image, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name    
    print("file sent: ", file_name, file_type)
    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
    
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PSSWRD)
    smtp.send_message(msg)
'''



#                   To add One Image to mail
'''
with open('image.jpg', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name    
print("file sent: ", file_name, file_type)
    
msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PSSWRD)
    smtp.send_message(msg)
'''



#                   To send several files (pdf/word) to mail
'''
files = ['PDF_sample.pdf', 'README.txt']
for image in files:
    with open(image, 'rb') as f:
        file_data = f.read()
        file_name = f.name    
    print("file sent: ", file_name)
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
    
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PSSWRD)
    smtp.send_message(msg)
'''


#                   To run on a localhost run in Shell:
#                   python -m smtpd -c DebuggingServer -n localhost:1025          and change: smtplib.SMTP('localhost', 1025)
'''    
with smtplib.SMTP('localhost', 1025) as smtp:
    
    subject = 'This is an Email Demo with environ.get'
    body = 'How emails sent from Python?'
    msg = f'Subject: {subject}\n\n{body}'
    smtp.sendmail(EMAIL_ADDRESS, 'goralkin@gmail.com', msg)
''' 

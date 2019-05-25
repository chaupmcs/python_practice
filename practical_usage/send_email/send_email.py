import os
import smtplib
import imghdr
from email.message import EmailMessage

# EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
# EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')



with open('./../../../print_doc_2_pass.txt') as f:
    data = f.readlines()
    EMAIL_ADDRESS, EMAIL_PASSWORD = data[0].strip(), data[1].strip()


contacts = ['xyz@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'Reschedule the meeting - third'
msg['X-Priority'] = '1'

msg['From'] = EMAIL_ADDRESS
msg['To'] = contacts

msg.set_content("Hi Chau, the second email")

# msg.add_alternative("""\
# <!DOCTYPE html>
# <html>
#     <body>
#         <h1 style="color:SlateGray;">This is an HTML Email!</h1>
#     </body>
# </html>
# """, subtype='html')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
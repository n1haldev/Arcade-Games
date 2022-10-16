import random
import smtplib
from email.message import EmailMessage
import imghdr
from rand_pass_gen import generate_random_password,generate_2FA_code

EMAIL_ADDRESS='your_mail_id@mail.com'	# email id to send your users email
EMAIL_PASSWORD='yourmailpassword'	# password of that email id (do not forget to disbale all 2 FA authentication as SMTP needs free access to your mail account)

def welcome(a,b):	# welcome email for newly registered users
    global EMAIL_ADDRESS,EMAIL_PASSWORD,msg
    msg=EmailMessage()
    msg['Subject']='Welcome to Arcade world'
    msg['From']=EMAIL_ADDRESS
    msg['To']=a
    twofa=generate_2FA_code()
    msg.set_content(f'''Dear {b},\nRelive your childhood with a game that will give make you feel nostalgic and experience euphoria!
\nEnjoy the Game\nHere is your Confirmation code- {twofa}\nWith Warm Regards,\nNihal T M.''')
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
            smtp.send_message(msg)
            return twofa

def send_pass(a,b,c):	# forgot password email
    global EMAIL_ADDRESS,EMAIL_PASSWORD,msg
    msg=EmailMessage()
    msg['Subject']='Arcade world password Reset'
    msg['From']=EMAIL_ADDRESS
    msg['To']=a
    new_pass=c
    msg.set_content(f'''Dear {b},\nWe realised that you wanted to login to your favourite Arcade games but could not as you had forgotten the password.
\nSo here is your password- {new_pass}\nPlease do not forget to delete this email once you have logged in\nEnjoy the Game\nWith Warm Regards,\nNihal T M.''')
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
            smtp.send_message(msg)
    return new_pass

def two_FA(a,b):	# two factor authentication email
    global EMAIL_ADDRESS,EMAIL_PASSWORD,msg
    msg=EmailMessage()
    msg['Subject']='Arcade world 2FA'
    msg['From']=EMAIL_ADDRESS
    msg['To']=a
    twofa=generate_2FA_code()
    msg.set_content(f'''Dear {b},\nWe realised that you wanted to login to your Arcade world.
\nSo here is the 2FA code- {twofa}\nEnjoy the Game\nWith Warm Regards,\nNihal T M.''')
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
            smtp.send_message(msg)
    return twofa






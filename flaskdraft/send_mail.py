import smtplib
import os
#allows us to send text and html emails
from email.mime.text import MIMEText
from flaskdraft.settings import Config

def send_mail(name, email, comments):
    
#_--------Login Credentials and Info--------#
    
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = ADD MAILTRAP_LOGIN
    password =  ADD MAILTRAP_PASS
    message = f'<h3>New Feedback Submission</h3><ul><li>Name: {name}</li><li>Email: {email}</li><li>Comments: {comments}</li></ul>'
    sender_email = 'sample@yahoo.com'
    receiver_email = 'email2@example.com'
    
    
#_--------Setup --------#
    
    #takes the message from above and the text we want (html)
    msg = MIMEText(message, 'html')
    #our email subject
    msg['Subject'] = 'Draft Feedback'
    #From and to 
    msg['From'] = sender_email
    msg['To'] = receiver_email
    
#_--------Send request to Server --------#
    
    # takes server and port and sets it as server we'll use

    with smtplib.SMTP(smtp_server, port) as server:
        #login to server
        server.login(login, password)
        #sends mail
        server.sendmail(sender_email, receiver_email, msg.as_string())


    login = '91801d061939fc'
    password = 'cb987337ae8348'
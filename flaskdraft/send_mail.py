import smtplib
#allows us to send text and html emails
from email.mime.text import MIMEText

def send_mail(name, email, comments):
    
#_--------Login Credentials and Info--------#
    
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '91801d061939fc'
    password = 'cb987337ae8348'
    message = f'<h3>New Feedback Submission</h3><ul><li>Name: {name}</li><li>Email: {email}</li><li>Comments: {comments}</li></ul>'
    sender_email = 'aschonn_trinity@yahoo.com'
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

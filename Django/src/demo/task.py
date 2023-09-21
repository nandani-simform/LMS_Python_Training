from celery import shared_task
from time import sleep
from django.conf import settings
from email.mime.text import MIMEText
import smtplib

@shared_task
def send_email(email_address):
    print('email send called')
    sleep(10)
    print(f"Hi, I'm sending an email to: {email_address}")
    me = settings.EMAIL_USERNAME
    password = settings.EMAIL_PASSWORD
    you = email_address

    email_body = """
        <html>
            <body>
                <p> hello, its nandani </p>
            </body>
        </html>
    """

    message = MIMEText(email_body, "html")
    message['Subject'] = 'new mail'
    message['From'] = me
    message['To'] = you

    try:
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login(me,password)
        server.sendmail(me, you,message.as_string())
        server.quit()
    except Exception as e:
        print('Error in sending email: {e}')

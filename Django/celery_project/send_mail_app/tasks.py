# from django.contrib.auth import get_user_model
# from celery import shared_task
# from django.core.mail import send_mail
# from celery_project import settings



# @shared_task(bind=True)
# def send_mail(self):
#     users = get_user_model().objects.all()
#     for user in users:
#         mail_subject = 'Hi!! Celery Testing'
#         message = "Hey!! Good Morning , Its Nandani here"
#         to_email = user.email 
#         send_mail(
#             subject = mail_subject,
#             message = message,
#             from_email = settings.EMAIL_HOST_USER,
#             recipientlist = [to_email],
#             fail_silently = True ,
#         )

#     return 'Done'


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
        print("email sent")
        server.quit()
    except Exception as e:
        print('Error in sending email: {e}')

# send_email.py

import smtplib
from email.message import EmailMessage


sender_email = "vaninehra4@gmail.com"
receiver_email = "vstyle.estudio@gmail.com"
app_password = "baghlgoxfbhueymq"


msg = EmailMessage()

msg["Subject"] = "Python Email"
msg["From"] = sender_email
msg["To"] = receiver_email

msg.set_content("""
Hello!
This is my Week 4 Python assignment.

Regards,
Vani
""")


try:

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:

        server.login(sender_email, app_password)

        server.send_message(msg)

    print("Email sent successfully!")

except Exception as e:

    print("Error:", e)
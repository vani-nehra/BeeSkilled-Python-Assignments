import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Your Gmail details
SENDER_EMAIL = "your_email@gmail.com"
APP_PASSWORD = "Your_app_password"

# Dynamic email details
subject = input("Enter email subject: ")
message = input("Enter email message: ")

# Read students.csv
with open("students.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    # Connect to Gmail
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(SENDER_EMAIL, APP_PASSWORD)

    for student in reader:
        name = student["name"]
        email = student["email"]

        # Personalize message
        personalized_message = f"""
Hello {name},

{message}

Regards,
Vani
"""

        # Create email
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = email
        msg["Subject"] = subject

        msg.attach(MIMEText(personalized_message, "plain"))

        try:
            server.sendmail(
                SENDER_EMAIL,
                email,
                msg.as_string()
            )
            print(f"Email sent to {name}")

        except Exception as e:
            print(f"Failed for {name}: {e}")

    server.quit()

print("All emails processed!")
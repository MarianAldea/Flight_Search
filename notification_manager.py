from twilio.rest import Client
import smtplib
import os
class NotificationManager:
    def __init__(self):
        self.acc_sid = "ACb5cfd827d47363055ee234c3eb9436cb"
        self.auth_token = "e41e66f53b8c7aaf71167e0129a39ab3"
        self.number = "+16789213832"

    def send_sms(self, mesaj):
        self.message = mesaj
        client = Client(self.acc_sid, self.auth_token)
        message = client.messages \
            .create(
            body=f"Price alert! {self.message}",
            from_=self.number,
            to=os.environ.get("USER_PHONE_NUMBER")
        )
    def send_email(self, email, text):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=os.environ.get("USER_EMAIL"), password=os.environ.get("MAIL_PASSWORD"))
            connection.sendmail(
                from_addr=os.environ.get("USER_EMAIL"),
                to_addrs=email,
                msg=f"Subject: New flight deals\n\n{text}"
            )
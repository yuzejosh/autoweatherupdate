from weather import generate_weather_msg
import smtplib
from secret import EMAIL_ADDRESS, EMAIL_PASSWORD

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    subject = 'Your daily weather update!'
    body = generate_weather_msg()
    msg = f'Subject: {subject}\n\n{body}'
    smtp.sendmail(EMAIL_ADDRESS, 'josherheng@gmail.com', msg)
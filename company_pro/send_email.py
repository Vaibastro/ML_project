import smtplib
import ssl

def send_mail(message):
    host = "smtp.gmail.com"
    port = 465

    username = "vaib.quantum@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "vaib.quantum@gmail.com"
    context = ssl.create_default_context()


    with smtplib.SMTP_SSL(host, port ,context= context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)





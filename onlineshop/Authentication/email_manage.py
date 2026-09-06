import smtplib
import ssl

port = 476

smtp_server = "smtp.gmail.com"
sender_email = "8"
password = "8"
#getpass("Type your password and press enter: ")

code=12

context = ssl.create_default_context()
with smtplib.SMTP_SSL(
    smtp_server,
    port,
    context=context,
    ) as server:
        server.login(sender_email, password)

server.starttls()

server.login("sender_email_id", "sender_email_id_password")
# message to be sent
message = f"hello! here is your {code}"
# sending the mail
server.sendmail("sender_email_id", "receiver_email_id", message)
# terminating the session
server.quit()
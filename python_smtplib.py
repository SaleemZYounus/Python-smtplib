import smtplib

#two factor authentication must be off

message = "Yo python helped me send this"

server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()

server.login("EMAIL@gmail.com", "PASSWORD")

server.sendmail('vidudeman@gmail.com', "vidudeman@gmail.com", message)

print('Email Sent')
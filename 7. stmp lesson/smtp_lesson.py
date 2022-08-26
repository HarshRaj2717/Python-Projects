# Gmail blocks this now as it's not secure enough.
# Tried with Yahoo too but unable to use it's less secure apps functionality.

import smtplib

my_mail = "tempraj2717@gmail.com"
my_password = input("enter password: ")

destination_mail = input("enter destination mail: ")
mail_text = input("enter text to send: ")

with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    connection.starttls() # tls = transport layer security, used to secure the connection.
    connection.login(user=my_mail, password=my_password)
    connection.sendmail(from_addr=my_mail, to_addrs=destination_mail, msg=mail_text)

import csv, smtplib, ssl

message = """Subject: Umur

Hi {name}, Umurmu {umur} tahun"""
from_address = "rahadianpython1995@gmail.com"
password = input("Type your password and press enter: ")

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(from_address, password)
    with open("daftar_kontak.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, email, umur in reader:
            server.sendmail(
                from_address,
                email,
                message.format(name=name,umur=umur),
            )
#sumber https://realpython.com/python-send-email/#sending-multiple-personalized-emails

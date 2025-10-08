import smtplib

my_email = ("placeholder@gmail.com")
password = "abcd1234()"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls() #transport layer security = tls -- provides us encruption to make this connection secure
connection.login(user=my_email, password=password)

connection.sendmail(from_addr=my_email, 
                    to_addrs="notreal@gmail.com", 
                    msg = "Subject:Test\n\nThis is the body of my email")
connection.close()
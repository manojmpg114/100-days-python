import smtplib
import datetime as dt
import random

my_email = ("placeholder@gmail.com")
password = "abcd1234()"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls() #encrypt the connection with tls
    connection.login(user=my_email, password=password)
    
    now = dt.datetime.now() #we want to use this to determine that today is the same day we expect it to be, really an if case with True will work 
    
    quotes = []
    with open("quotes.txt", "r", encoding="utf-8") as file:
        quotes = [line.strip() for line in file]
        
    with open(quotes.txt) as quote_file:
        all_quotes = quote_file.readlines() # this could have been a more direct way to get the lines into a list vs using loop comprehensions
      
      
    if now.weekday() == now.weekday(): #now we know today is the day we want to send stuff to make it work right away, since its 0 indexed we would really want to make it now.weekday()+1
        #send a random quote from quotes.txt file
        random_quote = random.choice(quotes)
        
        connection.sendmail(from_addr=my_email,
                            to_addrs="notrealgmail.com",
                            msg = f"Subject:Random Quote\n\n{random_quote}")
        

# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls() #transport layer security = tls -- provides us encruption to make this connection secure
# connection.login(user=my_email, password=password)

# connection.sendmail(from_addr=my_email, 
#                     to_addrs="notreal@gmail.com", 
#                     msg = "Subject:Test\n\nThis is the body of my email")
# connection.close()

# with smtplib.SMTP("smtp.gmail.com") as connection: #doing it this way we will automatically close the connection when we are done with this code block
#     connection.starttls() #transport layer security = tls -- provides us encruption to make this connection secure
#     connection.login(user=my_email, password=password)

#     connection.sendmail(from_addr=my_email, 
#                         to_addrs="notreal@gmail.com", 
#                         msg = "Subject:Test\n\nThis is the body of my email")
    
# import datetime as dt

print(dt.datetime.now().weekday())
# now = dt.datetime.now()
# print(now.year)
# print(type(now))
# print(now.weekday()+1)

# date_of_birth = dt.datetime(year=2025, month= 1, day= 1)

# print(date_of_birth)

quotes = []
with open("quotes.txt", "r", encoding="utf-8") as file:
    quotes = [line.strip() for line in file]

print(len(quotes))  
print(random.choice(quotes))

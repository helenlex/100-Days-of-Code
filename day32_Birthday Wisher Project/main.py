
# Wednesday Inspiration Quote Email

import smtplib
import datetime as dt
import random as r

my_email = "test@test.com"
password = "testpassword-notreal" # if emailing from gmail, use an app password

with open(r"day32_Birthday Wisher Project\quotes.txt") as file:
    read = file.read()

read_split = read.split("\n") #split the file into a list

#print(r.choice(read_split))

now = dt.datetime.now()

if now.weekday() == 2: # If it's a Wednesday

    with smtplib.SMTP("smtp.gmail.com", port= 587) as connection:
        connection.starttls() #securing our connection
        connection.login(user=my_email, password= password)
        connection.sendmail(from_addr = my_email, to_addrs= "othertest@test.com", 
                            msg= f"Subject:Motivational Quote Wednesday\n\n {r.choice(read_split)}.") # send a random quote from the file

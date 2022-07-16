import pandas
import random
import smtplib
import datetime as dt
USER_NAME = "mdtauseefakhtar284@gmail.com"
PASSWORD = "jjhdpacjnkwwmgjl"

"""
To-Do:-
1. Update the birthdays.csv
2. Check if today matches a birthday in the birthdays.csv
3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name
from birthdays.csv
4. Send the letter generated in step 3 to that person's email address.
"""

data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")

today = dt.datetime.now()
month = today.month
day = today.day
for dates in data_dict:
    if dates["month"] == month and dates["day"] == day:
        random_letter_number = random.randint(1, 3)
        random_letter = "letter_"+str(random_letter_number)+".txt"
        with open(f"letter_templates/{random_letter}", "r") as letter_file:
            txt = letter_file.read()
            new_letter = txt.replace("[NAME]", dates["name"])
            connection = smtplib.SMTP("smtp.gmail.com", 587)
            connection.starttls()
            connection.login(user=USER_NAME, password=PASSWORD)
            connection.sendmail(from_addr=USER_NAME, to_addrs=dates["email"], msg=f"Subject:Happy Birthday\n\n"
                                                                                  f"{new_letter}")

# Weekdays
# This program recognice if the day is weekday or weekend
# By Ignacio Riboldi

import datetime

today = datetime.datetime.today().weekday()

if today < 5:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")
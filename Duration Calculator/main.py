import numpy as np
import datetime

flag = False

while flag == False:
    date_input = np.datetime64(input("Enter the date in the past in the format YYYY-MM-DD: "))
    today = np.datetime64(datetime.date.today())
    if date_input > today:
        print("You have chosen a date in the future. Try again.")
    else:
        difference = (today - date_input)
        print (difference)
        flag = True


import tkinter as tk
import datetime
from calendar import monthrange 


root = tk.Tk()

root.geometry("500x500")

root.title("Calandar")

date = datetime.date.today()

def NextMonth():
    print("next")
    global current_month
    global current_year
    global month_label
    current_month += 1
    if current_month > 12:
        current_month = 1
        current_year += 1
    #print(current_month)
    days_in_month = monthrange(current_year,current_month)
    day_of_week = datetime.date(current_year,current_month,1).weekday()
    date = datetime.date(current_year,current_month,1)
    month = date.strftime("%B")
    month_label.configure(text = month)
    ShowMonth(days_in_month,day_of_week)


def PreviousMonth():
    print("previous")
    global current_month
    global current_year
    global month_label
    current_month -= 1
    if current_month < 1:
        current_month = 12
        current_year -= 1
    days_in_month = monthrange(current_year,current_month)
    day_of_week = datetime.date(current_year,current_month,1).weekday()
    date = datetime.date(current_year,current_month,1)
    month = date.strftime("%B")
    month_label.configure(text = month)
    ShowMonth(days_in_month,day_of_week)


prev_Month = tk.Button(root,text = "Previous", command = PreviousMonth)

prev_Month.grid(column = 0, row = 0)

next_Month = tk.Button(root,text = "Next", command = NextMonth)

next_Month.grid(column = 6, row = 0)

month = date.strftime("%B")
month_label = tk.Label(root,text = month)
month_label.grid(column=0,row=1,columnspan=6)

days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
for day in days:
    db = tk.Label(root,text = day)
    db.grid(column = days.index(day),row = 2)

date_labels = []
for da in range(35):
    lb = tk.Label(root,text = "")
    date_labels.append(lb)

def ShowMonth(days_in_month,day_of_week):
    if len(date_labels) > 0:
        for da in date_labels:
            da.configure(text = "")
    for days in range(days_in_month[1]):
        lb = date_labels[day_of_week+days]
        lb.configure(text = str(days+1))
        lb.grid(column = (day_of_week+days)%7, row = 3 + (days+day_of_week)//7)


current_month = date.month
current_year = date.year

days_in_month = monthrange(current_year,current_month)
day_of_week = datetime.date(current_year,current_month,1).weekday()
ShowMonth(days_in_month,day_of_week)


    



import tkinter as tk
import datetime
from calendar import monthrange 


root = tk.Tk()

root.geometry("500x500")

root.title("Calandar")

d = datetime.date.today()

prev_Month = tk.Button(root,text = "Previous")

prev_Month.grid(column = 0, row = 0)

next_Month = tk.Button(root,text = "Next")

next_Month.grid(column = 6, row = 0)

month = d.strftime("%B")
month_label = tk.Label(root,text = month)
month_label.grid(column=0,row=1,columnspan=6)

days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
for day in days:
    db = tk.Label(root,text = day)
    db.grid(column = days.index(day),row = 2)

days_in_month = monthrange(d.year,d.month)
print(days_in_month)
print(type(days_in_month[1]))
day_of_week = datetime.date(d.year,d.month,1).weekday()
print(day_of_week)
print(type(day_of_week))



date_labels = []
def ShowMonth(mon):
    date_labels.clear()
    for days in range(days_in_month[1]):
        lb = tk.Label(root,text = str(days+1))
        lb.grid(column = (day_of_week+days)%7, row = 3 + (days+day_of_week)//7)
        date_labels.append(lb)


import tkinter as tk
import datetime
import calendar
import pickle
import os

class ToDoItem:
    def __init__(self,description,due_date):
        self.description = description
        self.registered_date = datetime.date.today()
        self.due_date = due_date
        self.completed = False
        self.completed_date = None

    def Complete(self):
        self.completed = True
        self.completed_date = datetime.date.today()

    def __repr__(self):
        return self.due_date.isoformat() + " " + self.description + " " \
               + "(" + str(self.completed) +")"

file_name = "ToDoList.dat"
todo_dictionary = {}

if os.path.isfile(file_name) and os.path.getsize(file_name):
    file = open(file_name,"rb")
    todo_dictionary = pickle.load(file)
    file.close()
    print(todo_dictionary)
else:
    file = open(file_name,"wb")
    file.close()

root = tk.Tk()

root.geometry("600x500")

root.title("Calandar")

date = datetime.date.today()

def NextMonth():
    #print("next")
    global current_month
    global current_year
    global month_label
    global monthVar
    current_month += 1
    if current_month > 12:
        current_month = 1
        current_year += 1
    #print(current_month)
    days_in_month = calendar.monthrange(current_year,current_month)
    day_of_week = datetime.date(current_year,current_month,1).weekday()
    monthVar.set(months[current_month-1])
    ShowMonth(days_in_month,day_of_week)


def PreviousMonth():
    #print("previous")
    global current_month
    global current_year
    global month_label
    current_month -= 1
    if current_month < 1:
        current_month = 12
        current_year -= 1
    days_in_month = calendar.monthrange(current_year,current_month)
    day_of_week = datetime.date(current_year,current_month,1).weekday()
    monthVar.set(months[current_month-1])
    ShowMonth(days_in_month,day_of_week)

def Set(*arg):
    #print(monthVar.get())
    #print(months.index(monthVar.get()))
    current_month = months.index(monthVar.get())+1
    days_in_month = calendar.monthrange(current_year,current_month)
    day_of_week = datetime.date(current_year,current_month,1).weekday()
    ShowMonth(days_in_month,day_of_week)
    


prev_Month = tk.Button(root,text = "Previous", command = PreviousMonth)

prev_Month.grid(column = 0, row = 0)

next_Month = tk.Button(root,text = "Next", command = NextMonth)

next_Month.grid(column = 6, row = 0)

month = date.strftime("%B")
monthVar = tk.StringVar()
monthVar.set(month)
months = list(calendar.month_name)
months.pop(0)
month_label = tk.OptionMenu(root,monthVar,*months,command = Set)
month_label.grid(column=0,row=1,columnspan=6)

days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
for day in days:
    db = tk.Label(root,text = day)
    db.grid(column = days.index(day),row = 2)

# 0,  1,  2,  3,  4,  5,  6
# 7,  8,  9,  10, 11, 12, 13,
# 14, 15, 16, 17, 18, 19, 20,
# 21, 22, 23, 24, 25, 26, 27,
# 28, 29, 30, 31, 32, 33, 34
date_buttons = []
for da in range(36):
    lb = tk.Button(root,text = "")
    date_buttons.append(lb)

def ShowMonth(days_in_month,day_of_week):
    if len(date_buttons) > 0:
        for da in date_buttons:
            da.configure(text = "")
            da.grid_forget()
    for days in range(days_in_month[1]):
        lb = date_buttons[day_of_week+days-1]
        lb.configure(text = str(days+1),command = lambda d = (days+1): ShowDaysToDoItems(d))
        lb.grid(column = (day_of_week+days)%7, row = 3 + (days+day_of_week)//7)


current_month = date.month
current_year = date.year

days_in_month = calendar.monthrange(current_year,current_month)
day_of_week = datetime.date(current_year,current_month,1).weekday()
ShowMonth(days_in_month,day_of_week)

def Hide():
    global frame
    global entry
    global hidebtn
    global btn
    for x in frame.winfo_children():
        x.destroy()
    entry.delete(0,len(entry.get()))
    entry.grid_forget()
    btn.grid_forget()
    hidebtn.grid_forget()
    hidebtn.update()

entry = tk.Entry(root)
btn = tk.Button(root,text = "Register todo item")
hidebtn = tk.Button(root,text = "Hide todo items",command = Hide)
frame = tk.Frame(root)



def ShowDaysToDoItems(day):
    date = datetime.date(current_year,current_month,day)
    for td in todo_dictionary[date]:
        lb = tk.Label(frame,text = td.description)
        lb.pack()
    frame.grid(column = 7, row = 3, rowspan = 7)
    ShowRegisterButtons(day)
    

def ShowRegisterButtons(day):
    global entry
    global btn
    btn.configure(command = lambda d = day: RegisterNewToDoItem(d))
    entry.grid(column = 8, row = 3)
    btn.grid(column = 9, row = 3)
    hidebtn.grid(column = 9, row = 4)

def RegisterNewToDoItem(day):
    global entry
    global btn
    global hidebtn
    global frame
    tdl = ToDoItem(entry.get(),datetime.date(current_year,current_month,day))
    if tdl.due_date in todo_dictionary:
        todo_dictionary[tdl.due_date].append(tdl)
    else:
        l = [tdl]
        todo_dictionary[tdl.due_date] = l
    print("registered")
    print(todo_dictionary)
    file = open(file_name,"wb")
    pickle.dump(todo_dictionary,file)
    file.close()
    
    Hide()

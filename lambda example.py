import tkinter as tk


root = tk.Tk()

root.geometry("500x500")

root.title("Lambda Example")

def ButtonPushed(btn_name):
    print(btn_name + " was pushed.")

btn = tk.Button(root,text = "Push me", command = lambda x = "Push me": ButtonPushed(x))
btn.pack()

btnTwo = tk.Button(root,text = "Don't push me", command = lambda x = "Don't push me": ButtonPushed(x))
btnTwo.pack()


s = input("blah bhal")

s_list = s.split("/")
date = datetime.date(int(s_list[0]),int(s_list[1]), int(s_list[2]))

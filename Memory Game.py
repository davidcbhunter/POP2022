import tkinter as tk
import random
import winsound

#make a Trump class
class Trump:
    def __init__(self,btn,b_file_name,f_file_name,t_name):
        self.button = btn
        self.trump_back_file_name = b_file_name
        self.trump_front_file_name = f_file_name
        self.trump_name = t_name
        self.is_showing_face = False

# create a window    
root = tk.Tk()

root.geometry("512x512")
#root.configure(title = "Memory Game")

btn = tk.Button(root)
btn.place(x = 0, y = 0)

t = Trump("b","b.txt","f.txt","Ace of Clubs")

#let's print the information in t
print(t.button)
print(t.trump_back_file_name)
print(t.trump_front_file_name)
print(t.trump_name)
print(t.is_showing_face)




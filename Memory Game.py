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
        self.button.configure(text = "back")

    def Flip(self):
        
        self.is_showing_face = not self.is_showing_face
        if self.is_showing_face == False:
            #back_image = tk.PhotoImage(file = self.trump_back_file_name)
            #self.button.configure(image = back_image)
            #self.button.image = back_image
            self.button.configure(text = "Back")
        else:
            #self.is_showing_face = False
            self.button.configure(text = self.trump_name)
            #self.button.image = None
            
        

# create a window    
root = tk.Tk()

root.geometry("512x512")
#root.title("Memory Game")

back_image = tk.PhotoImage(file = "playing card back.png")

def LoadCards():
    cards = []
    file = open("Trumps.txt","r")
    data = file.read()
    file.close()
    
    cards = data.split(", ")

    return cards

cards = LoadCards()
#for c in cards:
#    print(c)

number_of_columns = 5
number_of_rows = 4
card_width = 113
x_offset = 129
x_spacing = 50

card_height = 166
y_offset = 105
y_spacing = 50

number_of_cards = number_of_rows * number_of_columns

number_of_unique_cards = number_of_cards // 2

random.shuffle(cards)



for x in range(number_of_cards):
    x_pos = x_offset + (x % number_of_columns)*card_width +\
            (x % number_of_columns)*x_spacing
    
    y_pos = y_offset + (x // number_of_columns)*card_height +\
            (x // number_of_columns)*y_spacing
    btn = tk.Button(root)#,image = back_image,compound = "center")
    btn.place(x = x_pos, y = y_pos)

    t = Trump(btn,"playing card back.png","f.txt",cards[x])
    btn.configure(command = t.Flip)

#btn = tk.Button(root)#,image = back_image,compound = "center")
#btn.place(x = 0, y = 0)

#card size is 113 by 166

#t = Trump(btn,"playing card back.png","f.txt","Ace of Clubs")
#btn.configure(command = t.Flip)

#let's print the information in t
#print(t.button)
#print(t.trump_back_file_name)
#print(t.trump_front_file_name)
#print(t.trump_name)
#print(t.is_showing_face)




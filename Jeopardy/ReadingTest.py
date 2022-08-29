import tkinter as tk
import tkinter.font
import winsound
import time
import random

file = open("JeopardyQs.txt","r")
text = file.readlines()
file.close()

#line2 = text[1].split(",")
#print(line2[-1])


root = tk.Tk()

root.geometry("700x600")
root.configure(bg = "blue")

#load the images
image = tk.PhotoImage(file = "gj.png")
imagetwo = tk.PhotoImage(file = "sad cat.png")
bgimage = tk.PhotoImage(file = "gold.png")

#create the fonts
fo = tk.font.Font(family = "Helvetica", size = 24)
fotwo = tk.font.Font(family = "Helvetica", size = 28)



buttons = []

#returns a list of strings which is used for the button names 
def GetCategories(t):
    line1 = text[0].split(",")
    bn = []
    for c in line1:
        c = c.replace("\n","")
        bn.append(c)
    return bn

# returns 3 dictionaries
# a dictionary for the category names with a list of buttons
# a dictionary for the category names with lists of questions
# a dictionary for the category names with a list of bools (for answered or not)
def GetItems(t):
    cbd = {}
    cqd = {}
    answered = {}
    for n in button_names:
        cbd[n] = []
        cqd[n] = []
        answered[n] = []
        firstline = t[0].split(",")
        firstline[-1] = firstline[-1].replace("\n","")
        for x in range(len(t)-1):
            
            cbd[n].append(x+1)
            line = t[x+1].split(",")
            
            #print(line)
            item = line[firstline.index(n)].replace("\n","")
            cqd[n].append(item)
            answered[n].append(False)
    return cbd,cqd,answered

button_names = GetCategories(text)
category_buttons_dictionary, category_questions_dictionary, answered = GetItems(text)

# checks whether we have answered all the questions or not

def game_over():
    global answered
    for c in answered:
        #print(c)
        for a in answered[c]:
            #print(a)
            if not a:
                return False
    return True

index = -1
category = ""
selected_button = None
bgLabel = tk.Label(root,image = bgimage)
bgLabel.place(x = 0,y = 0)


# shows the question based on the button pressed
def Show(cat, ind, button):
    #print(cat)
    global category
    global index
    global selected_button
    selected_button = button
    index = ind
    category = cat
    var.set(category_questions_dictionary[cat][index])
    l = list(category_buttons_dictionary.keys())
    r = len(category_buttons_dictionary[l[0]])+1
    label.grid(row = r, column = 0,columnspan = 5)
    label.update()
    correct_button.configure(state = tk.NORMAL)
    incorrect_button.configure(state = tk.NORMAL)
    PlayThinkSound()

# disables the button and updates the answered dictionary    
def Correct():
    #print("Correct")
    PlayCorrectSound()
    #we also need to update the answered dictionary
    answered[category][index] = True
    global selected_button
    #print(selected_button['text'])
    buttons[buttons.index(selected_button)].configure(state = tk.DISABLED)
    
    var.set("")
    #print(answered[category][index])
    correct_button.configure(state = tk.DISABLED)
    incorrect_button.configure(state = tk.DISABLED)
    canvas = tk.Canvas(root, width = 250, height = 300)
    #we always need to offset this by half the size of the canvas or image
    #is it the canvas or the image?
    image_id = canvas.create_image(125,150,im = image)
    canvas.grid(column = 0,row = 9, columnspan = 5)
    label.grid_forget()
    label.update()
    canvas.update()
    if game_over():
        var.set("Game Over")
        label.update()
    ShowImage(canvas, image_id)


def ShowImage(canvas, image_id):
    time.sleep(3)
    canvas.itemconfigure(image_id,state = tk.HIDDEN)
    canvas.grid_forget() # this makes it invisible!!




    
def PlayCorrectSound():
    lis = ["58672__timtube__cheer-2.wav","333404__jayfrosting__cheer-2.wav","337000__tim-kahn__cheer-01.wav"]
    winsound.PlaySound(random.choice(lis), winsound.SND_ASYNC)

def PlayIncorrectSound():
    lis = ["572938__bloodpixelhero__error-3.wav","572936__bloodpixelhero__error.wav"]
    winsound.PlaySound(random.choice(lis), winsound.SND_ASYNC)

def PlayThinkSound():
    winsound.PlaySound("Jeopardy.wav", winsound.SND_ASYNC)


def Incorrect():
    #print("Incorrect")
    var.set("")
    #we only disable the button if it is the 1st, 2nd or 4th category
    if category == button_names[0] or category == button_names[1] or \
       category == button_names[3]:
        answered[category][index] = True
        buttons[buttons.index(selected_button)].configure(state = tk.DISABLED)
    correct_button.configure(state = tk.DISABLED)
    incorrect_button.configure(state = tk.DISABLED)
    canvas = tk.Canvas(root, width = 250, height = 300)
    #we always need to offset this by half the size of the canvas or image
    #is it the canvas or the image?
    image_id = canvas.create_image(125,150,im = imagetwo)
    canvas.grid(column = 0,row = 9, columnspan = 5)
    canvas.update()
    label.grid_forget()
    label.update()
    PlayIncorrectSound()
    if game_over():
        var.set("Game Over")
        label.update()
    ShowImage(canvas, image_id)

l = tk.Label(root)
l.grid(row = 0, column = 0)

# creates the buttons for each category, and for each difficulty level
for n in button_names:
    btn = tk.Button(root,text = n, font = fo, state = tk.DISABLED, disabledforeground = "white", bg = "blue")
    buttons.append(btn)
    btn.grid(row = 0, column = button_names.index(n)+1)
    for num in category_buttons_dictionary[n]:
        btn = tk.Button(root,text = "$" + str(200*num), font = fo, bg = "blue", fg = "yellow")
        btn.configure(command= lambda n = n, \
                      num = category_buttons_dictionary[n].index(num), btn = btn: Show(n,num,btn))
        buttons.append(btn)
        btn.grid(row = 1 + category_buttons_dictionary[n].index(num), column = button_names.index(n)+1, sticky = tk.E + tk.W)


#print(category_dictionary[button_names[0]])
var = tk.StringVar()
var.set("")
label = tk.Label(root, textvariable = var, font = fotwo, wraplength = 600)

l = list(category_buttons_dictionary.keys())
r = len(category_buttons_dictionary[l[0]])+2

#creates the correct button
correct_button = tk.Button(root,text = "Correct", font = fo, state = tk.DISABLED,command= lambda: Correct())
correct_button.grid(row = r, column = 2)

#creates the incorrect button
incorrect_button = tk.Button(root,text = "Incorrect", font = fo,state = tk.DISABLED, command= lambda: Incorrect())
incorrect_button.grid(row = r, column = 3)

import tkinter as tk
import tkinter.font
import winsound
import time
import random


root = tk.Tk()

root.geometry("700x600")
root.configure(bg = "blue")

image = tk.PhotoImage(file = "gj.png")
imagetwo = tk.PhotoImage(file = "sad cat.png")
bgimage = tk.PhotoImage(file = "gold.png")
fo = tk.font.Font(family = "Helvetica", size = 20)
#tk.Grid.columnconfigure(root,0,weight=1)
#tk.Grid.columnconfigure(root,1,weight=1)
#tk.Grid.columnconfigure(root,2,weight=1)
#tk.Grid.columnconfigure(root,3,weight=1)
#tk.Grid.columnconfigure(root,4,weight=1)
#tk.Grid.columnconfigure(root,5,weight=1)
#tk.Grid.rowconfigure(root, 1, weight = 1)


buttons = []

button_names = ["Subject-Verb Agreement","Pronouns","Wacky English", \
                "Noun Versus Verb","Japan Studies", "Home Economics"]

category_buttons_dictionary = {button_names[0]: [1,2,3,4,5], button_names[1]: [1,2,3,4,5],\
                               button_names[2]: [1,2,3,4,5], button_names[3]: [1,2,3,4,5],\
                               button_names[4]: [1,2,3,4,5], button_names[5]: [1,2,3,4,5]}
category_questions_dictionary = {button_names[0]: \
                                  ["Jenny and her friend ___ (go) to English class every day."\
                                   ,"Henry never __ (eat) breakfast.",\
                                   "You __ (like) reading manga.","Tammy __ (study) math on Wednesday.",\
                                   "Christy __ (love) listening to Taylor Swift."],\
                                 button_names[1]: \
                                  ["(She/Her) favorite food is Cobb salad."\
                                   ,"(I/My) friend\'s name is Brian.",\
                                   "Tom is not nice. You see that boy? Tom kicked (him/he)."\
                                   ,"My dog\'s name is Angel. She is very cute. I like to play with (her/she)."\
                                   ,"Tony and his mother like to swim. (They/Them/Their) swim every Sunday."],
                                 button_names[2]: \
                                  ["This word can mean both 'two times a week' and 'one time every two weeks.'"\
                                   ,"This phrase means to rain very heavily.",\
                                   "The meaning of the phrase 'can't do ~~~ to save my life'",\
                                   "The meaning of the phrase 'play it by ear'",\
                                   "This word can mean both 'to read slowly and carefully' and 'to read quickly'"], \
                                   button_names[3]: \
                                  ["Rachel (decided / decision) to study Spanish."\
                                   ,"I want to converse / conversation with foreign people.",\
                                   "That idea has a lot of (attracted / attraction) for me",\
                                   "She gave a great (performance / perform) at the concert last night.",\
                                   "That company (specializes / specialization) in office furniture."],\
                                 button_names[4]: \
                                  ["'The park is over there.' What kind of there is this (pointing, existing, or place)"\
                                   ,"Altitude/Elevation means ???",\
                                   "Latitude means ???",\
                                   "Say 45,374,190",\
                                   "'There are many cute cats there.'What are these two there's"],\
                                 button_names[5]: \
                                  ["Homosexual marriage is allowed in Japan. T/F"\
                                   ,"Name one of Breslow's 7 healthy habits.",\
                                   "The title/name of the woman who is getting married's friends",\
                                   "One of the types of child abuse",\
                                   "Mr. Hunter lives together with his wife. What kind of family is this?"]}

answered = {button_names[0]: [False,False,False,False,False], \
            button_names[1]: [False,False,False,False,False],\
            button_names[2]: [False,False,False,False,False],\
            button_names[3]: [False,False,False,False,False],\
            button_names[4]: [False,False,False,False,False],\
            button_names[5]: [False,False,False,False,False]}
#print(category_questions_dictionary[button_names[0]][0])

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

def Show(cat, ind, button):
    #print(cat)
    global category
    global index
    global selected_button
    selected_button = button
    index = ind
    category = cat
    var.set(category_questions_dictionary[cat][index])
    label.grid(row = 6, column = 0,columnspan = 5)
    label.update()
    correct_button.configure(state = tk.NORMAL)
    incorrect_button.configure(state = tk.NORMAL)
    PlayThinkSound()
    
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

for n in button_names:
    btn = tk.Button(root,text = n, font = fo, state = tk.DISABLED, disabledforeground = "white", bg = "blue")
    buttons.append(btn)
    btn.grid(row = 0, column = button_names.index(n))
    for num in category_buttons_dictionary[n]:
        btn = tk.Button(root,text = "$" + str(100*num), font = fo, bg = "blue", fg = "yellow")
        btn.configure(command= lambda n = n, \
                      num = category_buttons_dictionary[n].index(num), btn = btn: Show(n,num,btn))
        buttons.append(btn)
        btn.grid(row = 1 + category_buttons_dictionary[n].index(num), column = button_names.index(n), sticky = tk.E + tk.W)


#print(category_dictionary[button_names[0]])
var = tk.StringVar()
var.set("")
label = tk.Label(root, textvariable = var, font = fo, wraplength = 400)

correct_button = tk.Button(root,text = "Correct", font = fo, state = tk.DISABLED,command= lambda: Correct())
correct_button.grid(row = 7, column = 2)

incorrect_button = tk.Button(root,text = "Incorrect", font = fo,state = tk.DISABLED, command= lambda: Incorrect())
incorrect_button.grid(row = 7, column = 3)

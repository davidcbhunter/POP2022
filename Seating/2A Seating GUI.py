import tkinter as tk
import tkinter.font
import random
import winsound

students = ["Chinami Akiyama","Haruna Ishii","Misumi Ishii",\
            "Rino Ishikura","Yui Iwaki","Hiiro Umino","Arina Ohashi",\
            "Nana Ogura","Miyu Katayanagi","Kinari Sakamoto",\
            "Hinata Sato","Sara Takeda","Sakura Tanaka","Haruna Nagata",\
            "Yuri Nakachi","Ai Hatekeyama","Moeri Minori","Sara Yanagibara",\
            "Moeka Yamazaki","Paolina Zanner","Elise Tazawa-Lim"]

root = tk.Tk()

fo = tk.font.Font(family = "Helvetica", size = 18)

root.geometry("1000x800")
root.title("2A Seating")

bgimage = tk.PhotoImage(file = "wood floor.png")

deskimage = tk.PhotoImage(file = "chair and desk.png")

wl = 120

bgLabel = tk.Label(root,image = bgimage)
bgLabel.place(x = 0,y = 0)

desks = []
currentIndex = 0
def CreateDesks():
    global desks
    c = 1
    r = 4
    for s in students:
        deskLabel = tk.Button(root, font = fo,image = deskimage,\
            text = s, compound = "center",wraplength = wl)
        deskLabel.grid(column = r,row = c, padx = 10, pady = 10)
        desks.append(deskLabel)
        
        c += 1

        if c > 5:
            r -=1
            c = 1
        if r < 0:
            r = 4

currentStudent = 0
first = True
c = 1
r = 4

studentsCopy = students.copy()
ra = []
raIndex = 0
studentCopy = students.copy()
random.shuffle(studentsCopy)

def Randomize():
    global ra
    global studentCopy
    global raIndex
    ra.clear()
    raIndex = 0
    random.shuffle(studentsCopy)
    for s in studentsCopy:
        ra.append(students.index(s))

    
def GetRandom():
    global desks
    global raIndex
    global studentsCopy
    global ra
    for d in desks:
        d.configure(bd=0,bg="white")
        d.update()
    desks[studentsCopy.index(students[raIndex])].configure(bd=5,bg="red")
    raIndex += 1
    winsound.PlaySound("trumpets.wav", winsound.SND_ASYNC)
    if raIndex >= len(desks):
        Randomize()

frontLabel = tk.Label(root, font = fo,text = "Front", compound = "center",wraplength = wl)
frontLabel.grid(column = 0,row = 0, sticky = "ew", columnspan = 6,padx = 10, pady = 10)

getRandom = tk.Button(root, font = fo,text = "Get Random", command = GetRandom)
getRandom.grid(column = 5,row = 2,padx = 10, pady = 10)

CreateDesks()


root.mainloop()

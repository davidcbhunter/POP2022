import tkinter as tk
import tkinter.font
import random
import pickle
import winsound

rows = [["","","","",""],["","","","","",],["","","","","",],\
        ["","","","",""],["","","","",""],["","","","",""],\
        ["","","","",""]]

students = ["Momoka Isogai","Mei Inoue","Yuri Ebihara",\
            "Emi Okawa","Kaede Okuma","Rino Otsuka", "Yukika Ozaki",\
            "Haru Ozasa","Ari Kato", "Anri Kawabe", "Miu Kawamata",\
            "Haruka Kigoshi","Mamika Kubo", "Aoi Kobayashi",\
            "Haruka Kobayashi","Rino Sasaki", "Aoi Takashima",\
            "An Takahashi", "Hina Takahashi", "Sana Dasic","Konoha Terui",\
            "Aoi Tokumaru", "Miya Harashima", "Riona Fukasawa",\
            "Naru Maekawa", "Wako Mizuno", "Koharu Murayama",\
            "Caitlyn Yamasaki", "Risa Yamazaki", "Saki Yoshikawa",\
            "Kohaku Watanabe" , "Magrat Gaudlitz"]



root = tk.Tk()

fo = tk.font.Font(family = "Helvetica", size = 18)

root.geometry("1000x800")

bgimage = tk.PhotoImage(file = "wood floor.png")

deskimage = tk.PhotoImage(file = "chair and desk.png")

wl = 120

bgLabel = tk.Label(root,image = bgimage)
bgLabel.place(x = 0,y = 0)


desks = []
currentIndex = 0

studentNumberStr = tk.StringVar()
studentNumberStr.set("")


def DisplaySet(index):
    global currentIndex
    global entry
    currentIndex = index
    entry.grid(column = 6, row = 3)

def Set(event):
    global studentNumberStr
    global entry
    global desks
    global rows
    previousS = desks[currentIndex].cget("text")
    desks[currentIndex].configure(text = students[int(studentNumberStr.get())-1])
    desks[currentIndex].update()
    #we also need to update the rows
    column = 0
    row = 0
    #print(currentIndex)
    if currentIndex >= 12:
        column = (currentIndex-1)//6
    else:
        column = currentIndex//6
    
        
    if currentIndex != 31:
        row = currentIndex % 6
        if currentIndex > 12:
            row -= 1
        if row < 0:
            row = 5
        if currentIndex == 12:
            row = 6
    else:
        row = 6
        column = 2
    
    # reverse the column
    column = 4 - column
    for r in rows:
        backwards = []
        for b in reversed(r):
            backwards.append(b)
        for c in backwards:
            if c == students[int(studentNumberStr.get())-1]:
                #print(rows.index(r))
                #print(backwards.index(c))
                rows[rows.index(r)][r.index(c)] = previousS
                index = GetCorrectIndex(c,backwards,r)
                desks[index].configure(text = previousS)
    rows[row][column] = students[int(studentNumberStr.get())-1]
    #print(rows)
    studentNumberStr.set("")
    entry.grid_forget()
    winsound.PlaySound("school_desk_scrape.wav", winsound.SND_ASYNC)

entry = tk.Entry(root,textvariable = studentNumberStr)
entry.bind("<KeyRelease-Return>",Set)

def CreateDesks():
    global desks
    c = 1
    r = 4
    for s in students:
        if (c == 7 and r == 3) or c < 7 and\
            students.index(s) != 31:
            deskLabel = tk.Button(root, font = fo,image = deskimage,\
                text = "", compound = "center",wraplength = wl)
            deskLabel.grid(column = r,row = c, padx = 10, pady = 10)
            desks.append(deskLabel)
            deskLabel.configure(command = lambda i = desks.index(deskLabel): DisplaySet(i))
                #rows[column][row] = s
        elif students.index(s) == 31:
            deskLabel = tk.Button(root, font = fo,image = deskimage,\
                text = "", compound = "center",wraplength = wl)
            deskLabel.grid(column = r,row = c, padx = 10, pady = 10)
            desks.append(deskLabel)
            deskLabel.configure(command = lambda i = desks.index(deskLabel): DisplaySet(i))
            
            deskLabel = tk.Button(root, font = fo,image = deskimage,\
                text = "", compound = "center",wraplength = wl)
            deskLabel.grid(column = 2,row = 7, padx = 10, pady = 10)
            desks.append(deskLabel)
            deskLabel.configure(command = lambda i = desks.index(deskLabel): DisplaySet(i))
        
        c += 1

        if ((r == 3 or r == 2) and c > 7) \
           or (r != 3 and r != 2 and c > 6):
            r -=1
            c = 1
        if r < 0:
            r = 4

currentStudent = 0
first = True
c = 1
r = 4
studentsCopy = students.copy()

def MoveOne():
    global currentStudent
    global studentsCopy
    global c
    global r
    global first
    global desks
    global moveOne
    if first:
        random.shuffle(studentsCopy)
        first = False
        for d in desks:
            d.configure(text = "")
            d.update()
    if (c == 7 and r == 3)\
        or c < 7 and currentStudent != 31:
        desks[currentStudent].configure(text = studentsCopy[currentStudent])
        desks[currentStudent].update()
        #deskLabel = tk.Label(root, font = fo,image = deskimage,\
        #    text = students[currentStudent], compound = "center",wraplength = wl)
        #deskLabel.grid(column = r,row = c, padx = 10, pady = 10)
        rows[c-1][r] = studentsCopy[currentStudent]
        #desks.append(deskLabel)
                #rows[column][row] = s
    elif currentStudent == 31:
        desks[currentStudent].configure(text = studentsCopy[currentStudent])
        desks[currentStudent].update()
        rows[6][2] = studentsCopy[currentStudent]
    currentStudent += 1

    c += 1
    if (r == 3 and c > 7) \
           or (r == 2 and c > 6)\
           or (r != 3 and r != 2 and c > 6):
        r -=1
        c = 1
    if r < 0:
        r = 4

    if currentStudent == 32:
        moveOne.configure(state = tk.DISABLED)
    winsound.PlaySound("school_desk_scrape.wav", winsound.SND_ASYNC)

def GetCorrectIndex(stu, roBack,r):
    index = rows.index(r)
    if roBack.index(stu) == 1:
        index += 6
    if roBack.index(stu) == 2:
        index += 13
    if roBack.index(stu) == 3:
        index += 19
    if roBack.index(stu) == 4:
        index += 25

    if roBack.index(stu) == 2 and rows.index(r) == 6:
        index = 31
    return index

def ShowDefault():
    global desks
    global moveOne
    global currentStudent
    currentStudent = 0
    global first
    first = True
    global c
    global r
    moveOne.configure(state = tk.NORMAL)
    c = 1
    r = 4
    for s in students:
        if (c == 7 and r == 3) or c < 7 and\
            students.index(s) != 31:
            desks[students.index(s)].configure(text = s)
            desks[students.index(s)].update()
            rows[c-1][r] = s

            
        elif students.index(s) == 31:
            desks[31].configure(text = s)
            desks[31].update()
            rows[6][2] = s
            
        c += 1

        if (r == 3 and c > 7) \
           or (r == 2 and c > 6)\
           or (r != 3 and r != 2 and c > 6):
            r -=1
            c = 1
        if r < 0:
            r = 4
            
    c = 1
    r = 4
    
def Load():
    global desks
    global rows
    file = open("1A Seating Test.txt","rb")

    rows = pickle.load(file)
    #print(rows)
    file.close()

    for r in rows:
        backwards = []
        for b in reversed(r):
            backwards.append(b)
        for c in backwards:
            if c != "":
                #print(rows.index(r))
                #print(backwards.index(c))
                #print(c)
                #index = backwards.index(c)*6+rows.index(r)
                #print(index+1)
                index = GetCorrectIndex(c,backwards,r)
                desks[index].configure(text = c)
                
def Save():
    file = open("1A Seating Test.txt","wb")

    pickle.dump(rows,file)

    file.close()

ra = []
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
    if raIndex >= len(desks):
        raIndex = 0
        random.shuffle(studentsCopy)
        ra.clear()
        for s in studentsCopy:
            ra.append(students.index(s))
            
frontLabel = tk.Label(root, font = fo,text = "Front", compound = "center",wraplength = wl)
frontLabel.grid(column = 0,row = 0, sticky = "ew", columnspan = 6,padx = 10, pady = 10)


CreateDesks()

#moveAll = tk.Button(root, font = fo,text = "Move All", command = CreateDesks)
#moveAll.grid(column = 5,row = 5, rowspan = 5)

moveOne = tk.Button(root, font = fo,text = "Move One", command = MoveOne)
moveOne.grid(column = 5,row = 6, padx = 10, pady = 10)

showDefault = tk.Button(root, font = fo,text = "Show Default", command = ShowDefault)
showDefault.grid(column = 5,row = 7, padx = 10, pady = 10)

load = tk.Button(root, font = fo,text = "Load", command = Load)
load.grid(column = 5,row = 3, padx = 10, pady = 10)

save = tk.Button(root, font = fo,text = "Save", command = Save)
save.grid(column = 5,row = 4, padx = 10, pady = 10)

getRandom = tk.Button(root, font = fo,text = "Get Random", command = GetRandom)
getRandom.grid(column = 5,row = 2,padx = 10, pady = 10)

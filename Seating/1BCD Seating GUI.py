import tkinter as tk
import tkinter.font
import random
import winsound

elective_rows = [["","","","","",""],["","","","","",""],["","","","","",""],\
        ["","","","","",""],["","","","","",""],["","","","","",""],\
        ["","","","","",""]]

regular_rows = [["","","","",""],["","","","",""],["","","","",""],\
        ["","","","",""],["","","","",""],["","","","",""],\
        ["","","","",""]]

s_students = ["Hano Kusaka","Yuma Sato","Sara Shirai","Yuuna Tachikawa",
              "Himawari Tohyama","Misaki Nishimura","Rinko Hasegawa",\
              "Nanaha Murase","Yuna Yoshida","Yuu Watanabe","Hikari Ishihara",\
              "Mitsuki Iwasaki", "Shiori Ueno", "Kureha Uemoto", "Yuuka Ohtake",\
              "Haruka Kimura", "Kana Takahashi", "Nanami Torii", "Midori Nakamura",\
              "Chio Nagoshi", "Yurina Hasegawa", "Yuzuki Hirata", "Maki Isogai",\
              "Misuzu Inoue", "Mei Iwasaki", "Haruka Oda", "Tsukuyomi Katou", \
              "Azuki Kudou", "Ayame Takahashi","Minami Nishioka", "Mayu Morimoto",\
              "Mayu Yamamoto","Haruka Watanabe"]

alpha_students = ["Kaya Icchouda","Riona Ogata","Runa Kajiwara","Vivian Aine Goto",\
                  "Ichika Sawada","Yukino Shirakawa", "Renka Tsukakoshi","Riko Nakamura",\
                  "Yuina Funatsu", "Miyuu Maruyama","Shiori Morino","Haruka Yasumoto",\
                  "Kanon Asahi", "Suzuha Imamura", "Miyuu Kaneko","Kokomi Kawamata",\
                  "Miina Kume","Noi Kobayashi", "Chikako Shiina", "Rino Sudou",\
                  "Kiho Nanba", "Misaki Yabuhara", "Miya Ieemon", "Mizuki Ohsawa",\
                  "Shino Kamiya", "Setare Kobayashi", "Rio Takahashi", "Aimi Nakada",\
                  "Ramu Hirako", "Hina Yasui", "Honoka Yamada", "Kaede Watanabe"]

beta_students = ["Yuna Aoki", "Yuuka Urano", "Mio Goto", "Kanade Kobayashi",\
                 "Karen Kobayahsi", "Rin Sato", "Hinano Toyama","Sou Fujita",\
                 "Mio Motomatsu","Chika Yanagi", "Airi Okazaki", "Tomoka Kazama",\
                 "Ririka Suzuki", "Namika Suda", "Haruka Tanaka", "Narumi Tsurumaki",\
                 "Kanon Nagase", "Tsumugi Nakano", "Saki Matsuda", "Ayana Muneta",\
                 "Hiroka Aoki", "Haruka Itou", "Sayaka Ogura", "Makoto Komasaka", \
                 "Mei Koyama", "Jasmine Kondou", "Ayano Suzuki", "Wakana Suzuki",\
                 "Chiharu Degami", "Raki Nakamura", "Akane Matsuzaki"]

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
studentsCopy = []

class_name = tk.StringVar()
class_name.set("")
cn = ""

elective_column_number = 6
regular_column_number = 5

elective_row_number = 6
regular_row_number = 7


def SelectClass():
    global entry
    entry.grid(column = 7, row = 3)

def Set(event):
    global class_name
    global entry
    global desks
    global rows
    global cn
    cn = class_name.get()
    if class_name.get() == "s":
        CreateDesks(s_students)
    elif class_name.get() == "a":
        CreateDesks(alpha_students)
    elif class_name.get() == "b":
        CreateDesks(beta_students)
    class_name.set("")
    entry.grid_forget()
    

entry = tk.Entry(root,textvariable = class_name)
entry.bind("<KeyRelease-Return>",Set)

def CreateDesks(students):
    global desks
    if len(desks) > 0:
        for d in desks:
            d.destroy()
            d.update()
        desks.clear()
    global studentsCopy

    studentsCopy.clear()
    
    c = 1
    if cn == "s":
        r = elective_column_number-1
        print(r)
    elif cn == "a" or cn == "b":
        r = regular_column_number-1
    
    for s in students:
        deskLabel = tk.Button(root, font = fo,image = deskimage,\
        text = s, compound = "center",wraplength = wl)
        deskLabel.grid(column = r,row = c, padx = 10, pady = 10)
        desks.append(deskLabel)
        studentsCopy.append(s)
        
        c += 1
        if cn == "s":
            if c > elective_row_number:
                r -=1
                c = 1
        elif cn == "a" or cn == "b":
            if c > regular_row_number:
                r -=1
                c = 1


        if r < 0:
            if cn == "s":
                r = elective_column_number-1
            elif cn == "a" or cn == "b":
                r = regular_column_number-1
    Randomize()

currentStudent = 0
first = True
c = 1
if cn == "s":
    r = elective_column_number-1
elif cn == "a" or cn == "b":
    r = regular_column_number-1


ra = []
raIndex = 0

def Randomize():
    global ra
    global studentCopy
    global raIndex
    ra.clear()
    raIndex = 0
    random.shuffle(studentsCopy)
    for s in studentsCopy:
        if cn == "s":
            ra.append(s_students.index(s))
        elif cn == "a":
            ra.append(alpha_students.index(s))
        elif cn == "b":
            ra.append(beta_students.index(s))
        
def GetRandom():
    global desks
    global raIndex
    global studentsCopy
    global ra
    for d in desks:
        d.configure(bd=0,bg="white")
        d.update()
    if cn == "s":
        desks[studentsCopy.index(s_students[raIndex])].configure(bd=5,bg="red")
    elif cn == "a":
        desks[studentsCopy.index(alpha_students[raIndex])].configure(bd=5,bg="red")
    elif cn == "b":
        desks[studentsCopy.index(beta_students[raIndex])].configure(bd=5,bg="red")
    raIndex += 1
    winsound.PlaySound("trumpets.wav", winsound.SND_ASYNC)
    if raIndex >= len(desks):
        Randomize()
            
            
frontLabel = tk.Label(root, font = fo,text = "Front", compound = "center",wraplength = wl)
frontLabel.grid(column = 0,row = 0, sticky = "ew", columnspan = 6,padx = 10, pady = 10)


#CreateDesks()
selectClass = tk.Button(root, font = fo,text = "Select Class", command = SelectClass)
selectClass.grid(column = 7,row = 7, padx = 10, pady = 10)

getRandom = tk.Button(root, font = fo,text = "Get Random", command = GetRandom)
getRandom.grid(column = 7,row = 2,padx = 10, pady = 10)

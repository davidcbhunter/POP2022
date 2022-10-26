import random

rows = [["","","","",""],["","","","","",],["","","","","",],\
        ["","","","",""],["","","","",""],["","","","",""],\
        ["","","","",""]]

students = ["Momoka Isogai","Mei Inoue","Yuri Ebihara",\
            "Emi Okawa","Kaede Okuma","Rino Otsuka", "Yukika Ozaki",\
            "Haru Ozasa","Ari Kato", "Anri Kawabe", "Miu Kawamata",\
            "Haruka Kigoshi","Mamika Kubo", "Aoi Kobayashi",\
            "Haruka Kobayashi","Rino Sasaki", "Aoi Takashima",\
            "An Takahashi", "Hina Takahashi", "Sana Dasic","Konoha Terui",\
            "Aoi Tokumaru", "Miya Harashima", "Riona Fukusawa",\
            "Naru Maekawa", "Wako Mizuno", "Koharu Murayama",\
            "Caitlyn Yamasaki", "Risa Yamazaki", "Saki Yoshikawa",\
            "Kohaku Watanabe" , "Magrat Gaudlitz"]

shuffle = True
if shuffle:
    random.shuffle(students)

row = 0
column = 0
for s in students:
    if shuffle: 
        if (column == 6 and (row == 1 or row == 2))\
        or column < 6:
            rows[column][row] = s
        else:
            pass
    else:
        if (column == 6 and row == 1) or column < 6 and\
           students.index(s) != 31:
            rows[column][row] = s
        elif students.index(s) == 31:
            rows[6][2] = s
    
    column += 1

    if ((row == 1 or row == 2) and column > 6) \
       or (row != 1 and row != 2 and column > 5):
        column = 0
        row +=1
    if row > 4:
        row = 0
    
#print(rows)
for r in rows:
    r.reverse()

row_string = ""
#print(rows)
for r in rows:
    rs = "{0:16} {1:16} {2:16} {3:16} {4:16}".format(r[0],r[1],r[2],r[3],r[4])
    row_string += rs
    row_string += "\n"

print("Windows \t\t\t\tBlack Board \t\t\t\tDoor".rjust(20," "))
print("\n")

print(row_string)
print("Door".rjust(85," "))

file = open("1A 3rd Quarter Seating.txt","w")

file.write(row_string)

file.close()

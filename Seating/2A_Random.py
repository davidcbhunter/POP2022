import random
import winsound

students = ["Chinami Akiyama","Haruna Ishii","Misumi Ishii",\
            "Rino Ishikura","Yui Iwaki","Hiiro Umino","Arina Ohashi",\
            "Nana Ogura","Miyu Katayanagi","Kinari Sakamoto",\
            "Hinata Sato","Sara Takeda","Sakura Tanaka","Haruna Nagata",\
            "Yuri Nakachi","Ai Hatekeyama","Moeri Minori","Sara Yanagibara",\
            "Moeka Yamazaki","Paolina Zanner","Elise Tazawa-Lim"]

shuffle = True
if shuffle:
    random.shuffle(students)

command = ""
current = 0
while command != "q":
    print("\n")
    print(students[current])
    winsound.PlaySound("trumpets.wav", winsound.SND_ASYNC)

    current += 1

    if current >= len(students):
        current = 0
        random.shuffle(students)
        print("Starting Over")
    print("\n")
    command = input("q to quit\n")

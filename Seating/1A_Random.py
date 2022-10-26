import random

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

command = ""
current = 0
while command != "q":
    print("\n")
    print(students[current])

    current += 1

    if current >= len(students):
        current = 0
        random.shuffle(students)
        print("Starting Over")
    print("\n")
    command = input("q to quit")

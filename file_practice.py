my_file = open("Movies.txt", "r",encoding="utf-8")


info = my_file.read()

my_file.close()

li = info.splitlines()

print(li)

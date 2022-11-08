my_file = open("Movies.txt", "r",encoding="utf-8")


info = my_file.read()

#check the type of info
#print(type(info))

my_file.close()

li = info.splitlines()

#check the type of li
#print(type(li))

#for loop --> prints each line in li

movie_dictionary = {}

for x in li:
    #print(x)
    sp = x.split(",")
    #print each item in sp
    #for s in sp:
    #    print(s)
    
    #check the type of x
    #print(type(x))
    #print(type(sp))
    #check the type of sp[0]
    #print(type(sp[0]))
    #check the type of sp[1]
    #print(type(sp[1]))
    
    movie_dictionary[int(sp[0])] = sp[1]

print(movie_dictionary[2017])


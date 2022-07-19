import datetime

family = ["David", "Kathy", "Michael"]

print(type(family))
print(type(family[0]))



number_of_students = [31,29,30,32,24,23,20,21,24,22,23,25]

print(type(number_of_students))
print(type(number_of_students[0]))

name = "David"
age = 400
likes_cats = True
favorite_number = 3.14159

me = [name,age,likes_cats,favorite_number]



me.append(2009)

me.append(datetime.date(1685,9,17))

me.remove(400)

me.insert(0,False)

me.pop(4)

print(me)

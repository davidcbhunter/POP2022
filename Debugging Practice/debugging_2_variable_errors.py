import datetime

writer1 = "Steven Erikson"
writer2 = "Robert Jordan"
writer3 = "Frank Herbert"


book1 = "The Gardens of the Moon"
book2 = "The Eye of the World"
book3 = "Dune"

date = datetime.date(1965,8,1)

#this should look this way:
# Steven Erikson wrote The Gardens of the Moon
print("writer1 wrote " + "book1.")

#this should look this way:
# The Eye of the World was written by Robert Jordan
print("book2 was written by " + "writer2.")

#this should look this way:
# Frank Herbert published Dune on August 1, 1965
#HINT: use the date function -> date.strftime("%B%e,%Y")
print("writer3 published book3 on date.")


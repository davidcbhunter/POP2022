import datetime

class My_Class:
    def __init__(self):
        self.name = ""
        self.number_of_students = 0
        self.dates = []

    def Add(self,n):
        self.number_of_students += n

c = My_Class()
c.name = "POP Programming"
c.number_of_students = 3
c.Add(2)

print(c.name)
print(c.number_of_students)

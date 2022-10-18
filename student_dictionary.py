import datetime

student_names = {111:"Sam Smith",112:"Jennifer Jones",113:"Susan Hill"}

student_birthdays = {111:datetime.date(1545,11,10),\
                     112:datetime.date(1685,2,14),\
                     113:datetime.date(1895,8,19)}

student_classes = {111:["Biology","Social Studies", "POP"],\
                   112:["Chemistry","French", "Algebra"],\
                   113:["English", "Japanese History", "Physics"]}


#use the key to get all the information about the student
info = student_names.get(113) + "\n" + str(student_birthdays.get(113)) \
       + "\n"+ str(student_classes.get(113))



print(info)

import datetime

bd = datetime.date(1982,11,10)


print(bd.weekday())

rock_climbing = datetime.date(2002,5,6)

t = datetime.date.today() - rock_climbing

print(t.days / 365)

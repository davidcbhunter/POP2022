import datetime

d = datetime.date(2022,8,27)


#write a function that checks if date
# is a weekday
def IsWeekday(date):
    #weekdays = [0,1,2,3,4]
    #return date.weekday() in weekdays
    return date.weekday() < 5

print(IsWeekday(d))

#write a function that checks if date
# is a weekend
def IsWeekend(date):
    return not IsWeekday(date)
    #return date.weekday() > 4


print(IsWeekend(d))


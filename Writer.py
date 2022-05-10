import datetime

first_name = "Steven"
last_name = "Erikson"
country = "Canada"
birthday = datetime.date(1965,6,10)
#birth_year = 1965
#birth_month = 6
#birth_day = 10
book = "The Malazon Book of the Fallen"
age = (datetime.date.today() - birthday).days/365
living = False
married = True
print(first_name)
print(last_name)
print(country)
#print(birth_year)
#print(birth_month)
#print(birth_day)
print(birthday)
print(age)
print(book)
print(living)
print(married)

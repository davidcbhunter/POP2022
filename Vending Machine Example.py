import datetime

product_list = ["Black Coffee","Milk Coffee",\
                "Apple Juice","Cola","Energy Drink"]

price_list = [130,130,160,160,220]

amount_list = [40,50,40,30,20]

money = 2000

class Product:
    def __init__(self,n,p,a,h,d):
        self.name = n
        self.price = p
        self.amount = a
        self.is_hot = h
        self.expiry_date = d


    def IsEnoughMoney(self,p):
        return self.price >= p

    def IsInStock(self):
        return self.amount > 0

    def IsSafe(self):
        return datetime.date.today() < self.expiry_date

    def Temperature(self):
        if self.is_hot:
            return "Hot"
        else:
            return "Cold"

#make the products and add them to the product list
happy_happy_drink = Product("Happy Happy Drink",50,10,False,datetime.date(2023,11,22))

black_coffee = Product("Black Coffee",40,200,True,datetime.date(2023,11,22))

energy_drink = Product("Genki",140,100,False,datetime.date(2023,11,22))

oolong_tea = Product("Oolong Tea",120,50,False,datetime.date(2023,11,22))

cola = Product("Craft Cola",150,60,True,datetime.date(2023,11,22))

products = [happy_happy_drink,black_coffee,energy_drink,oolong_tea,cola]


def ShowProducts():
    #we don't need global here because we are not changing the value
    # of the products or prices
    first_line_message = ""
    second_line_message = ""
    third_line_message = ""
    for x in products:
        first_line_message += x.name + "\t"
        second_line_message += x.Temperature() + "\t"
        third_line_message += str(x.price) + "\t"
        
    print(first_line_message)
    print(second_line_message)
    print(third_line_message)    

def IsProduct():
    #we don't need global here because we are not changing the value
    # of the products
    return current_product in product_list

def IsAmountEnough():
    return amount_list[product_index] > 0

def IsEnoughMoney():
    #price_list[product_index] <= current_money
    return current_money >= price_list[product_index]

def ShowMessage():
    if current_money > price_list[product_index]:
        #we only want to print the change message if the customer
        # gave us too much money.
        print("You have " + str(current_money-price_list[product_index]) + " yen in change.")
    print("Enjoy your " + current_product + ".")

def Buy():
    global amount_list
    global money
    amount_list[product_index] -= 1
    money += price_list[product_index]
    
    ShowMessage()

ShowProducts()

current_product = input("What product do you want to buy? \n")

if not IsProduct():
    print("Not a product.")
else:
    product_index = product_list.index(current_product)
    if not IsAmountEnough():
        print("Sorry. We are sold out.")
    else:
        current_money = int(input("Insert money. \n"))
        if not IsEnoughMoney():
            print("Not enough money.")
        else:
            Buy()

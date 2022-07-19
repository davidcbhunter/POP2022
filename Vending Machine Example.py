product1 = "Black Coffee"
product2 = "Milk Coffee"
product3 = "Apple Juice"
product4 = "Cola"
product5 = "Energy Drink"

price1 = 130
price2 = 130
price3 = 160
price4 = 160
price5 = 220

amount1 = 40
amount2 = 50
amount3 = 40
amount4 = 30
amount5 = 20

money = 2000

def ShowProducts():
    #we don't need global here because we are not changing the value
    # of the products or prices
    print(product1 + "\t" + product2 + "\t" + product3 + "\t" \
          + product4 + "\t" + product5)
    print(str(price1) + "\t\t" + str(price2) + "\t\t" + str(price3) + "\t\t" \
          + str(price4) + "\t" + str(price5))

def IsProduct():
    #we don't need global here because we are not changing the value
    # of the products
    return current_product == product1 or current_product == product2 \
   or current_product == product3 or current_product == product4 \
   or current_product == product5

def IsAmountEnough():
    return (current_product == product1 and amount1 > 0) or \
           (current_product == product2 and amount2 > 0) or \
           (current_product == product3 and amount3 > 0) or \
           (current_product == product4 and amount4 > 0) or \
           (current_product == product5 and amount5 > 0)

def IsEnoughMoney():
    return (current_product == product1 and current_money >= price1) or \
        (current_product == product2 and current_money >= price2) or \
        (current_product == product3 and current_money >= price3) or \
        (current_product == product4 and current_money >= price4) or \
        (current_product == product5 and current_money >= price5)

def ShowMessage(price):
    if current_money > price:
        #we only want to print the change message if the customer
        # gave us too much money.
        print("You have " + str(current_money-price) + " yen in change.")
    print("Enjoy your " + current_product + ".")

def Buy():
    global amount1
    global amount2
    global amount3
    global amount4
    global amount5
    global money
    if current_product == product1:
        amount1 -= 1
        money += price1
        ShowMessage(price1)
    if current_product == product2:
        amount2 -= 1
        money += price2
        ShowMessage(price2)
    if current_product == product3:
        amount3 -= 1
        money += price3
        ShowMessage(price3)
    if current_product == product4:
        amount4 -= 1
        money += price4
        ShowMessage(price4)
    if current_product == product5:
        amount5 -= 1
        money += price5
        ShowMessage(price5)

ShowProducts()

current_product = input("What product do you want to buy? \n")

if not IsProduct():
    print("Not a product.")
elif not IsAmountEnough():
    print("Sorry. We are sold out.")
else:
    current_money = int(input("Insert money. \n"))
    if not IsEnoughMoney():
        print("Not enough money.")
    else:
        Buy()

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

amount1 = 50
amount2 = 50
amount3 = 40
amount4 = 30
amount4 = 20

money = 2000

def ShowProducts():
    print(product1 + "\t" + product2 + "\t" + product3 + "\t" \
          + product4 + "\t" + product5)
    print(str(price1) + "\t\t" + str(price2) + "\t\t" + str(price3) + "\t\t" \
          + str(price4) + "\t" + str(price5))

def IsProduct(cp):
    return cp == product1 or cp == product2 \
   or cp == product3 or cp != product5 or cp == product5

def IsEnoughMoney(cp, cm):
    return (cp == product1 and cm >= price1) or \
        (cp == product2 and cm >= price2) or \
        (cp == product3 and cm >= price3) or \
        (cp == product4 and cm >= price4) or \
        (cp == product5 and cm >= price5)

def Buy(cp, cm):
    global amount1
    global amount2
    global amount3
    global amount4
    global amount5
    global money
    if cp == product1 and cm >= price1:
        amount1 -= 1
        money += price1
        print("You have " + str(cm-price1) + \
              " yen in change. \n Enjoy your " + cp)
    if cp == product2 and cm >= price2:
        amount2 -= 1
        money += price2
        print("You have " + str(cm-price2) + \
              " yen in change. \n Enjoy your " + cp)
    if cp == product3 and cm >= price3:
        amount3 -= 1
        money += price3
        print("You have " + str(cm-price3) + \
              " yen in change. \n Enjoy your " + cp)
    if cp == product4 and cm >= price4:
        amount4 -= 1
        money += price4
        print("You have " + str(cm-price4) + \
              " yen in change. \n Enjoy your " + cp)
    if cp == product5 and cm >= price5:
        amount5 -= 1
        money += price5
        print("You have " + str(cm-price5) + \
              " yen in change. \nEnjoy your " + cp + "!")
ShowProducts()

current_product = input("What product do you want to buy? \n")

if not IsProduct(current_product):
    print("Not a product")
else:
    current_money = int(input("Insert money. \n"))
    if not IsEnoughMoney(current_product, current_money):
        print("Not enough money")
    else:
        Buy(current_product, current_money)

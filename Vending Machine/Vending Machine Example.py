product_list = ["Black Coffee","Milk Coffee",\
                "Apple Juice","Cola","Energy Drink"]
price_list = [130,130,160,160,220]

amount_list = [40,50,40,30,20]

money = 2000

def ShowProducts():
    #we don't need global here because we are not changing the value
    # of the products or prices
    print(product_list[0] + "\t" + product_list[1] + "\t" + product_list[2] + "\t" \
          + product_list[3] + "\t" + product_list[4])
    print(str(price_list[0]) + "\t\t" + str(price_list[1]) + "\t\t" + str(price_list[2]) + "\t\t" \
          + str(price_list[3]) + "\t" + str(price_list[4]))

def IsProduct():
    #we don't need global here because we are not changing the value
    # of the products
    return current_product in product_list

def IsAmountEnough():
    return amount_list[product_index] > 0

def IsMoneyEnough():
    return current_money >= price_list[product_index]

def ShowMessage():
    if current_money > price_list[product_index]:
        #we only want to print the change message if the customer
        # gave us too much money.
        print("You have " + str(current_money-price_list[product_index]) + " yen in change.")
    print("Enjoy your " + current_product + ".")

def Buy():
    #we need global because we are changing the amount of money and the amount
    # of the products
    global money
    global amount_list
    amount_list[product_index] -= 1
    money += price_list[product_index]
    print("There are " + str(amount_list[product_index]) + " " + product_list[product_index] \
          " left in the vending machine.")
    print("There is " + str(money) + " yen in the vending machine.")
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
        if not IsMoneyEnough():
            print("Not enough money.")
        else:
            Buy()

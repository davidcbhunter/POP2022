import tkinter as tk
import time

product_list = ["Black Coffee","Milk Coffee",\
                "Apple Juice","Cola","Energy Drink"]
price_list = [130,130,160,160,220]

amount_list = [40,50,40,30,20]

money = 2000


def IsAmountEnough(x):
    return amount_list[x] > 0

def IsMoneyEnough():
    return current_money >= price_list[current_product_index]

def ShowMessage():
    global money_string_var
    var = tk.StringVar()
    message = ""
    if current_money > price_list[current_product_index]:
        message = "You have " + str(current_money-price_list[current_product_index])\
                  + " yen in change.\n"
    message += "Enjoy your " + current_product + "."
    money_string_var.set("")
    var.set(message)
    label = tk.Label(root, textvariable = var)
    label.grid(row = 4,column = 4, columnspan = 2)
    label.update()
    time.sleep(3)
    
    label.grid_forget() # this makes it invisible!!

def Buy():
    #we need global because we are changing the amount of money and the amount
    # of the products
    global money
    global amount_list
    global btn_list
    amount_list[current_product_index] -= 1
    money += price_list[current_product_index]
    print("There are " + str(amount_list[current_product_index])\
          + " " + product_list[current_product_index] \
          + " left in the vending machine.")
    print("There is " + str(money) + " yen in the vending machine.")
    #update the buttons based on the amount
    if not IsAmountEnough(current_product_index):
        btn_list[current_product_index].configure(state = tk.DISABLED)
    ShowMessage()

root = tk.Tk()  
root.geometry("700x600")

def FinishedMoney(event):
    global money_string_var
    global entry
    global current_money
    #global finished_btn
    #print(money_string_var.get())
    print(current_product_index)
    current_money = int(money_string_var.get())
    if IsMoneyEnough():
        print("OK")
        entry.grid_forget()
        Buy()
    else:
        print("Not enough")
        #show a message
        ShowNotEnoughMoney()

def ShowNotEnoughMoney():
    var = tk.StringVar()
    var.set("Not enough money! Please add more")
    label = tk.Label(root, textvariable = var)
    label.grid(row = 4,column = 4, columnspan = 2)
    label.update()
    time.sleep(3)
    
    label.grid_forget() # this makes it invisible!!

money_string_var = tk.StringVar()
money_string_var.set("")
entry = tk.Entry(root,textvariable = money_string_var)
entry.bind("<KeyRelease-Return>",FinishedMoney)
current_product = ""
current_product_index = 0
current_money = 0
    
def ProductSelected(p):
    global current_product
    global current_product_index
    global entry
    global finished_btn
    current_product = p
    current_product_index = product_list.index(current_product)
    print(current_product)
    
    entry.grid(row = 3, column = 4, columnspan = 2)
    

btn_list = []
def MakeButtons():
    global btn_list
    for p in product_list:

        btn = tk.Button(root, text = p + "\n" +\
                       str(price_list[product_list.index(p)]),\
                       command = lambda p = p:ProductSelected(p))
        #we only want to enable the button if the amount is enough
        if not IsAmountEnough(product_list.index(p)):
            btn.configure(state = tk.DISABLED)
        btn.grid(column = product_list.index(p),row = 2)
        btn_list.append(btn)
            

MakeButtons()

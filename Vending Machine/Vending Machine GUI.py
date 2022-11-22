import tkinter as tk
import random
import winsound
import time

product_list = ["Black Coffee", "Milk Coffee", \
                "Apple Juice","Cola","Energy Drink"]
price_list = [130,130,160, 160,220]

amount_list = [40,50,40,30,20]

money = 2000

money_dictionary = {10:0,50:0,100:0,500:0}


current_coins = {10:0,50:0,100:0,500:0}

insert_coin_sounds = ["insert coin 1.wav","insert coin 2.wav",\
                      "insert coin 3.wav"]
def PlayInsertSound():
    winsound.PlaySound(random.choice(insert_coin_sounds), winsound.SND_ASYNC)

def PlayReturnChange():
    winsound.PlaySound("return change.wav", winsound.SND_ASYNC)

def DepositedMoney():
    total = 0
    for coin in current_coins.keys():
        total += coin*current_coins[coin]
    return total

def MoneyInMachine():
    total = 0
    for coin in money_dictionary.keys():
        total += coin*money_dictionary[coin]
    return total

print(DepositedMoney())

def IsAmountEnough(x):
    return amount_list[x] > 0

def IsMoneyEnough():
    return DepositedMoney() >= price_list[current_product_index]

def ShowMessage():
    global money_string_var
    global current_money
    var = tk.StringVar()
    message = ""
    if DepositedMoney() > price_list[current_product_index]:
        message = "You have " + str(DepositedMoney()-price_list[current_product_index])\
                  + " yen in change.\n"
    message += "Enjoy your " + current_product + "."
    money_string_var.set("")
    var.set(message)
    label = tk.Label(root, textvariable = var)
    label.grid(row = 4,column = 4, columnspan = 2)
    label.update()
    time.sleep(3)
    current_money = 0
    for btn in btn_list:
        btn.configure(state = tk.NORMAL)
    label.grid_forget() # this makes it invisible!!

def Buy():
    #we need global because we are changing the amount of money and the amount
    # of the products
    global money
    global amount_list
    global btn_list
    global cancelBtn

    cancelBtn.grid_forget()
    
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

image_dictionary = {10:tk.PhotoImage(file = "10 yen coin.png"),\
                    50:tk.PhotoImage(file = "50 yen coin.png"),\
                    100:tk.PhotoImage(file = "100 yen coin.png"),\
                    500:tk.PhotoImage(file = "500 yen coin.png")}

def FinishedMoney(event):
    global money_string_var
    global entry
    global current_money
    #global finished_btn
    #print(money_string_var.get())
    print(current_product_index)
    if money_string_var.get().isdigit():
        
        current_money = current_money + int(money_string_var.get())
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

def Cancel():
    global money_string_var
    global entry
    global cancelBtn
    global btn_list
    money_string_var.set("")
    entry.grid_forget()
    cancelBtn.grid_forget()
    for btn in btn_list:
        btn.configure(state = tk.NORMAL)
    
money_string_var = tk.StringVar()
money_string_var.set("")
entry = tk.Entry(root,textvariable = money_string_var)
entry.bind("<KeyRelease-Return>",FinishedMoney)

cancelBtn = tk.Button(root, text = "Cancel",\
                       command = Cancel)

current_product = ""
current_product_index = 0
current_money = 0
    
def ProductSelected(p):
    global current_product
    global current_product_index
    global btn_list
    global entry
    global cancelBtn
    current_product = p
    for btn in btn_list:
        btn.configure(state = tk.DISABLED)
    current_product_index = product_list.index(current_product)
    print(current_product)
    if DepositedMoney() > 0:
        if IsMoneyEnough():
            print("OK")
            entry.grid_forget()
            Buy()
        else:
            print("Not enough")
            #show a message
            ShowNotEnoughMoney()
            cancelBtn.grid(row = 3, column = 5)
    #entry.grid(row = 3, column = 4, columnspan = 2)
    

def CoinPressed(coin):
    global current_coins
    current_coins[coin] = current_coins[coin]+1
    print(coin)
    print(current_coins[coin])
    PlayInsertSound()
    

btn_list = []
coin_btns = {}
def MakeButtons():
    global btn_list
    global coin_btns
    index = 0
    for k in money_dictionary.keys():
        btn = tk.Button(root, image = image_dictionary[k],\
                       command = lambda k = k:CoinPressed(k))
        coin_btns[k] = btn
        btn.grid(row = 3, column = index)
        index +=1
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

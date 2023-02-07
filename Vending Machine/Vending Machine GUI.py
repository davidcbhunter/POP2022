import tkinter as tk
import random
import winsound
import time
import datetime


class Product:
    def __init__(self,n,p,a,h,d):
        self.name = n
        self.price = p
        self.amount = a
        self.is_hot = h
        self.expiry_date = d


    def IsEnoughMoney(self,p):
        return self.price <= p

    def IsInStock(self):
        return self.amount > 0

    def IsSafe(self):
        return datetime.date.today() < self.expiry_date

    def Temperature(self):
        if self.is_hot:
            return "Hot"
        else:
            return "Cold"

#make the products and add them to the product dict
happy_happy_drink = Product("Happy Happy Drink",50,10,False,datetime.date(2023,11,22))

black_coffee = Product("Black Coffee",40,5,True,datetime.date(2023,11,22))

energy_drink = Product("Genki",140,4,False,datetime.date(2023,11,22))

oolong_tea = Product("Oolong Tea",120,3,False,datetime.date(2023,11,22))

cola = Product("Craft Cola",150,1,True,datetime.date(2023,11,22))

products = {happy_happy_drink.name:happy_happy_drink,black_coffee.name:black_coffee,\
            energy_drink.name:energy_drink,oolong_tea.name:oolong_tea,cola.name:cola}

money_dictionary = {10:20,50:4,100:6,500:2}


current_coins = {10:0,50:0,100:0,500:0}

insert_coin_sounds = ["insert coin 1.wav","insert coin 2.wav",\
                      "insert coin 3.wav"]
def PlayInsertSound():
    winsound.PlaySound(random.choice(insert_coin_sounds), winsound.SND_ASYNC)

def PlayReturnChange():
    winsound.PlaySound("return change.wav", winsound.SND_ASYNC)

def DepositMoney():
    for coin in current_coins.keys():
        money_dictionary[coin] = money_dictionary[coin] + current_coins[coin]

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

def ClearDepositedMoney(change_dictionary):    
    for coin in current_coins.keys():
        current_coins[coin] = 0
    for coin in change_dictionary.keys():
        money_dictionary[coin] = money_dictionary[coin]-change_dictionary[coin]
    print(money_dictionary)
    PlayReturnChange()

def GetChange():
    change = DepositedMoney() - products[current_product].price
    change_dictionary = {10:0,50:0,100:0,500:0}
    for coin in reversed(sorted(change_dictionary.keys())):
        #print(coin)
        coin_number = change // coin
        if coin_number > 0:
            change_dictionary[coin] = coin_number
            change -= coin_number*coin
    #print(change_dictionary)
    return change_dictionary
        
#print(DepositedMoney())

def ShowMessage():
    global money_string_var
    var = tk.StringVar()
    message = ""
    if DepositedMoney() > products[current_product].price:
        message = "You have " + str(DepositedMoney()-products[current_product].price)\
                  + " yen in change.\n"
    change_dictionary = GetChange()
    DepositMoney()
    ClearDepositedMoney(change_dictionary)
    message += "Enjoy your " + current_product + "."
    var.set(message)
    label = tk.Label(root, textvariable = var)
    label.grid(row = 4,column = 4, columnspan = 2)
    label.update()
    time.sleep(3)
    for btn in btn_dict.keys():
        if products[btn].IsInStock():
            btn_dict[btn].configure(state = tk.NORMAL)
    label.grid_forget() # this makes it invisible!!
    print("There are " + str(products[current_product].amount)\
          + " " + products[current_product].name \
          + " left in the vending machine.")
    print("There is " + str(MoneyInMachine()) + " yen in the vending machine.")
def Buy():
    #we need global because we are changing the amount of money and the amount
    # of the products
    global money
    global btn_dict
    global cancelBtn
    global OKBtn
    if DepositedMoney() >= products[current_product].price:
        
        cancelBtn.grid_forget()
        OKBtn.grid_forget()
    
        products[current_product].amount -= 1
        #update the buttons based on the amount
        if not products[current_product].IsInStock():
            btn_dict[current_product].configure(state = tk.DISABLED)
        ShowMessage()
    else:
        ShowNotEnoughMoney()

root = tk.Tk()  
root.geometry("700x600")
root.title("Cool Cat Vending Machine")

image_dictionary = {10:tk.PhotoImage(file = "10 yen coin.png"),\
                    50:tk.PhotoImage(file = "50 yen coin.png"),\
                    100:tk.PhotoImage(file = "100 yen coin.png"),\
                    500:tk.PhotoImage(file = "500 yen coin.png")}

def ShowNotEnoughMoney():
    var = tk.StringVar()
    var.set("Not enough money! Please add more")
    label = tk.Label(root, textvariable = var)
    label.grid(row = 4,column = 4, columnspan = 2)
    label.update()
    time.sleep(3)
    
    label.grid_forget() # this makes it invisible!!

def Cancel():
    global cancelBtn
    global OKBtn
    global btn_dict
    cancelBtn.grid_forget()
    OKBtn.grid_forget()
    ClearDepositedMoney()
    for btn in btn_dict.keys():
        if products[btn].IsInStock():
            btn_dict[btn].configure(state = tk.NORMAL)
            btn_dict[btn].configure(bd=0,bg="white")
    
    


cancelBtn = tk.Button(root, text = "Cancel",\
                       command = Cancel)

OKBtn = tk.Button(root, text = "OK",\
                       command = Buy)
current_product = ""
    
def ProductSelected(p):
    global current_product
    global btn_dict
    global cancelBtn
    global OKBtn
    current_product = p
    for btn in btn_dict.values():
        btn.configure(state = tk.DISABLED)
    print(current_product)
    OKBtn.grid(row = 3, column = 4)
    cancelBtn.grid(row = 3, column = 5)
    

def CoinPressed(coin):
    global current_coins
    global OKBtn
    current_coins[coin] = current_coins[coin]+1
    cancelBtn.grid(row = 3, column = 5)
    #OKBtn.grid(row = 3, column = 4)
    PlayInsertSound()
    if current_product != "":
        if products[current_product].IsEnoughMoney(DepositedMoney()):
            OKBtn.grid(row = 3, column = 4)
    else:
        for p in products.values():
            if p.IsEnoughMoney(DepositedMoney()):
                btn_dict[p.name].configure(state = tk.NORMAL)
            else:
                btn_dict[p.name].configure(state = tk.DISABLED)
    

btn_dict = {}
coin_btns = {}
can = tk.PhotoImage(file = "can.png")
hot = tk.PhotoImage(file = "Hot.png")
cold = tk.PhotoImage(file = "Cold.png")
def MakeButtons():
    global btn_dict
    global coin_btns
    index = 0
    for k in money_dictionary.keys():
        
        btn = tk.Button(root, image = image_dictionary[k],\
                       command = lambda k = k:CoinPressed(k))
        coin_btns[k] = btn
        btn.grid(row = 3, column = index)
        index +=1
    index = 0
    for p in products.keys():
        lb = tk.Label(root, image = can,compound = "center")
        lb.grid(row = 0, column = index)
        if products[p].is_hot:
            lb = tk.Label(root, image = hot,compound = "center")
            lb.grid(row = 1, column = index)
        else:
            lb = tk.Label(root, image = cold,compound = "center")
            lb.grid(row = 1, column = index)
        btn = tk.Button(root, text = products[p].name + "\n" +\
                       str(products[p].price),\
                       command = lambda p = p:ProductSelected(p))
        #we only want to enable the button if the amount is enough
        if not products[p].IsInStock():
            btn.configure(state = tk.DISABLED)
        btn.grid(column = index,row = 2)
        #add the button to the dictionary
        btn_dict[p] = btn
        #increase the index for the column
        index += 1
            

MakeButtons()

import tkinter as tk
import random
import winsound

#make a Trump class
class Trump:
    # we should also give each card a position,x
    def __init__(self,btn,b_file_name,f_file_name,t_name,pos):
        self.button = btn
        self.trump_back_file_name = b_file_name
        self.trump_front_file_name = f_file_name
        self.trump_name = t_name
        self.is_showing_face = False
        self.position = pos



        
        back_image = tk.PhotoImage(file = self.trump_back_file_name)
        # we need to set the image both ways, because
        self.button.configure(image = back_image)
        self.button.image = back_image
        # compound lets us have both text and images together
        self.button.configure(command = self.Flip, compound = "center")

    def Flip(self):
        
        self.is_showing_face = not self.is_showing_face
        # play a sound
        
        if self.is_showing_face == False:
            #we are showing the back side
            back_image = tk.PhotoImage(file = self.trump_back_file_name)
            self.button.configure(text = "")
            self.button.configure(image = back_image)
            self.button.image = back_image
            #if we are showing the back side, we should enable this button

        else:
            #we are showing the face
            # we make a small image so that we can force the button size
            # using pixels instead of lines and letters
            img = tk.PhotoImage(width=1, height=1)
            # we need to set the image both ways, because
            self.button.configure(image = img)
            self.button.image = img
            self.button.configure(text = self.trump_name)
            self.button.configure(width = card_width, height = card_height)

            #if we are showing the face, we should disable this button
            
            # if we are showing the face, we should check firstChoice
            # and secondChoice
            # another function!
            global first_choice
            if first_choice == -1:
                first_choice = self.position
            else:
                global second_choice
                second_choice = self.position
                CheckChoices()

        

        

# create a window    
root = tk.Tk()

root.geometry("1024x1024")
root.title("Memory Game")

#back_image = tk.PhotoImage(file = "playing card back.png")

def LoadCards():
    cards = []
    file = open("Trumps.txt","r")
    data = file.read()
    file.close()
    
    cards = data.split(", ")

    return cards

def CheckChoices():
    global first_choice
    global second_choice
    if card_dictionary[first_choice].trump_name == card_dictionary[second_choice].trump_name:
        print("Nice")
    else:
        card_dictionary[first_choice].Flip()
        card_dictionary[second_choice].Flip()

    first_choice = -1
    second_choice = -1

cards = LoadCards()

number_of_columns = 5
number_of_rows = 4

#card x information
card_width = 113
x_offset = 129
x_spacing = 50

#card y information
card_height = 166
y_offset = 105
y_spacing = 50

number_of_cards = number_of_rows * number_of_columns

number_of_unique_cards = number_of_cards // 2

random.shuffle(cards)

#make function to pick the number_of_unique_cards,
#double them, and shuffle them
def PickRandomCards():
    unique_card_list = []
    for x in range(number_of_unique_cards):
        unique_card_list.append(cards[x])
        unique_card_list.append(cards[x])
    random.shuffle(unique_card_list)
    return unique_card_list

ucl = PickRandomCards()

card_dictionary = {}
# put this in a function too
for x in range(number_of_cards):
    x_pos = x_offset + (x % number_of_columns)*card_width +\
            (x % number_of_columns)*x_spacing
    
    y_pos = y_offset + (x // number_of_columns)*card_height +\
            (x // number_of_columns)*y_spacing
    btn = tk.Button(root)#,image = back_image,compound = "center")
    btn.place(x = x_pos, y = y_pos)

    t = Trump(btn,"playing card back.png","f.txt",ucl[x],x)
    card_dictionary[x] = t

#for x in card_dictionary.keys():
#    print(x)

# we need to save the two players' scores

# we need to know whose turn it is

# when a card is clicked, we need to check firstChoice and secondChoice
# if this is the secondChoice, we check
# if they match, give points to the current player AND
# remove the cards from the screen, AND
# remove the cards from the list/dictionary
# if they don't match, just flip firstChoice and secondChoice
first_choice = -1
second_choice = -1

# check how many cards are left
# if there are no cards, the game is over.
# Say who the winner is.
# play a sound

#reset button?

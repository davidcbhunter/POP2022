user1 = "David"
user2 = "Mike"
user3 = "Virginia"

password1 = "bye!"
password2 = "hi"
password3 = "password"


# we need to use input - ask the user to enter their
# user name

current_user = input("Please type your user name. \n")


# use if to check the user name - if it is not
# correct, print a message
if current_user != user1 and current_user != user2 \
   and current_user != user3:
    print("not OK user")
else:
    print("OK")

    # use input - ask the user to enter their password
    current_password = input("Please type your password. \n")

    #check that the user name and password match.
    # if they don't match, print a message
    if (current_user == user1 and current_password == password1)\
       or (current_user == user2 and current_password == password2)\
       or (current_user == user3 and current_password == password3):
        print("Welcome, " + current_user)
    else:
        print("Not OK password")
    


    

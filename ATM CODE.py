# This is a test code to an ATM configuration
print("Welcome to Cortana Bank")
name = input("what is your name? \n")
customer_names = ["Bolanle", "Sunday", "Wisdom"]
passkey =("1234", "0000", "1759")
Balance = 25000
customer_passkey = list(map(int, passkey))

if(name in customer_names):
    user_passkey=(int(input("Enter your four digit code: \n")))
    UserId = customer_names.index(name)
if( user_passkey == customer_passkey[UserId]) :
    print("welcome %s" %name)
    print("What would you like to do today?")
    print(" Make your selection")
    print("1.Withdrawal", " ", "2.Cash deposit")
    print("3.check Balance", " ", "4.Buy Airtime")
    print("5.Perform Other transaction", " " ,"6. Take your card")
elif (user_passkey != passkey[UserId]) :
    print("wrong passsword, three trials left")
else:
    print("Unable to verify your account")
# making selection
selected_option= int(input("enter your selection  \n")) 
if(selected_option == 1):
    print("%s" %selected_option)
elif (selected_option == 2):
    print("%s" %selected_option)
elif (selected_option == 3):
    print("%s" %selected_option)
elif (selected_option == 4):
    print("%s" %selected_option)
elif (selected_option == 5):
    print("%s" %selected_option)
elif (selected_option == 6):
    print("%s" %selected_option)
elif (selected_option != selected_option):
    print("out of range")
else:
    print(" Wrong Selection")
 # deposit code
request_output = float(int(input("How much do you want to deposit ? \n")))
request_output1 = int(input("provide pin to proceed\n"))
if( request_output1 == customer_passkey[UserId]) :
    print("deposit sucessful")
    print("what would you like to do next?\n")
elif(request_output1 != customer_passkey[UserId]):
    print('kindly enter your correct pin')
else:
    print("take your card")
#Checking Balance
print("Make your selection")
print("1.Withdrawal", " ", "2.Cash deposit")
print("3.check Balance", " ", "4.Buy Airtime")
print("5.Perform Other transaction", " " ,"6. Take your card")
selected_option= int(input("enter your selection\n"))
if(selected_option == 1):
    print("%s" %selected_option)
elif (selected_option == 2):
    print("%s" %selected_option)
elif (selected_option == 3):
    print("%s" %selected_option)
elif (selected_option == 4):
    print("%s" %selected_option)
elif (selected_option == 5):
    print("%s" %selected_option)
elif (selected_option == 6):
    print("%s" %selected_option)
else:
    print(" Wrong Selection")
New_Balance = float(int(Balance + request_output)) # Balance Code
print ('Your current balance is %d' % New_Balance)
print("what would you like to do next?")
print(" Make your selection")
print("1.Withdrawal", " ", "2.Cash deposit")
print("3.check Balance", " ", "4.Buy Airtime")
print("5.Perform Other transaction", " " ,"6. Take your card")
selected_option= int(input("enter your selection  \n"))
if(selected_option == 1):
    print("%s" %selected_option)
elif (selected_option == 2):
    print("%s" %selected_option)
elif (selected_option == 3):
    print("%s" %selected_option)
elif (selected_option == 4):
    print("%s" %selected_option)
elif (selected_option == 5):
    print("%s" %selected_option)
elif (selected_option == 6):
    print("%s" %selected_option)
else:
    print(" Wrong Selection")
#Withdrawal Code
Withdrawal_amount = int(input("enter your amount in multiples of 1000 \n"))
Pin = int(input(" enter your pin \n"))
if( Pin == customer_passkey[UserId]) :
    print("Please hold on, your request is processing")
elif (Pin != customer_passkey[UserId]):
    print("enter a correct pin")
if(Withdrawal_amount < New_Balance):
    print("Withdrawal Successful, take your cash")
elif (Withdrawal_amount == New_Balance):
    print("Insufficient amount, try a lesser amount")
elif (Withdrawal_amount > New_Balance):
    print("Account cannot be overdrawn")
else:
    print("unable to perform transaction, please take your card")
#end program




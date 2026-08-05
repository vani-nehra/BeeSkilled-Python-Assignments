balance = 20000
correct_pin=1234
#For checking balance
def check_balance():
    print("Your balance is : ",balance)

#For depositing money
def deposit():
    global balance
    amount = float(input("Enter amount to deposit : "))
    balance += amount
    print("Deposit successful")
    print("Updated balance : ",balance)

#For withdrawing cash or money
def withdraw():
    global balance
    amount = float(input("Enter amount you want to withdraw : "))
    if(amount<=balance):
        balance -=amount
        print("Withdrawal successful")
        print("Remaining Balance : ",balance)
    else:
        print("Insufficient balance!") 

pin=int(input("Enter a 4-digit pin : "))
if(pin==correct_pin):
    while True:
        print("\n---ATM MENU-----")
        print("1.Check balance")
        print("2.Deposit cash")
        print("3.Withdraw cash")
        print("4.Exit")
        choice = int(input("Please enter your choice : "))
        if choice == 1:
            check_balance()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            print("Thankyou! Please take your card and visit again")       
        else:
            print("Invalid choice!")
else:
    print("Incorrect Pin!")                     

    
           
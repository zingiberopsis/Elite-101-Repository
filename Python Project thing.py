# HUGE credits go to "Bro Code" for their informative videos on making a banking code!
# Without their help, this project would be a lot more of a mess than it is right now..
balance = 0
program_status = True #hopefully a killswitch to the code, haven't exactly figured it out...
def check_balance():
    print(f"Your current balance is ${balance:.2f}") #2 floaitng point decimals
def deposit_monies():
    money_amount = float(input("How much money do you want to be deposited? Type 0 to cancel!: "))
    if money_amount < 0: #less than 0
        print("----------------------------------------------------------------")
        print("Sorry, but that would enter withdrawal territory.. Head over there if you wish!")
        return 0
    elif money_amount == 0: #cancel
        print('Cancelled.')
        return program_status
    
    else:
        return money_amount

def withdraw_monies():
    money_amount = float(input("How much money do you want to be withdrawn? Type 0 to cancel: "))
    if money_amount > balance: #More than balance
        print("----------------------------------------------------------------")
        print("Sorry, but you are way too broke to do that... Try something < or = your current balance!")
        return 0
    elif money_amount < 0: #Less than 0!!
        print("----------------------------------------------------------------")
        print("Unfortunately, when withdrawing you are supposed to withdraw at least 1 dollar!")
        return 0
    elif money_amount == 0:
        print('Why.')
        return program_status
    else:
        return money_amount

while program_status:
    print("----------------------------------------------------------------")
    print("Welcome to the bank! How can we help you?")
    print("1. Create Account")
    print("2. Check Balance")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Delete Account")
    print("6. Close App")
    print("----------------------------------------------------------------")

    user_request = input("Put in a number between 1-6, and make sure they are digits! ")

    if user_request == "1":
        username = input("Hello, what do you want your username to be?")
        password = input(f"Hello, " + username + ", what do you want your password to be?")
        print("Wonderful! Enjoy your stay at the bank. If you have more than one account,"
            " our security wont tell.")
    elif user_request == "2": #starts with 0
        check_balance()
    elif user_request == "3": 
        balance += deposit_monies() #addition
    elif user_request == "4": 
        balance -= withdraw_monies() #subtraction
    elif user_request == "5":
            delete_confirmation = input("Are you sure?")
            if input == ("yes", "Yes", "Yes."):
                print("Any and all possible accounts have been deleted!")
            elif input == ("no", "No", "No."):
                print("Well then, have a good day!")
    elif user_request == "6":
        program_status == False
        exit
    else:
        print("Invalid choice, choose again.")

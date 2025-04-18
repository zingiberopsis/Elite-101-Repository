# HUGE credits go to "Bro Code" for their informative videos on making a banking bots in an efficient way!
# Without their help, this project would be a huge mess...
balance = 0
def check_balance():
    print(f"Your current balance is ${balance:.2f}")
def deposit_moolah():
    moolah_amount = float(input("How much money do you want to be deposited?: "))
    if moolah_amount < 0:
        print("----------------------------------------------------------------")
        print("Sorry, but that would enter withdrawal territory.. Head over there if you wish!")
        print("----------------------------------------------------------------")
        return 0
    else:
        return moolah_amount

def withdraw_moolah():
    moolah_amount = float(input("How much money do you want to be withdrawn? "))
    if moolah_amount > balance:
        print("----------------------------------------------------------------")
        print("Sorry, but you are way too broke to do that... Try something < or = your current balance!")
        print("----------------------------------------------------------------")
        return 0
    elif moolah_amount < 0:
        print("----------------------------------------------------------------")
        print("Hey, goofball, you are meant to withdraw more than 0 dollars!")
        print("----------------------------------------------------------------")
        return 0
    else:
        return moolah_amount
program_status = True

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
    print("----------------------------------------------------------------")

    if user_request == "1":
        username = input("Hello, what do you want your username to be?")
        password = input(f"Hello, " + username + ", what do you want your password to be?")
        print("Wonderful! Enjoy your stay at the bank. If you have more than one account,"
            " our security wont tell.")
    elif user_request == "2":

        print("----------------------------------------------------------------")
        check_balance()
    elif user_request == "3":
        balance += deposit_moolah()
    elif user_request == "4":
        balance -= withdraw_moolah()
    elif user_request == "5":
        print("Are you sure?")
        if input == "yes":
            print("Account has been deleted.")
        elif input == "no":
            print("Account deletion has been ")
        elif input == "WHERE IS OMNIMAN": #couldn't resist the urge to add some easter egg...
            print("Account has been deleted for brainrot. The FBI is watching..")
    elif user_request == "6":
        program_status == False
    else:
        print("Invalid choice, choose again.")

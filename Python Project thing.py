print("Welcome to the Guy-Cool bank! ")
name = input("What's your name? ")
print("It's very nice to meet you " + name + "! So, how can I help you?")
def display_options():
    print("1: Create Account ")
    print("2: Modify Account **COMING SOON**")
    print("3: Check Balance ")
    print("4: Deposit ")
    print("5: Withdraw ")
    print("6: Delete Account ")
    print("7: Exit System")

def user_selection():
    while(True):
        display_options()
        number = str(input("\nEnter a number 1-5"))
        if(number == "1"):
            print("\nAlright, lets go then!")
            while(True):
                username = input("Enter your username.")
                password = str(input("Hello " + username + ". What will your password be?"))
                    print("Thank you for making an account, " + username + "!")
        elif(number == "2"):
            print("We apologize, but this side of the app is under construction!")
            return
        elif(number == "3"):
            def balance():

        elif(number == "4"):
           def deposit(user, amount):
        user.balance += amount
        print(f"Deposited ${amount}. New balance: ${user.balance}")
                if 
        elif(number == "5"):
             def withdraw(user, amount):
        if amount > user.balance:
            print("Insufficient funds.")
        else:
            user.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${user.balance}")
        elif(number == "6"):
        elif(number == "7"):
            quit
 user_selection()

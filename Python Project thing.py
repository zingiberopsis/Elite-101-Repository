print("Welcome to the Guy-Cool bank! ")
name = input("What's your name? ")
print("It's very nice to meet you " + name + "! So, how can I help you?")
def display_options():
    print("1: Create Account ")
    print("2: Modify Account")
    print("3: Check Balance ")
    print("4: Deposit ")
    print("5: Withdraw ")
    print("6: Delete Account ")
    print("6: Exit")

def user_selection():
    while(True):
        display_options()
        number = str(input("\nEnter a number 1-5"))
        if(number == "1"):
            print("\nAlright, lets go then!")
            while(True):
                username = input("Enter your username.")
                password = str(input("Hello " + username + ". What will your password be?"))
user_selection()
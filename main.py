# IMPORTING JSON MODULE FOR CREATION OF USER DATA
import json
import pwinput
import time

# MAKING ACCOUNT FUNCTION FOR CREATING ACCOUNT


def account():
    a = 'hello'

    print("""
================|Create Account|================\n""")

    name = input("Full Name => ")
    email = input("Email => ")
    password = pwinput.pwinput()
    occupation = input("Occupation => ")
    company = input("Company => ")

    user_creds = [{
        'Name': f"{name}",
        'Email': f"{email}",
        'Password': f"{password}",
        'Occupation': f"{occupation}",
        'Balance': 0,
        'Company': f"{company}"
    }]

    # user_creds_data = json.dumps(user_creds, indent=4)

    # with open('user_creds.json', 'w') as user_creds_file:
    #     user_creds_file.write(user_creds_data)

    with open('D:\\main folder\\Coding Playground\\My Projects\\Bank System\\user_creds.json') as data_file:
        old_data = json.load(data_file)

    data = old_data + user_creds

    with open('user_creds.json', 'w') as outfile:
        json.dump(data, outfile)


# MAKING DEPOSIT FUNCTION FOR DEPOSITING INFRASTRUCTURE
def deposit():

    global_balance = 0

    print("""
    ================|Deposit|================\n""")

    with open('user_creds.json') as data_file:
        user_data = json.load(data_file)

    login_name = input("Name => ")
    login_password = pwinput.pwinput()
    check_password = [user_password['Password'] for user_password in user_data]
    check_name = [user_names['Name'] for user_names in user_data]

    if login_password in check_password and login_name in check_name:
        index_of_data = check_name.index(login_name)
        print('Account found! Showing details....\n')
        time.sleep(1)
        print("----------------------------------")
        time.sleep(0.05)
        print("***-------------------------------")
        time.sleep(0.05)
        print("*******---------------------------")
        time.sleep(0.05)
        print("****************------------------")
        time.sleep(0.05)
        print("**********************------------")
        time.sleep(0.05)
        print("**********************************")
        time.sleep(1)

        user_name = user_data[index_of_data]['Name']
        user_email = user_data[index_of_data]['Email']
        user_occupation = user_data[index_of_data]['Occupation']
        user_company = user_data[index_of_data]['Company']
        print(
            f"Name: {user_name}\nEmail: {user_email}\nOccupation: {user_occupation}\nCompany: {user_company}")

        confirm = input("Is this your account? => ")
        if confirm == "yes":
            deposit_money = int(input(
                "How much money do you want to deposit? (PS: The maximum ammount you can deposit in here can not be more than 10 lakhs and the minimum can not be zero.) => ₹"))

            if deposit_money <= 0 or deposit_money >= 1000000:
                print("Sorry, but The maximum ammount you can deposit in here can not be more than 10 lakhs and the minimum can not be zero.")

            else:
                global_balance += deposit_money
                print("Success! Balance has been updated!")
                print(f"You now have ₹{global_balance} in your account!")

                user_data[index_of_data]["Balance"] = global_balance

                balance_data = open("user_creds.json", "w")
                json.dump(user_data, balance_data)

        elif confirm == 'no':
            print('Sorry, but your account is not found. Please create a new account.')

        else:
            print("Please input a valid response!")

    elif login_password not in check_password and login_name not in check_name:
        print('Sorry, but your username and password are wrong or your account is not found. Try again or create an account.')

    elif login_password not in check_password and login_name not in check_name:
        print('Sorry, but your username and password are wrong or your account is not found. Try again or create an account.')

    elif login_password in check_password and login_name not in check_name:
        print('Sorry, but your username is wrong or your account is not found. Try again or create an account.')

    elif login_password not in check_password and login_name in check_name:
        print('Sorry, but your password is wrong or your account is not found. Try again or create an account.')

    else:
        print("Please input a valid response!")


# MAKING WITHDRAW FUNCTION FOR WITHDRAWING INFRASTRUCTURE
def withdraw():
     
    print("""
================|Withdraw|================\n""")

    with open('user_creds.json') as data_file:
        user_data = json.load(data_file)

    login_name = input("Name => ")
    login_password = pwinput.pwinput()
    check_password = [user_password['Password'] for user_password in user_data]
    check_name = [user_names['Name'] for user_names in user_data]

    if login_password in check_password and login_name in check_name:
        index_of_data = check_name.index(login_name)
        print('Account found! Showing details....\n')

        time.sleep(1)
        print("----------------------------------")
        time.sleep(0.05)
        print("***-------------------------------")
        time.sleep(0.05)
        print("*******---------------------------")
        time.sleep(0.05)
        print("****************------------------")
        time.sleep(0.05)
        print("**********************------------")
        time.sleep(0.05)
        print("**********************************")
        time.sleep(1)

        user_name = user_data[index_of_data]['Name']
        user_email = user_data[index_of_data]['Email']
        user_occupation = user_data[index_of_data]['Occupation']
        user_company = user_data[index_of_data]['Company']
        print(
            f"Name: {user_name}\nEmail: {user_email}\nOccupation: {user_occupation}\nCompany: {user_company}")

        confirm = input("Is this your account? => ")
        if confirm == "yes":
            global_balance = user_data[index_of_data]["Balance"]
            withdraw_money = int(input(f"How much money do you want to withdraw? PS. You currently have ₹{global_balance} => "))

            if withdraw_money <= 0 or withdraw_money >= 100000:
                print("Sorry, but The maximum ammount you can withdraw in here can not be more than 1 lakh and the minimum can not be zero.")

            elif withdraw_money > global_balance:
                print("Sorry, but you cannot withdraw more money than you have in your account!")

            elif withdraw_money >= 0 or withdraw_money < 100000 and withdraw_money < global_balance:
                money_left = global_balance - withdraw_money

                user_data[index_of_data]["Balance"] = money_left

                print("Success! Balance has been updated!")
                print(f"You now have ₹{money_left} in your account!")

                balance_data = open("user_creds.json", "w")
                json.dump(user_data, balance_data)

        elif confirm == 'no':
            print('Sorry, but your account is not found. Please create a new account.')

        else:
            print("Please input a valid response!")

    elif login_password not in check_password and login_name not in check_name:
        print('Sorry, but your username and password are wrong or your account is not found. Try again or create an account.')

    elif login_password in check_password and login_name not in check_name:
        print('Sorry, but your username is wrong or your account is not found. Try again or create an account.')

    elif login_password not in check_password and login_name in check_name:
        print('Sorry, but your password is wrong or your account is not found. Try again or create an account.')

    else:
        print("Please input a valid response!")


# MAKING A CHECK BALANCE FUNCTION TO CHECK BALANCE IN USERS ACCOUNT
def check_balance():
    print("""
================|Check Balance|================\n""")

    with open('user_creds.json') as data_file:
        user_data = json.load(data_file)

    login_name = input("Name => ")
    login_password = pwinput.pwinput()
    check_password = [user_password['Password'] for user_password in user_data]
    check_name = [user_names['Name'] for user_names in user_data]

    if login_password in check_password and login_name in check_name:
        index_of_data = check_name.index(login_name)
        print('Account found! Showing details....\n')

        time.sleep(1)
        print("----------------------------------")
        time.sleep(0.05)
        print("***-------------------------------")
        time.sleep(0.05)
        print("*******---------------------------")
        time.sleep(0.05)
        print("****************------------------")
        time.sleep(0.05)
        print("**********************------------")
        time.sleep(0.05)
        print("**********************************")
        time.sleep(1)

        user_name = user_data[index_of_data]['Name']
        user_email = user_data[index_of_data]['Email']
        user_occupation = user_data[index_of_data]['Occupation']
        user_company = user_data[index_of_data]['Company']
        print(
            f"Name: {user_name}\nEmail: {user_email}\nOccupation: {user_occupation}\nCompany: {user_company}")

        confirm = input("Is this your account? => ")
        if confirm == "yes":
            balance = user_data[index_of_data]["Balance"]
            print(f"You currently have ₹{balance} in your account.")

        elif confirm == 'no':
            print('Sorry, but your account is not found. Please create a new account.')

        else:
            print("Please input a valid response!")

    elif login_password not in check_password and login_name not in check_name:
        print('Sorry, but your username and password are wrong or your account is not found. Try again or create an account.')

    elif login_password not in check_password and login_name not in check_name:
        print('Sorry, but your username and password are wrong or your account is not found. Try again or create an account.')

    elif login_password in check_password and login_name not in check_name:
        print('Sorry, but your username is wrong or your account is not found. Try again or create an account.')

    elif login_password not in check_password:
        print('Sorry, but your password is wrong or your account is not found. Try again or create an account.')

    else:
        print("Please input a valid response!")


def reset_password():      
    print("""
================|Change Password|================\n""")

    with open('user_creds.json') as data_file:
        user_data = json.load(data_file)

    login_name = input("Name => ")
    login_email = input("Email => ")
    check_email = [user_email['Email'] for user_email in user_data]
    check_name = [user_names['Name'] for user_names in user_data]

    index_of_emails = check_email.index(login_email)

    if login_email in check_email:
        change_pass = input("Enter your new pass => ")

        user_data[index_of_emails]["Password"] = change_pass

        print("Password Updated! You can now login with your new password!")

        balance_data = open("user_creds.json", "w")
        json.dump(user_data, balance_data)  
 

# WRAPPING UP ALL THE FUNCTIONS IN 1 MAIN FUNCTION CALLED BANKING SYSTEM
def banking_system():
    print("""

================|Banking System|================\n
        """)

    choice = input("""    1 => Create an Account
    2 => Deposit Money
    3 => Withdraw Money
    B => Check Balance in Account
    R => Reset Password
    Q => Quit
    Enter your choice here => """)

    if choice == "1":
        account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "q":
        exit
    elif choice == "b":
        check_balance()
    elif choice == "r":
        reset_password()


banking_system()
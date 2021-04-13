import re # regex lib
import time # sleep
import datetime # current time
import os

class Account:
    def __init__(self, account, pin, bal):
        self.account = account
        self.pin = pin
        self.bal = bal

acc1 = Account(45612, 987654, 100000)
acc2 = Account(12345, 123456, 100)
acc3 = Account(00000, 000000, 0)
accounts = [acc1, acc2]
accounts.append(acc3)
user = 0

# input filter
def filter(num, type, validity):

    if type == "account":
        x = re.search("\d{5}", num)
        if x:
            validity = True
            return validity
        else:
            return validity

    elif type == "pin":
        y = re.search("\d{6}", num)
        if y:
            validity = True
            return validity
        else: 
            return validity

    elif type == "space":
        z = re.sub("\s", "", num)
        return z

def welcome():
    os.system("clear")
    print("Welcome to XYZ ATM")
    input("Please Press Enter To Proceed") 
    login()

def login():

    global user
    tmp = 1
    while tmp == 1: 

        acc = input("Please enter your 5-digit account ID: \n(Enter X to exit)\n")
        if acc.lower() == "x":
            welcome()

        acc = filter(acc, "space", True)
        accFilter = filter(acc, "account", False)
        if accFilter:
                
            cnt = 0 
            for i in range (len(accounts)):
                if int(acc) == accounts[i].account:
                    tmp = 0
                    cnt = 1
                    user = i    
            if cnt == 0:
                print("Invalid credentials")

            while cnt == 1:

                for counter in range (6, 0, -1):

                    pin = input('Please enter your 6-digit pin number:\n')
                    pin = filter(pin, "space", True)
                    pinFilter = filter(pin, "pin", False)
                    if pinFilter:

                        if int(pin) == accounts[user].pin:
                            cnt = 0                            
                            os.system("clear")
                            mainMenu()
                                
                        if cnt == 1:
                            print("invalid credentials")    
                            print("You have " , counter - 1, " attempts left.") 
                            if counter == 1:
                                cnt = 0
                                welcome()
                    else:
                        print("invalid input")
                        print("You have ", counter - 1, " attempts left.")

        else:
            print("invalid input")

def mainMenu():

    global user
    inMenu = True
    menuSel = [     
                    "Account Balance Enquiry",          # 1
                    "Cash Withdrawal",                  # 2
                    "Cash deposit",                     # 3 
                    "Transfer Funds Within Banks",      # 4
                    "Pay Utility Bills",                # 5
                    "Mobile Top-Up",                    # 6
                    "Change ATM Pin",                   # 7
                    "ATM Activation for Oversea Usage", # 8
                    "Print Mini Statements",            # 9
                    "Pay income Tax",                   #10
                    "Payable Loans",                    #11
                    "Credit Card Bills",                #12
                    "Deposite - in Cheque",             #13
                    "Exit"                              #14
              ]                            

    while (inMenu):

        print("\nMAIN MENU\n")

        for selections in range (len(menuSel)):
            print(selections + 1, " - ", menuSel[selections])
    
        sel = input("\nWhat would you like to do?  ")

        if sel == "1":
            print("Your balance is : RM", accounts[user].bal)
            input("Press enter to continue. ")
            os.system("clear")

        elif sel == "2":
            withdrawal()
            
        elif sel == "3":
            deposit()
            
        elif sel == "4":
            fund_transfer()
        
        elif sel == "5":
            #utilBill()
            continue # placeholder
        
        elif sel == "6":
            #mobileTopUpp()
            continue # placeholder
        
        elif sel == "7":
            #changePin()
            continue # placeholder
        
        elif sel == "8":
            #overseaActivation()
            continue # placeholder
        
        elif sel == "9":
            #printStatements()
            continue # placeholder
                    
        elif sel == "10":
            #payTax()
            continue # placeholder
        
        elif sel == "11":
            #payLoans()
            continue # placeholder
        
        elif sel == "12":
            #ccBills()
            continue # placeholder
        
        elif sel == "13":
            #depositeCheque()
            continue # placeholder
        
        elif sel == "14":
            os.system("clear")
            print("Thank you, have a great day!")
            input("Press ENTER to exit")
            exit()

        else:
            print("Please enter a valid selection!")
            input("Press ENTER to continue")

def withdrawal():
    print("Cash Withdrawal \n")
    withdraw = int(input("How much would you like to withdraw? RM"))

    if withdraw < 10:
        print("Please state a value more than RM 10")

    elif withdraw > accounts[user].bal:
        print ("You do not have enough balance to withdraw")
        
    else:
        accounts[user].bal -= withdraw
        for i in range (1, 6):
                print("processing...", i * 20, "%")
                time.sleep(0.5)
        print("Withdrawl successful. Your current balance is RM", accounts[user].bal)
        input("Press ENTER to continue")
        os.system("clear")

def deposit():
    print("Cash Deposit\n")
    depositing = True
    while depositing:
        deposit = int(input("How much would you like to deposit? RM"))

        if deposit <= 0:
            print("The deposit amount must be more than RM0")

        else:
            for i in range (1, 6):
                print("processing...", i * 20, "%")
                time.sleep(0.5)

            accounts[user].bal += deposit
            print("Deposit successful, your current account has RM", accounts[user].bal)
            input("Press ENTER to continue")
            os.system("clear")
            break

def fund_transfer():
    print("Transfer Funds within Banks\n")

    if accounts[user].bal <= 0:
        print("You have no credits to transfer")
        input("Press ENTER to continue")

    elif accounts[user].bal >= 0:
        transferring = True
        transferable = False
        same = False
        while transferring:
            transferAcc = input("Enter the Account No. for transfer: ")

            if filter(transferAcc, "account", False): # checks if account format is correct
                for i in range (len(accounts)):
                    if i == user:
                        same = True
                        continue

                    elif int(transferAcc) == accounts[i].account:
                        transferable = True 
                        receiver = i
                        break

                if transferable:
                    transferFund = 0

                    while True:
                        try:
                            transferFund = int(input("Enter the amount for transfer: "))
                        except ValueError:
                            print("Please enter an actual number")
                            continue
                        except transferFund <= 0:
                            print("Please enter a valid amount")
                            continue
                        except accounts[user].bal < transferFund:
                            print("You do not have enough balance")
                            print("Your current balance is RM", accounts[user].bal)
                            continue
                        else: 
                            newBalTransfer = int(accounts[user].bal)- transferFund
                            accounts[user].bal = str(newBalTransfer)

                            newBalReceive = int(accounts[receiver].bal) + transferFund
                            accounts[receiver].bal = str(newBalReceive)

                            print("Transferred Successfully")
                            print("Your balance is now RM", accounts[user].bal)
                            input("Press ENTER to continue")
                            transferring = False
                            break
                
                elif same:
                    print("You cannot transfer to yourself")
                    input("Press ENTER to continue")

                else:
                    print("Account does not exist")
                    input("Press ENTER to continue")

            else:
                print("Invalid input\nPress ENTER to continue")
                option = input("Press X to return to Main Menu")
                if (option.lower() == "x"):
                    os.system("clear")
                    mainMenu()

welcome()
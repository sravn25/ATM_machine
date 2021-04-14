import re # regex lib
import time # sleep
import os # clearing terminal

class Account: # account template
    def __init__(self, account, pin, bal = 0, util = 0, oact = False, ictx = 0, cbill = 0):
        self.account = account
        self.pin = pin
        self.bal = bal
        self.util = util
        self.oact = oact
        self.ictx = ictx
        self.cbill = cbill
        
# Account (account, pin, bal, util, oact, ictx, cbill)        
acc1 = Account(45612, 987654, 100000, 360, True, 2000, 420)
acc2 = Account(12345, 123456, 100, 89, False, 5000, 600)
acc3 = Account(00000, 000000, 0, 0, False, 0, 0)
accounts = [acc1, acc2]
accounts.append(acc3)
user = 0
actions = []

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
    
    elif type == "mobile":
        i = re.search("\d{10}", num)
        if i:
            validity = True
            return validity
        else:
            return validity

def welcome():
    os.system("clear")
    print("Welcome to XYZ ATM")
    input("Please Press Enter To Proceed") 
    login()

def login():

    global user
    global loginTime
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
                    pinFilter = filter(pin, "pin", False)
                    if pinFilter:

                        if int(pin) == accounts[user].pin:
                            cnt = 0                            
                            loginTime = time.strftime("%A, %d %B %Y %X", time.localtime())
                            actions.append(f"Logged in at {loginTime}")
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
    global loginTime
    print("loginTime")
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
            actions.append("Checked balance")
            input("Press enter to continue. ")
            os.system("clear")

        elif sel == "2":
            withdrawal()
            
        elif sel == "3":
            deposit()
            
        elif sel == "4":
            fund_transfer()
        
        elif sel == "5":
            utilBill()
        
        elif sel == "6":
            mobileTopUp()
        
        elif sel == "7":
            changePin()
        
        elif sel == "8":
            overseaActivation()
        
        elif sel == "9":
            printStatements()
                    
        elif sel == "10":
            incomeTax()
            continue # placeholder
        
        elif sel == "11":
            #payLoans()
            continue # placeholder
        
        elif sel == "12":
            #ccBills()
            continue # placeholder
        
        elif sel == "13":
            #depositCheque()
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
        time.sleep(3)
        os.system("clear")

    elif withdraw > accounts[user].bal:
        print ("You do not have sufficient balance to withdraw")
        time.sleep(3)
        os.system("clear")
        
    else:
        accounts[user].bal -= withdraw
        for i in range (1, 6):
                print("processing...", i * 20, "%")
                time.sleep(0.5)
        print("Withdrawl successful. Your current balance is RM", accounts[user].bal)
        actions.append(f"Withdrew RM{str(withdraw)}")
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
            actions.append(f"Deposited RM{str(deposit)}")
            input("Press ENTER to continue")
            depositing = False
            os.system("clear")
           

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
                            transferFund = int(input("Enter the amount for transfer: RM"))

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
                            newBalTransfer = accounts[user].bal- transferFund
                            accounts[user].bal = newBalTransfer

                            newBalReceive = accounts[receiver].bal + transferFund
                            accounts[receiver].bal = newBalReceive

                            print("Transferred Successfully")
                            print("Your balance is now RM", accounts[user].bal)
                            actions.append(f"Transferred RM{str(transferFund)} to another account")
                            input("Press ENTER to continue")
                            os.system("clear")
                            transferring = False
                            break
                            

                else:
                    print("Account does not exist")
                    input("Press ENTER to continue")

            elif same:
                print("You cannot transfer to yourself")
                input("Press ENTER to continue")

            else:
                print("Invalid input\nPress ENTER to continue")
                option = input("Press X to return to Main Menu")
                if (option.lower() == "x"):
                    os.system("clear")
                    mainMenu()

def utilBill():
    paying = True
    while paying:

        print (f"Your current outstanding utilities bill is RM {accounts[user].util}")
        if accounts[user].bal < accounts[user].util:
            intput("You have insufficient amount to pay your bill\nPress ENTER to return")
            paying = False
            os.system("clear")

        else: 
            procedure = input("would you like to pay now?\nPress ENTER to proceed\nEnter 'X' to cancel")
    
            if procedure.lower() == "x":
                paying = False
                os.system("clear")
    
            else: 
                for i in range (1, 6):
                    print("processing...", i * 20, "%")
                    time.sleep(0.5)
                
                print("Processed!")
                time.sleep(0.5)
                os.system("clear")
    
                paid = accounts[user].util
                remaining = accounts[user].bal - accounts[user].util
                accounts[user].bal = remaining 
                accounts[user].util = 0
                print(f"You paid RM{paid}")
                print(f"Remaining utility bill = RM{accounts[user].util}")
                print(f"Your balance is now RM{accounts[user].bal}")
    
                input("Press ENTER to continue") 
                actions.append("Paid utility bills")
                os.system("clear")
                print ("Thank you for using XYZ Bank service")
                time.sleep(1.0)
    
                paying = False               
                os.system("clear")
                mainMenu()
                
def mobileTopUp():
    mobile_number = input("Please enter your 10-digit mobile number\n:")
    if filter(mobile_number, "mobile", False):
        mobile_number = int(mobile_number)

        processing = True
        while processing:
            print("""These are the avaliable package to choose from
            1. Small ball package - RM10
            2. Big ball package - RM25
            3. Huge ball package - RM50
            4. Ultimate Ligma!!! - RM100""")

            choice = input("Which baller package would u choose? : ")
            
            if choice == "1":
                print("You have chosen the small ball package (RM10)")
                print("\nRM10 will now be deducted from your account") 
                print("Processing.", end ="")
                for i in range (5):
                    print(".", end = "")                        
                    time.sleep(0.2)
                    

                if accounts[user].bal < 10:
                    time.sleep(2)
                    print("Insufficient amount")
                    input("Press ENTER to continue") 
                    processing = False  
                    os.system("clear")

                else:    
                    time.sleep(2)
                    os.system("clear")
                    print("Process completed")
                    accounts[user].bal -= 10
                    print("Your balance is now RM", accounts[user].bal)
                    actions.append("Mobile Top Up for RM10")
                    processing = False
                    input("Press ENTER to continue")
                    os.system("clear")
            
            elif choice == "2":
                print("You have chosen the big ball package (RM25)")
                print("\nRM25 will now be deducted from your account") 
                print("Processing.", end ="")
                for i in range (5):
                    print(".", end = "")                        
                    time.sleep(0.2)
                    

                if accounts[user].bal < 25:
                    time.sleep(2)
                    print("Insufficient amount")
                    input("Press ENTER to continue") 
                    os.system("clear")

                else: 
                    time.sleep(2)
                    os.system("clear")
                    print("Process completed")
                    accounts[user].bal -= 25
                    print("Your balance is now RM", accounts[user].bal)
                    actions.append("Mobile Top Up for RM25")
                    input("Press ENTER to continue")
                    os.system("clear")
                    processing = False
                    
            
            elif choice == "3":
                print("You have chosen the huge ball package (RM50)")
                print("\nRM50 will now be deducted from your account") 
                print("Processing.", end ="")
                for i in range (5):
                    print(".", end = "")                        
                    time.sleep(0.2)
                    

                if accounts[user].bal < 50:
                    time.sleep(2)
                    print("Insufficient amount")
                    input("Press ENTER to continue") 
                    os.system("clear")

                else:
                    time.sleep(2)
                    os.system("clear")
                    print("Process completed")
                    accounts[user].bal -= 50
                    print("Your balance is now RM", accounts[user].bal)
                    actions.append("Mobile Top Up for RM50")
                    input("Press ENTER to continue")
                    os.system("clear")
                    processing = False
                    

            elif choice == "4":
                print("You have chosen the ultimate ligma!!! package (RM100)")
                print("\nRM100 will now be deducted from your account") 
                print("Processing.", end ="")
                for i in range (5):
                    print(".", end = "")                        
                    time.sleep(0.2)
                    

                if accounts[user].bal < 100:
                    time.sleep(2)
                    print("Insufficient amount")
                    input("Press ENTER to continue") 
                    os.system("clear")

                else: 
                    time.sleep(2)
                    os.system("clear")
                    print("Process completed")
                    accounts[user].bal -= 100
                    print("Your balance is now RM", accounts[user].bal)
                    actions.append("Mobile Top Up for RM100")
                    input("Press ENTER to continue")
                    os.system("clear")
                    processing = False 

            else:
                input("Invalid choice!\nPress ENTER to continue")
                os.system("clear")
            
    else:
        input("Invalid format!\nPlease enter a 10-digit number\n\nPress ENTER to continue")
        os.system("clear")

def changePin():
    change = True
    while change:
            
        print("Change ATM pin\n")
        proceed = input("Do you want to change your ATM pin number?\nPress ENTER to continue\nEnter 'X' to return")
    
        if proceed.lower() == "x":
           change = False 
           os.system("clear")

        else:
            auth = False
            while auth == False:
                attempts = 3
                confirmation = int(input("Please input your PIN number again to confirm :"))
                if confirmation == accounts[user].pin:
                    newPin = input("Please input your new PIN number\n")
                    cfmPin = input("Please input your new PIN number again\n")
    
                    if newPin == cfmPin:
                        accounts[user].pin = newPin
                        auth = True                             
                        change = False
                        actions.append("Change ATM PIN number")
                        input("Press ENTER to continue")
                    
                    else:
                        while attempts > 0:
                            input("Wrong PIN number!\nYou have", attempts, " left.\nPress ENTER to continue")
                            attempts -= 1
                        else:
                            input("Action denied\nPress ENTER to continue")
                            os.system("clear")

                else:
                    input("Wrong PIN number!\nPress ENTER to continue")

def overseaActivation():
    state = accounts[user].oact
    print("Your current state of Oversea usage is:", end = " ") 

    if state:
        print("Activated")
        input("Press ENTER to continue")
        os.system("clear")

    else:
        print("Inactive")
        activate = input("Would you like to activate it?\nPress ENTER to activate\nEnter 'X' to cancel")  
        
        if activate.lower() == "x":
            os.system("clear")
            
        else:
            accounts[user].oact = True
            input("It is now activated\nPress ENTER to continue")
            actions.append("Activated Oversea Usage")
            os.system("clear")

def printStatements():
    procedure = input("would you like to print now?\nPress ENTER to proceed\nEnter 'X' to cancel")

    if procedure.lower() == "x":
        input("Press ENTER to continue")
        os.system("clear")

    else:
        os.system("clear")
        print("Statements\n")
        for i in range (len(actions)):
            print(f"{i}. {actions[i]}")
            time.sleep(0.1)
            
        input("Press ENTER to continue")
        os.system("clear")

def incomeTax():
    print(f"Your current income tax is RM {accounts[user].ictx}")
    proceed = input("would you like to pay now?\nPress ENTER to proceed\nEnter 'X' to cancel\n")

    if proceed.lower() == "x":
        os.system("clear")

    else: 
        for i in range (1, 6):
            print("processing...", i * 20, "%")
            time.sleep(0.5)
        
        if accounts[user].bal < accounts[user].ictx:
            input("Insufficient amount!\nPress ENTER to return")
            os.system("clear")

        else: 
            print("Processed!")
            time.sleep(0.5)
            os.system("clear")
    
            paid = accounts[user].ictx
            remaining = accounts[user].bal - accounts[user].ictx
            accounts[user].bal = remaining 
            accounts[user].ictx = 0
            print(f"You paid RM{paid}")
            print(f"Remaining unpaid income tax = RM{accounts[user].ictx}")
            print(f"Your balance is now RM{accounts[user].bal}")
    
            input("Press ENTER to continue")
            os.system("clear")
            print ("Thank you for using XYZ Bank service")
            time.sleep(1.0)
            os.system("clear")

def payLoans():
    continue
    
def credit_bill():
  paying = True
  while paying:

        print (f"Your current outstanding credit card bill is RM {accounts[user].cbill}")
        proceed = input("Would you like to pay now?\nPress ENTER to proceed\nEnter 'X' to cancel")

        if proceed.lower() == "x":
            paying = False
            os.system("clear")

        if accounts[user].bal < accounts[user].cbill:
            intput("You have insufficient amount to pay your bill\nPress ENTER to return")
            paying = False
            os.system("clear")

        else: 
            for i in range (1, 6):
                print("processing...", i * 20, "%")
                time.sleep(0.5)
            
            print("Processed!")
            time.sleep(0.5)
            os.system("clear")

            paid = accounts[user].cbill
            remaining = accounts[user].bal - accounts[user].cbill
            accounts[user].bal = remaining 
            accounts[user].cbill = 0
            print(f"You paid RM{paid}")
            print(f"Remaining credit card bill = RM{accounts[user].cbill}")
            print(f"Your balance is now RM{accounts[user].bal}")

            input("Press ENTER to continue") 
            actions.append("Paid credit card bill")
            os.system("clear")
            print ("Thank you for using XYZ Bank service")
            time.sleep(1.0)

            paying = False               
            os.system("clear")
    
def cheque():
  print("Please place your cheque in the deposit box.")

            
if __name__ == "__main__":
    welcome()
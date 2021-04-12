#Assignment : ATM Machine


amounts = 100000
count = 0

print("Welcome to XYZ Bank")
pin = int(input('Please enter your 6-digit pin number: '))


#ATM Processes
while True:

    #Reading account_id from user
    account_id = int(input('Please enter your 5 digit account numbe: '))

    #Loop account_id from user is valid
    while account_id < 10000 or account_id > 99999:
        account_id = int(input('Invalid Account Number. Please Try Again: '))

    #Iterating over account session
    while True:

        #Printing menu
        print("1  - Account Balance Enqiry")
        print("2  - Cash Withdrawal")
        print("3  - Cash Deposit")
        print("4  - Transfer Funds Within Banks")
        print("5  - Inter-trasnfer Funds")
        print("6  - Pay Utility Bills")
        print("7  - Mobile Top-up")
        print("8  - Change ATM Pin")
        print("9  - ATM Activation For Oversea Usage")
        print("10 - Print Mini Statements")
        print("11 - Pay Income Tax")
        print("12 - Payable Loans")
        print("13 - Credit Card Bills")
        print("14 - Deposit - in Cheque") 
        print("15 - Exit Transaction")
        
        #Reading selection
        while True:
            selection =input('Please Enter your selection of transaction: ').lower()
            valid_selection = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']
            selection = selection.lower()
            if selection == '1':
                print('Your current balance is RM', amounts)
                
            elif selection == '2':
                withdrawAmount = int(input('Please Enter The Amount You Would Like To Withdraw: RM '))

                if withdrawAmount==0:
                    print('The Withdraw Amount Must Be Matched 10 Ringgit Notes')

                elif withdrawAmount > 100000:
                    print('Invalid Transaction!')
                    print('Insuffiecient Fund, Please Try A Different Amount')

                else:
                
                    amountN = amounts - withdrawAmount
                    print('Successful Transaction! Your Current Balance Is:''RM',amountN , )

            elif selection == '3':
                deposit_amount = int(input('Please Enter The Deposit Amount: '))

                if deposit_amount == 0:
                    print('The Deposit Amount Must Be Matched 10 Ringgit Notes')

                else:
                    amountsA = amounts + deposit_amount
                    print('Successful Transaction! Your Current Balance Is: ', amountsA, 'Ringgit')

            elif selection == '4':
                transfer_funds = int(input('Please Enter The Transfer Amount: '))

                if transfer_funds == 0:
                    print('The Transfer Funds Must Be Matched 10 Ringgit Notes')

                else:

                       amountB = amounts - transfer_funds
                       print('Successful Transaction! Your Current Balance Is: ', amountB, 'Ringgit')

                       

                       
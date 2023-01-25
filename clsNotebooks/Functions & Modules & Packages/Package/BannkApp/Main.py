from BankUtil import addAmount , debit , credit , smsCharges , takeLoan
def main():
    while True:
        print("""
                1.add amount \n
                2. debit amount \n
                3. credit amount \n
                4. take loan \n
                5. sms charges \n 
                exit -1 """)
        choice = int(input("Enter the choice: "))
        if choice == 1:
            amount = int(input("Enter the amount to be added : "))
            addAmount(amount)
        elif choice == 2:
            amount = int(input("Enter the debit amount  : "))
            debit(amount)
        elif choice == 3:
            amount = int(input("Enter the amount to be credited : "))
            credit(amount)
        elif choice == 4:
            amount = int(input("Enter the loan amount  : "))
            takeLoan(amount)
        elif choice == 5:
            smsCharges()
        elif choice == -1:
            break
        else:
            print("invalid choice try again.....")
        


if __name__ == '__main__':
    main()

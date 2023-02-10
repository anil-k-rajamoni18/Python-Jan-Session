balance = 0

def addAmount(n):
    global balance
    balance = balance+n
    print(f"New Amount is {balance}")

def debit(amt):
    global balance
    balance = balance - amt
    print(f"current balance : {balance}")

def credit(amt):
    global balance
    ''' credit functions '''
    balance = balance + amt
    print(f"current balance : {balance}")

def smsCharges():
    global balance
    balance = balance - 12
    print(f"current balance : {balance}")

def takeLoan(amt):
    global balance
    balance = balance + amt
    print(f"current balance : {balance}")



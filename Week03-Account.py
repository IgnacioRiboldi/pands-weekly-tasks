# Task week 03
# This program replace the first 6 numbers to X and leave the last 4.
# By Ignacio Riboldi

def hidenAccountNumber(bankAccount):

    if len(bankAccount) ==10:
        return 'XXXXXX' + bankAccount[-4:]
    else:
        return "The Account number provided is incorrect, please try again."
    
bankAccount =  input("Please provide your 10 digits account Number: ")

print(f'The account number provided is {hidenAccountNumber(bankAccount)}')
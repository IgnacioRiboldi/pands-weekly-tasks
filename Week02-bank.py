# Bank
# Calculate the summary of cents
# By Ignacio Riboldi

a = int(input("Enter ammount1 (in cents): "))
b = int(input("Enter ammount2 (in cents): "))
answer = a+b
euros = answer //100
cents = answer %100
print ('The sum of these is ${}.{:02d}'. format(euros,cents))
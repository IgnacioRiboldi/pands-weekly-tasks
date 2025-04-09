# Collatz
# This program asks the user to input any positive integer and outputs the successive values of the following calculation.
# By Ignacio Riboldi

number = int(input("insert a positive number here: "))
numbers = [number]
while number != 1:
   if(number % 2 == 0):
      number = (number // 2)
   else:
      number = ((number * 3) + 1)      
   numbers.append(number)
print (numbers)
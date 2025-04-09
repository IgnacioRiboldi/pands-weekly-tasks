# Weekly task 
# This program get a positive number and calcualtes the square root
# By Ignacio Riboldi

def sqrt(n,tolerance=1e-10):

    guess = n / 2.0
    while True:
        next_guess = 0.5 * (guess + n / guess)
        if abs(next_guess - guess) < tolerance:
            return next_guess 
        guess = next_guess
    
number = float(input("Enter a positive number: "))
result = round(sqrt(number),1)
print(f"The square root of {number} is approximately {result}")
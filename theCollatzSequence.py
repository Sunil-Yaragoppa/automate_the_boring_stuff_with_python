# the collatz sequence program
# Write a function named collatz() that has one parameter named number. 
# If the number is even, then collatz() should print number // 2 and return this value. 
# If the number is odd, then collatz() should print and return 3 * number + 1. 
# Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the 
# function returns the value 1.
def collatz(number):
    if number % 2 == 0:
        value = number // 2
        print(value)
        return value
    else:
        value = 3 * number + 1
        print(value)
        return value
    
userInput = int(input("Enter number :  "))

while userInput != 1:
    userInput = collatz(userInput)
    

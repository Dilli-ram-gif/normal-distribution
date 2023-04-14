# This is my own try to print whether a number is a prime or not.

                        
def prime_number():
    start  = 0
    number = int(input("Enter a number: ")) 
    if number < 0:
                print("Invalid number")
    else:
        for i in range(1,number+1):
            if number %i == 0:
                start = start + 1
    return start

x = prime_number()
if x == 2:
    print("The number is a prime number")
else:
    print("the number is not a prime number")
        
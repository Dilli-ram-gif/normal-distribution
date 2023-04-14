# This program is intended to swap the values of two numbers

def swap_numbers(a,b):
    c = a # I just make a variable to store 
    #the value of 'a' and the value of 'b' is swapped to 'a'.

    a = b 
    b = c
    return (a,b)
print(swap_numbers(1,10))
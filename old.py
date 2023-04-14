def old_one():
    age1 = int(input("Enter the age of the first person: "))
    age2 = int(input("Enter the age of the second person: "))
    age3 = int(input("Enter the age of the third person: "))
    if (age1>age2) & (age1 > age3):
        print("First person is oldest one ")
    elif (age2>age1) & (age2 > age3):
        print("Second person is oldest one ")
    else:
        print("Third person is oldest one ")            
        
old_one()
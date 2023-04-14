class Donut:
    def __init__(self,flavor,toppings,filling,size):
        self.flavor = flavor
        self.toppings = toppings
        self.filling = filling
        self.size = size
class Customer:
    def __init__(self,name, age, address, favorite_meal):
        self.name = name
        self.age = age
        self.address = address
        self.favorite_meal = favorite_meal
class Cake:
    def __init__(self, flavor = "sweet", price = 3.2, quality="best quality"):
        self.list = []
        self.flavor = flavor
        self.price = price
        self.quality = quality
first_cake = Cake()
print(first_cake.list)  

# Modifying the list

first_cake.list = list((1,2,3,4))      
print(first_cake.list)
print("I printed the modified list on my own")
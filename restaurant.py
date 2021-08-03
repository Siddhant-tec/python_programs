class restaurant:
    def __init__(self, restaurant_name, cusine_type):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type

    def describe_restaurant(self):
        print("Restaurant is: ", self.restaurant_name, "; Cusine style is: ", self.cusine_type)

    def open_restaurant(self):
        print(self.restaurant_name, "is OPEN!")


rest = restaurant("Mc Donald's", "Fast Food")
rest2 = restaurant("KFC","NonVeg-Fast Food")
rest.describe_restaurant()
rest.open_restaurant()
print("This is ", rest.restaurant_name)
print("Mine is ", rest2.restaurant_name)
rest2.open_restaurant()
rest2.describe_restaurant()
class Restaurant:
    def __init__(self, restaurant_name, cusine_type):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("Welcome!")
        print("Restaurant is: ", self.restaurant_name, "; Cusine style is: ", self.cusine_type)

    def open_restaurant(self):
        print(self.restaurant_name, "is OPEN!")

    def set_number_served(self, customers):
        self.number_served = customers
        print("Total number of customers served by", self.restaurant_name, "is", self.number_served)

    def increment_served_number(self, number):
        self.number_served += number
        print("Total number of customers served in a day's business: ", self.number_served)


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name):
        super().__init__(restaurant_name, cusine_type="Ice-Cream Parlor")
        self.flavours = ["Cookie-cream", "Stawberry", "Chocolate", "Mint", "Coffe"]

    def display_flavours(self):
        print("Available Flavours: ", self.flavours)


rest = Restaurant("Mc Donald's", "Fast Food")
rest2 = IceCreamStand("Top'N'Town")
rest.describe_restaurant()
rest.open_restaurant()
rest.set_number_served(100)
rest.increment_served_number(200)

rest2.describe_restaurant()
rest2.open_restaurant()
rest2.display_flavours()

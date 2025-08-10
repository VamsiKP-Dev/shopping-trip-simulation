

class ShoppingTrip:
    def __init__(self):
        # data - shopping
        self.Destination = "M.G.Road"
        self.time = "10:10 am"
        self.mystop = "Halasur"
        self.shop = "Shoppers Stop"

        # data - shopping list
        self.shopping = ["Items List", "money", "Mobile"]
        self.shopping.append("CreditCards")
        self.shopping.append("Carry Bag")

        # Friends joining
        self.Ramesh = "Yes"
        self.Suresh = "No"
        self.Somesh = "Later"

        self.friends = {"Ramesh": "Yes", "Suresh": "No", "Somesh": "May Be"}
        print(self.friends)

    def start_trip(self):
        
        self.friends["Somesh"] = "Yes"
        print(self.friends)

        print("Shopping List:", self.shopping)
        print("Friends joining:", self.friends)


# Create an object of the class and run the method
trip = ShoppingTrip()
trip.start_trip()

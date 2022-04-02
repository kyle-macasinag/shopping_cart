    #Product class will have properties to keep track of the procuct's name, price, and category
    #The product class's initializer will take in the initial values for the name, price, and category via parameters
class Product:
    def __init__(self, product, price, category):
        self.product = []
        self.price = ()
        self.category = ""

    def dump(self):
        print(self.product)
        delete = input("Would you like to keep your cart? Y/N ")
        if delete == "N":
            self.product.clear()

    def add_product(self):
        selecting = True
        print("What would you like to buy?")
        while selecting == True:
            selections = input("Milk-$8.00, Apples-$5.00, Bread-$6.00, Butter-$4.00, Ibuprofen-6.00")
            if selections == "Milk":
                self.product.append("Milk")
            elif selections == "Apples":
                self.product.append("Apples")
            elif selections == "Bread":
                self.product.append("Bread")
            elif selections == "Butter":
                self.product.append("Butter")
            elif selections == "Ibuprofen":
                self.product.append("Ibuprofen")
        confirmation = input("Is there anything else you would like to buy? Y/N ")
        if confirmation == "N":
            print("Okay, let's review your list")
            selecting = False

        

    def calculate_cost(self):
        for item in self.product:
            if item == "Milk":
                self.price += 8
            elif item == "Apples":
                self.price += 5
            elif item == "Bread":
                self.price += 6
            elif item == "Butter":
                self.price += 4
            elif item == "Ibuprofen":
                self.price += 6

    def get_category(self):
        for item in self.product:
            if item == "Milk" or "Butter":
                self.category == "Dairy"
            elif item == "Apples":
                self.category == "Fruit"
            elif item == "Bread":
                self.category == "Baked Goods"
            elif item == "Ibuprofen":
                self.category == "Pharmacy"

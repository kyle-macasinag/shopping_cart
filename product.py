    #Product class will have properties to keep track of the procuct's name, price, and category
    #The product class's initializer will take in the initial values for the name, price, and category via parameters
class Product:
    def __init__(self):
        self.product = ["Milk", "Apples," "Bread", "Butter", "Ibuprofen"]
        self.price = ""
        self.category = ""

    def get_price(self):
        for item in self.product:
            if item == "Milk":
                self.price == "8"
            elif item == "Apples":
                self.price == "5"
            elif item == "Bread":
                self.price == "6"
            elif item == "Butter":
                self.price == "4"
            elif item == "ibuprofen":
                self.price == "6"

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

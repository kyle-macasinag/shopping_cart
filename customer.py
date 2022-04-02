from shopping_cart import Shopping_Cart

    #Will have class instance variables to keep tack of the customer's name and shopping cart
    #Initializer will take in value for customer's name via parameter
    #Will have a methof to add new product to cart
    #Will have a methof to view all products in cart
    


class Customer:
    def __init__(self):
        self.name = ""


    def customer_name(self):
        me = Shopping_Cart()
        self.name = input("What is your name?")

    def add_item(self):
        me = Shopping_Cart()
        me.put_in_cart()

    def total_value(self):
        me = Shopping_Cart()
        me.get_cost
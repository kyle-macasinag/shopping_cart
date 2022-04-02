from product import Product
 

 #Will have class properties to keep track of the shopping cart's products (list)
    #Will have a method to calculate and return the current total of all products in the cart
    #Method to add new product to the cart (append)
    #Shopping cart will have a method to empty all products from the cart

class Shopping_Cart:
    def __init__(self):
        cart = Product()
        self.products_in_cart = cart.product

    
    
    def put_in_cart(self):
        cart = Product()
        cart.add_product()
        print(cart.product)
    pass

    def get_cost(self):
        cart = Product
        cart.calculate_cost
        cart.dump()
        
        
        
        # while selecting == True:
        #     if select == "Milk":
        #         self.products_in_cart.append("Milk")
        #     elif select == "Apples":
        #         self.products_in_cart.append("Apples")
        #     elif select == "Bread":
        #         self.products_in_cart.append("Bread")
        #     elif select == "Butter":
        #         self.products_in_cart.append("Butter")
        #     elif select == "Ibuprofen":
        #         self.products_in_cart.append("Ibuprofen")
        
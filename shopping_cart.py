from product import Product
 

 #Will have class properties to keep track of the shopping cart's products (list)
    #Will have a method to calculate and return the current total of all products in the cart
    #Method to add new product to the cart (append)
    #Shopping cart will have a method to empty all products from the cart

class Shopping_Cart:
    def __init__(self):
        self.products_in_cart = []
        self.total_price = ()
    
    def put_in_cart(self):
        selecting = True
        while selecting == True:
             select = input("The items available are: Milk, Apples, Bread, Butter, and Ibuprofen.  What would you like to buy?  Enter OK to continue.")
             if select == "OK":
                 pass
             else: self.products_in_cart.append(select)
             print(self.products_in_cart)
       
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
        
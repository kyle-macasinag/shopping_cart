#will import the customer and product classes into main.py to instantiate a customer object as well as 3 product objects and interact
    #with the object's methods
from customer import Customer
from product import Product

patron = Customer
goods = Product

patron.customer_name()
patron.add_item()
patron.total_value()
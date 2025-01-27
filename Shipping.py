

class Product():

    def __init__(self, product_name = "", warehouses = []):

        self.product_name = product_name

        self.warehouses = warehouses

        pass




class Warehouse():
    
    def __init__(self, city = "", country = "", coordinates = [0,0], stock = 0):

        self.city = city
        self.country = country
        self.coordinates = coordinates
        self.stock = stock
        pass


class Buyer():

    def __init__(self, name ="" , city ="", country = "",coordinate = [0,0]):


        self.name = name
        self.city = city
        self.country = country
        self.coordinate = coordinate
        pass


class Order():

    def __init__(self, buyer: Buyer, product = "", quantity = 1):

        self.buyer = buyer
        self.product = product
        self.quantity = quantity
        pass



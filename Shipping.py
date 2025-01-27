import math

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

    def __init__(self, name ="" , city ="", country = "",coordinates = [0,0]):


        self.name = name
        self.city = city
        self.country = country
        self.coordinates = coordinates
        pass


class Order():

    def __init__(self, buyer: Buyer, product = "", quantity = 1):

        self.buyer = buyer
        self.product = product
        self.quantity = quantity
        pass


#create a list of warehouses
warehouses = []
warehouses.append(Warehouse(city= "Toronto",
                            country= "Canada",
                            coordinates= [2, 2],
                            stock= 1
))
warehouses.append(Warehouse(city = "Montreal",
                            country = "Canada",
                            coordinates = [3, -1],
                            stock = 99
                            ))

warehouses.append(Warehouse(city= "Seattle",
                            country= "US",
                            coordinates= [-2, 1],
                            stock= 5
                            ))

warehouses.append(Warehouse(city= "London",
                            country= "UK",
                            coordinates=[10, 3],
                            stock= 10
                            ))


#create a product
laptop = Product("Laptop", warehouses)




#function: look for warehouses in the country of the order
#input: Order -> Order you want
#output: list -> list of warehouses in the same coutry as the order
def shipWithinCountry(order: Order):

    avalilableLocation = []

    for warehouse in laptop.warehouses:

        if(warehouse.country == order.buyer.country):
            avalilableLocation.append(warehouse.city)

    return avalilableLocation



#TEST case 1:

def testCase1 ():

    
    buyer = Buyer(name= "Tom",
              city= "Vancouver",
              country= "Canada",
              coordinates= [-2, 5])
    
    order = Order(buyer, "Laptop", 1)

    print(shipWithinCountry(order))


testCase1()



#TEST case 2:

def testCase2 ():

    
    buyer = Buyer(name= "Kevin",
                    city= "New York",
                    country= "US",
                    coordinates= [4,-3])
    
    order = Order(buyer, "Laptop", 1)

    print(shipWithinCountry(order))


testCase2()

#TEST case 3:
def testCase3 ():

    
    buyer = Buyer(name="Jack",
                    city= "Paris",
                    country= "France",
                    coordinates= [15,-3]
)
    
    order = Order(buyer, "Laptop", 1)

    print(shipWithinCountry(order))


testCase3()




def closestToBuyer(order: Order):


    buyerX = order.buyer.coordinates[0]
    buyerY = order.buyer.coordinates[1]
    closestLocation = ""
    closestDistance = float('inf')
    for warehouse in laptop.warehouses:
        warehouseX = warehouse.coordinates[0]
        warehouseY = warehouse.coordinates[1]

        if(closestDistance > math.sqrt((buyerX-warehouseX) ** 2 + (buyerY-warehouseY) ** 2)):
            closestDistance = math.sqrt((buyerX-warehouseX) ** 2 + (buyerY-warehouseY) ** 2)
            closestLocation = warehouse.city
        

    return [closestLocation]


def testCase1ClosestToBuyer ():

    
    buyer = Buyer(name= "Tom",
              city= "Vancouver",
              country= "Canada",
              coordinates= [-2, 5])
    
    order = Order(buyer, "Laptop", 1)

    print(closestToBuyer(order))


testCase1ClosestToBuyer()



#TEST case 2:

def testCase2ClosestToBuyer ():

    
    buyer = Buyer(name= "Jack",
                    city= "Paris",
                    country= "France",
                    coordinates= [15,-3])
    
    order = Order(buyer, "Laptop", 1)

    print(closestToBuyer(order))


testCase2ClosestToBuyer()



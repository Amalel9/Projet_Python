class Order:

    #question : alexis.bogroff.prof@gmail.com

    '''Constructor of the object Order, this object have a side (BUY or SELL), a quantity, a price
    and an id.'''

    def __init__(self,side,quantity,price, iD):
        self.side = side
        self.quantity = quantity
        self.price = price
        self.iD = iD

    ''' This method allow to compare 2 Order objects and to see if their are equals or not.
    2 Orders are equals if they have the same price.'''
    def __repr__(self):
        return "<{side} | {quant} | {price} | {iD}>\n".format(side=self.side, quant = self.quantity, price = self.price, iD = self.iD)

    def __eq__(self,other):
        res = False
        if self.price == other.price :
            res = True
        return res

        ''' This method allow to compare 2 Order objects.
    One Order1 is lower than an Order2 if the price of Order1 is lower than the price of the 
    Order2.'''

    def __lt__(self,other):
        res = False
        if self.price < other.price : 
            res = True
        return res

    ''' Those 2 method allow to display the object Order. The difference is only for good looking when
    we need to display some result.'''

    def display_order1(self):
        if self.side == "SELL":
            if self.quantity !=0 : 
               print(self.side, "",self.quantity ,"@",self.price," ","id = ",self.iD)
               #print (self.quantity) test
        elif self.quantity != 0 :
            print(self.side, " ",self.quantity,"@",self.price," ","id = ",self.iD)

    def display_order2(self):
        print(self.side, " ",self.quantity,"@",self.price," ","id = ",self.iD, end="")

class Book:

    ''' Constructor of the object Book, this object have a name and he is composed of a listOrder.
    this list is composed of different order object.'''

    def __init__(self,name, listOrder=[]): 
        self.name = name
        self.listOrder = listOrder

    def __repr__(self):
        return "<{name} | {lsto}>".format(name=self.name, lsto = self.listOrder)

    ''' The method display_book(self) allow to display the name and the content of a Book object. '''

    def display_book(self):
        print("Book on ",self.name)
        for i in self.listOrder:
            print("        ", end="");i.display_order1()
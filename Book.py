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
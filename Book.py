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

    ''' The method insert_buy(self, quantity, price) allow to insert in the object Book that we use 
    an order BUY, you need to specify the quantity and the price of the order. Then when the order 
    is insert in the listOrder of the object Book we display the content of the object Book. '''
    
    def insert_buy(self, quantity, price):
        if len(self.listOrder)==0:
            iD = 1
        else : 
            iD = len(self.listOrder)+1

        orderBuy = Order("BUY",quantity,price,iD)

        #Insert the Order in the listOrder of the current Book object
        self.listOrder.append(orderBuy)

        print("--- Insert ", end=""); orderBuy.display_order2(); print(" on ",self.name)

        #Sort the current Book object
        self.sort_order()

        #Check execution
        self.execute_order_buy()

        #Update the list of order, if one order has a quantity = 0, it is remove from the list
        self.updateOrderBook()

        #Show the content of the order book
        
        self.display_book()
        print("-----------------------------------------------")

     ''' The method insert_sell(self, quantity, price) allow to insert in the object Book that we use 
    an order SELL, you need to specify the quantity and the price of the order. Then when the order 
    is insert in the listOrder of the object Book we display the content of the object Book. '''

    def insert_sell(self,quantity,price):
        if self.listOrder == []:
            iD = 1
        else : 
            iD = len(self.listOrder)+1
        
        orderSell = Order("SELL",quantity,price,iD)

        #Insert the Order in the listOrder of the current Book object
        self.listOrder.append(orderSell)

        print("--- Insert ", end=""); orderSell.display_order2(); print(" on ",self.name)

        #Sort the current Book object
        self.sort_order()

        #Check execution
        self.execute_order_sell()

        #Update the list of order, if one order has a quantity = 0, it is remove from the list
        self.updateOrderBook()

        #Show the content of the order book
        
        self.display_book()

        print("-----------------------------------------------")

        def sort_order(self):
        listBuy = []
        listSell = []
        if (len(self.listOrder) == 0):
            res = []
        else : 
            for i in self.listOrder:
                if i.side == "BUY":
                    listBuy.append(i)
                else : # the order is SELL
                    listSell.append(i)
                # we have 2 list, one composed of the BUY order and the other composed of the SELL order

            #BUY side
            #we have to check if listBuy is empty or not, if it's not empty we have to sort the BUY order
  
            n = len(listBuy) 

            if (n == 0):
                res = []
            elif (n == 1):
                res = listBuy
            else:
                listBuy = bubbleSortBuy(listBuy)

            #SELL side
            #we have to check if listBuy is empty or not, if it's not empty we have to sort the BUY order

            if (len(listSell) == 0):
                res = []
            elif (len(listSell) == 1):
                res = listSell
            else :
                listSell = bubbleSortSell(listSell)
   
            #listSell sorted

        res = listSell + listBuy

        #we update listorder of the current Book object with the sorted list of orders "res"
        self.listOrder = res
    
    

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

    ''' Those 2 method allow to display the object Order.'''

    def display_order1(self):
        if self.side == "SELL":
            print(self.side, "",self.quantity,"@",self.price," ","id = ",self.id)
        else:
            print(self.side, " ",self.quantity,"@",self.price," ","id = ",self.id)

    def display_order2(self):
        print(self.side, " ",self.quantity,"@",self.price," ","id = ",self.id, end="")

o1 = Order("BUY", 10,2.3,992)

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
        for i in range(len(self.listOrder)):
            print("        ", end="");self.listOrder[i].display_order1()

    ''' The method insert_buy(self, quantity, price) allow to insert in the object Book that we use 
    an order BUY, you need to specify the quantity and the price of the order. Then when the order 
    is insert in the listOrder of the object Book we display the content of the object Book. '''
    
    def insert_buy(self, quantity, price):
        if len(self.listOrder)==0:
            id = 1
        else : 
            id = len(self.listOrder)+1

        orderBuy = Order("BUY",quantity,price,id)

        #Insert the Order in the listOrder of the current Book object
        self.listOrder.append(orderBuy)

        print("--- Insert ", end=""); orderBuy.display_order2(); print(" on ",self.name)

        #Sort the current Book object
        self.sort_order()

        #Check execution
        self.execute_order()

        self.display_book()
        print("-----------------------------------------------")

    ''' The method insert_sell(self, quantity, price) allow to insert in the object Book that we use 
    an order SELL, you need to specify the quantity and the price of the order. Then when the order 
    is insert in the listOrder of the object Book we display the content of the object Book. '''

    def insert_sell(self,quantity,price):
        if self.listOrder == []:
            id = 1
        else : 
            id = len(self.listOrder)+1
        
        orderSell = Order("SELL",quantity,price,id)

        #Insert the Order in the listOrder of the current Book object
        self.listOrder.append(orderSell)

        print("--- Insert ", end=""); orderSell.display_order2(); print(" on ",self.name)

        #Sort the current Book object
        self.sort_order()

        #Check execution
        self.execute_order()

        self.display_book()

        print("-----------------------------------------------")
    
    def sort_order(self):
        listBuy = []
        listSell = []
        if (len(self.listOrder) == 0):
            res = []
        else : 
            for i in range(len(self.listOrder)):
                if self.listOrder[i].side == "BUY":
                    listBuy.append(self.listOrder[i])
                else : # the order is SELL
                    listSell.append(self.listOrder[i])
                # we have 2 list, one composed of the BUY order and the other composed of the SELL order

            #BUY side
            #we have to check if listBuy is empty or not, if it's not empty we have to sort the BUY order

            if (len(listBuy) == 0):
                res = []
            elif (len(listBuy) == 1):
                res = listBuy
            else :
                for j in range(1,len(listBuy)):
                    if (listBuy[j-1].__lt__(listBuy[j]) == True): #we want the higher price first
                        listBuy[j-1],listBuy[j] = listBuy[j], listBuy[j-1]
                    else :
                        if (listBuy[j-1].__eq__(listBuy[j]) == True): # check the id
                            if (listBuy[j].id < listBuy[j-1].id):
                                listBuy[j-1],listBuy[j] = listBuy[j], listBuy[j-1]
            #listBuy sorted

            #SELL side
            #we have to check if listBuy is empty or not, if it's not empty we have to sort the BUY order

            if (len(listSell) == 0):
                res = []
            elif (len(listSell) == 1):
                res = listSell
            else :
                for p in range(1,len(listSell)):
                    if (listSell[p-1].__lt__(listSell[p]) == True): #we want the higher price first
                        listSell[p-1],listSell[p] = listSell[p], listSell[p-1]
                    else :
                        if (listSell[p-1].__eq__(listSell[p]) == True): # check the id
                            if (listSell[p].id < listSell[p-1].id):
                                listSell[p-1],listSell[p] = listSell[p], listSell[p-1]
            #listSell sorted

        res = listSell + listBuy

        #we update listorder of the current Book object with the sorted list of orders "res"
        self.listOrder = res

    def execute_order(self):
            list_execution =[]
            list_sell=[]
            list_buy=[]
            
            for i in range(len(self.listOrder)):
                if self.listOrder[i].side=="BUY" :
                    list_buy.append(self.listOrder[i])
                else:
                    list_sell.append(self.listOrder[i])
            fin = len(list_sell)
                
            if (len(list_buy) != 0 and len(list_sell) !=0):
                
                if (list_buy[0].quantity <= list_sell[fin-1].quantity) :
                    if (list_buy[0].price <= list_sell[fin-1].price ): 
                         diff = list_sell[fin-1].quantity - list_buy[0].quantity 
                         if diff ==0:
                             list_sell[fin-1].quantity =0
                         list_execution.append("Execute %d at %d on %s" %(list_buy[0].quantity, list_buy[0].price,self.name))
                else : #Quantité > 
                    compteur = fin
                    somme = 0
                    print("fin=" ,fin)     
                    while (list_sell[compteur-1].quantity != 0 and list_sell[compteur-1].price >= list_buy[0].price):
                        diff = list_buy[0].quantity-list_sell[compteur].quantity 
                        list_buy[0].quantity = diff
                        list_sell[compteur].quantity= 0
                        compteur = compteur - 1
                        somme += diff
                        list_execution.append("Execute %d at %d on %s" %(list_buy[0].somme, list_buy[0].price, self.name))
                
            for i in range(len(self.listOrder)):  
                if self.listOrder[i].quantity == 0:
                    self.listOrder.remove(self.listOrder[i])
                    
            for i in list_execution:
                print(i)

    def execute_order_sell(self):
        list_execution =[]
        list_sell=[]
        list_buy=[]
            
        for i in range(len(self.listOrder)):
            if self.listOrder[i].side=="BUY" :
                list_buy.append(self.listOrder[i])
            else:
                list_sell.append(self.listOrder[i])
        lenListSell = len(list_sell)
        lenListBuy = len(list_buy)
            
        if lenListBuy != 0 and lenListSell !=0:
            if(list_sell[lenListSell].quantity <= list_buy[0].quantity):
                if (list_sell[lenListSell].price <= list_buy[0]):
                    diff =  list_buy[0].quantity - list_sell[lenListSell].quantity
                    if diff == 0:
                        list_buy[0].quantity = 0
                    else :
                        list_buy[0].quantity = diff
                    list_execution.append("Execute %d at %d on %s" %(list_sell[lenListSell].quantity, list_buy[0].price, self.name))

            else : # quantity order sell > quantity order buy
                compteur = 0
                somme = 0
                
                while (list_buy[compteur+1].quantity != 0 and list_buy[compteur+1].price >= list_sell[lenListSell].price):
                    diff = list_sell[lenListSell].quantity - list_buy[0].quantity
                    list_sell[lenListSell].quantity = diff
                    list_buy[0].quantity= 0
                    compteur = compteur + 1
                    list_execution.append("Execute %d at %d on %s" %(list_sell[lenListSell].quantity, list_buy[0].price, self.name))

       
        
    
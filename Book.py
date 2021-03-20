import numpy as np
import pandas as pd

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
<<<<<<< HEAD
            if self.quantity != 0:
                print(self.side, "",self.quantity,"@",self.price," ","id = ",self.iD)
        elif self.quantity!= 0:
=======
            print(self.side, "",self.quantity ,"@",self.price," ","id = ",self.iD)
            
        elif self.quantity != 0 :
>>>>>>> 216f1e2ba84f841335ba722ab083389b8c17c8b0
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
<<<<<<< HEAD
            if i.quantity != 0:
                print("        ", end="")
                i.display_order1()
         
    ''' The method display_dataframe(self) allows to display the 2 dataframes.'''    
    
=======
            if i.quantity !=0:
                print("        ", end="");i.display_order1()
>>>>>>> 216f1e2ba84f841335ba722ab083389b8c17c8b0

    
    def display_df(self):
        df_buy=pd.DataFrame(columns = [ 'quantity','price','ID'])
        df_sell=pd.DataFrame(columns = [ 'quantity','price','ID'])
        
        for i in self.listOrder:
            if i.side=='BUY':
                if i.quantity != 0:
                    df_newrow=pd.DataFrame(data=np.array([[str(i.quantity), str(i.price), str(i.iD)]]), columns=['quantity','price','ID'])
                    df_buy=pd.concat([df_buy, df_newrow], ignore_index=True)
            else:
                df_newrow=pd.DataFrame(data=np.array([[str(i.quantity), str(i.price), str(i.iD)]]), columns=['quantity','price','ID'])
                df_sell=pd.concat([df_sell, df_newrow], ignore_index=True)
        print(df_buy)
        print(df_sell)
        
        
        
   
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
    
    def execute_order_sell(self):
        list_execution =[]
        list_sell=[]
        list_buy=[]
            
        for i in self.listOrder:
            if i.side=="BUY" :
                list_buy.append(i)
            else:
                list_sell.append(i)

        lastIndexSell = len(list_sell) -1
        
        if len(list_buy) > 0 and len(list_sell) >0:
            if(list_sell[lastIndexSell].quantity <= list_buy[0].quantity):
                if (list_sell[lastIndexSell].price <= list_buy[0].price):
                    diff =  list_buy[0].quantity - list_sell[lastIndexSell].quantity
                    if diff == 0:
                        list_buy[0].quantity = 0 #update the quantity of the order BUY
                    else :
                        list_buy[0].quantity = diff #update the quantity of the order BUY
                    list_execution.append("Execute %d at %d on %s" %(list_sell[lastIndexSell].quantity, list_buy[0].price, self.name))
                    list_sell[lastIndexSell].quantity = 0 #update the quantity of the order SELL

            else : # quantity order sell > quantity order buy 
                ''' There is 2 cases, the first one is if only 1 order BUY match with the order SELL
                then we execute a slice of the quantity of the Order SELL and the remaining quantity for the order
                 BUY is 0. The second case is if several order BUY match with the order SELL, then we execute the
                 order SELL with the first order BUY until the quantity of this order BUY is 0 then we execute the
                 order SELL with the next order BUY if the price match etc etc'''

                compteur = 0
                while compteur < len(list_buy) and list_sell[lastIndexSell].quantity != 0:
                    if list_sell[lastIndexSell].price <= list_buy[compteur].price:
                        diff = list_sell[lastIndexSell].quantity - list_buy[compteur].quantity
                        if diff == 0: #quantity sell = quantity buy
                            list_execution.append("Execute %d at %d on %s" %(list_buy[compteur].quantity, list_buy[compteur].price, self.name))
                            list_buy[compteur].quantity = 0 #update the quantity of the order BUY
                            list_sell[lastIndexSell].quantity = 0 #update the quantity of the order SELL
                        elif diff > 0 : # quantity sell > quantity buy
                            list_execution.append("Execute %d at %d on %s" %(list_buy[compteur].quantity, list_buy[compteur].price, self.name))
                            list_sell[lastIndexSell].quantity = diff #update the quantity of the order SELL
                            list_buy[compteur].quantity = 0 #update the quantity of the order BUY
                        else : # quantity sell < quantity buy
                            list_execution.append("Execute %d at %d on %s" %(list_sell[lastIndexSell].quantity, list_buy[compteur].price, self.name))
                            list_buy[compteur].quantity = abs(diff) #update the quantity of the order BUY
                            list_sell[lastIndexSell].quantity = 0 #update the quantity of the order SELL
                    compteur = compteur +1

            # display all the execution command
            for i in list_execution:
                print(i)

    def execute_order_buy(self):
        list_execution =[]
        list_sell=[]
        list_buy=[]
            
        for i in self.listOrder:
            if i.side=="BUY" :
                list_buy.append(i)
            else:
                list_sell.append(i)
       
        lastIndexSell = len(list_sell) -1
            
        if len(list_buy) != 0 and len(list_sell) !=0:
            if(list_buy[0].quantity <= list_sell[lastIndexSell].quantity):
                if (list_sell[lastIndexSell].price <= list_buy[0].price):
                    diff =  list_sell[lastIndexSell].quantity - list_buy[0].quantity
                    if diff == 0:
                        list_sell[lastIndexSell].quantity = 0 #update the quantity of the order SELL
                    else :
                        list_sell[lastIndexSell].quantity = diff #update the quantity of the order SELL
                    list_execution.append("Execute %d at %d on %s" %(list_buy[0].quantity, list_sell[lastIndexSell].price, self.name))
                    list_buy[0].quantity = 0 #update the quantity of the order BUY

            else : # quantity order buy >  quantity order sell
                ''' There is 2 cases, the first one is if only 1 order SELL match with the order BUY
                then we execute a slice of the quantity of the Order BUY and the remaining quantity for the order
                 SELL is 0. The second case is if several order SELL match with the order BUY, then we execute the
                 order BUY with the first order SELL until the quantity of this order SELL is 0 then we execute the
                 order BUY with the next order SELL if the price match etc etc'''

                compteur = lastIndexSell
                while 0 < compteur and list_buy[0].quantity !=0 :
                    if list_sell[compteur].price <= list_buy[0].price:
                        diff = list_buy[0].quantity - list_sell[compteur].quantity
                        if diff == 0: #quantity buy = quantity sell 
                            list_execution.append("Execute %d at %d on %s" %(list_buy[0].quantity, list_sell[compteur].price, self.name))
                            list_buy[0].quantity = 0 #update the quantity of the order BUY
                            list_sell[compteur].quantity = 0 #update the quantity of the order SELL

                        elif diff > 0 : #  quantity buy > quantity sell
                            list_execution.append("Execute %d at %d on %s" %(list_sell[compteur].quantity, list_sell[compteur].price, self.name))
                            list_buy[0].quantity = diff #update the quantity of the order BUY
                            list_sell[compteur].quantity = 0 #update the quantity of the order SELL
                            
                        else : # quantity buy < quantity sell
                            list_execution.append("Execute %d at %d on %s" %(list_buy[0].quantity, list_sell[compteur].price, self.name))
                            list_sell[compteur].quantity = abs(diff) #update the quantity of the order SELL
                            list_buy[0].quantity = 0 #update the quantity of the order BUY
                            
                    compteur = compteur - 1

            # display all the execution command
            for i in list_execution:
                print(i)

    def updateOrderBook(self):
            for i in self.listOrder:
                if i.quantity == 0:
                    self.listOrder.remove(i)

    
<<<<<<< HEAD
   

def bubbleSortBuy(listBuy): 

        n = len(listBuy) 

        if (n == 0):
            res = []
        elif (n == 1):
            res = listBuy
        else :
            # Traverse through all array elements 
            for i in range(n): 
                swapped = False
        
                # Last i elements are already in place 
                for j in range(0, n-i-1): 
        
                    # traverse the array from 0 to 
                    # n-i-1. Swap if the element  
                    # found is greater than the 
                    # next element 
                    if (listBuy[j].__lt__(listBuy[j+1]) == True) : 
                        listBuy[j],listBuy[j+1] = listBuy[j+1], listBuy[j]
                        swapped = True
                    else :
                        if (listBuy[j].__eq__(listBuy[j+1]) == True): # check the id
                            if (listBuy[j+1].iD < listBuy[j].iD):
                                listBuy[j],listBuy[j+1] = listBuy[j+1], listBuy[j]
                                swapped = True
                # IF no two elements were swapped 
                # by inner loop, then break 
                if swapped == False: 
                    break
            return listBuy 

def bubbleSortSell(listSell): 

    n = len(listSell) 
=======
def bubbleSortBuy(listBuy): 

    n = len(listBuy) 
>>>>>>> 216f1e2ba84f841335ba722ab083389b8c17c8b0

    if (n == 0):
        res = []
    elif (n == 1):
<<<<<<< HEAD
        res = listSell
    else :
    # Traverse through all array elements 
        for i in range(n): 
            swapped = False
    
            # Last i elements are already in place 
            for j in range(0, n-i-1): 
    
=======
        res = listBuy
    else :
        # Traverse through all array elements 
        for i in range(n): 
            swapped = False
    
            # Last i elements are already in place 
            for j in range(0, n-i-1): 
    
                # traverse the array from 0 to 
                # n-i-1. Swap if the element  
                # found is greater than the 
                # next element 
                if (listBuy[j].__lt__(listBuy[j+1]) == True) : 
                    listBuy[j],listBuy[j+1] = listBuy[j+1], listBuy[j]
                    swapped = True
                else :
                    if (listBuy[j].__eq__(listBuy[j+1]) == True): # check the id
                        if (listBuy[j+1].iD < listBuy[j].iD):
                            listBuy[j],listBuy[j+1] = listBuy[j+1], listBuy[j]
                            swapped = True
            # IF no two elements were swapped 
            # by inner loop, then break 
            if swapped == False: 
                break
        return listBuy 

def bubbleSortSell(listSell): 

    n = len(listSell) 

    if (n == 0):
        res = []
    elif (n == 1):
        res = listBuy
    else :
    # Traverse through all array elements 
        for i in range(n): 
            swapped = False
    
            # Last i elements are already in place 
            for j in range(0, n-i-1): 
    
>>>>>>> 216f1e2ba84f841335ba722ab083389b8c17c8b0
                # traverse the array from 0 to 
                # n-i-1. Swap if the element  
                # found is greater than the 
                # next element 
                if (listSell[j].__lt__(listSell[j+1]) == True) : 
                    listSell[j],listSell[j+1] = listSell[j+1], listSell[j]
                    swapped = True
                else :
                    if (listSell[j].__eq__(listSell[j+1]) == True): # check the id
                        if (listSell[j+1].iD < listSell[j].iD):
                            listSell[j],listSell[j+1] = listSell[j+1], listSell[j]
                            swapped = True
            # IF no two elements were swapped 
            # by inner loop, then break 
            if swapped == False: 
                break
        return listSell 

<<<<<<< HEAD
        
=======
>>>>>>> 216f1e2ba84f841335ba722ab083389b8c17c8b0

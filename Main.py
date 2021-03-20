from Book import Book
from Book import Order

def main():
    book = Book("TEST",)
    book.insert_buy(10,10.0)
    book.insert_sell(120,12.0)
    book.insert_buy(5,10.0)
    book.insert_buy(2,11.0)
    book.insert_sell(1,10.0)
    book.insert_sell(10,10.0)
    
    print( "    Affichage avec dataframe    ")
    book.display_df()


if __name__=="__main__":
    main() 
from BookS import Book
from BookS import Order

def main():
    book = Book("TEST",)
    book.insert_buy(10,10.0)
    book.insert_sell(120,12.0)
    book.insert_buy(5,10.0)
    book.insert_buy(2,11.0)
    book.insert_sell(1,10.0)
    book.insert_sell(10,10.0)

    print("test")


if __name__=="__main__":
    main() 
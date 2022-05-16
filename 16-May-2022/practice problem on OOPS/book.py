class Book:
    def __init__(self, Book_number, title, author, pages, price, copies):
        self.Book_number = Book_number
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.copies = copies

    def display(self):
        print(f'{self.title},Book_number = {self.Book_number},the price of the book is : {self.price} and the Number of copies {self.copies}')
        print('*' * 50)

    def price(self):
        return self.price

    def price(self, new_price):
        if 10 <= new_price <= 500:
            self.price = new_price
        else:
            raise ValueError('Price cannot be less than 10 or more than 500')

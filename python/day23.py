class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

class Library:
    def __init__(self):
        self.books = []

    def book_add(self,book):
        self.books.append(book)

    def book_search(self, title):
        for book in self.books:
            if book.title == title:
                print(f"{title}")

    def book_list(self):
        for book in self.books:
            print(book.title)

book1 = Book("파이썬", "홍길동", 30000)
book2 = Book("자바", "김철수", 25000)
book3 = Book("지프", "보쌈", 98000)
book4 = Book("흑구", "상추", 65000)

library = Library()
library.book_add(book1)
library.book_add(book2)
library.book_add(book3)
library.book_add(book4)

library.book_list()
library.book_search("흑구")
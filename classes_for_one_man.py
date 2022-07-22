class Book:
    books_count = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

    def __repr__(self):
        return self.name, self.year, self.author

    def __str__(self):
        return f"Author:  {self.author}\n" \
               f"Name:   {self.name}\n" \
               f"Year:   {self.year}\n"


class Author:
    main_list = []

    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = set()

    def write_new_book(self, name: str, year: int):
        # Author.main_list.append([self.name, name, year])
        book = Book(name, year, self.name).__repr__()
        if book not in self.books:
            self.books.add(book)
            Author.main_list.append([self.name, name, year])
        return book

    def __repr__(self):
        return Author.main_list

    def __str__(self):
        return f"Author: {self.name}"


class Library:

    def __init__(self):
        self.authors = set()
        self.books = set()

    def add_new_book(self, author):
        self.books.add(author[0])
        self.authors.add(author[2])
        return self.books, self.authors

    def __repr__(self):
        return self.books

    def __str__(self):
        return f"Authors: {self.authors}\n" \
               f"Books: {self.books}"


if __name__ == '__main__':
    add_book = Book('About All', 2002, 'Andry')
    add_boker = Book('About Al', 2002, 'Andrey')
    a = Library()
    a.add_new_book(add_book.__repr__())
    a.add_new_book(add_boker.__repr__())
    print(a)

# book1 = Book("gdg", "fsgsdg", "rsgdfbg")
# book2 = Book("gdg", "fsgsdg", "rsgdfbg")
# if book2 == book1:
#     print(1)
# else:
#     print(0)
# print(book1)
# print(book2)

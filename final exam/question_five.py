#quesion5
#(i)

class Book:
    def __init__(self, title, author, pages):  # Corrected to __init__
        self.title = title
        self.author = author
        self.pages = pages

    def infoAboutBook(self):
        print(f'The book "{self.title}" was written by {self.author} with {self.pages} pages.')
myBook = Book(title="Great Expectations", author="Nawamwena Nazifa", pages=2556)

myBook.infoAboutBook()

class Ebook(Book):
    def __init__(self, title, author, pages):
        super().__init__(title, author, pages) 
     
 #(ii)    
class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def get_title_and_author(self):
        return f"Title: {self.title}, Author: {self.author}"


class EBook(Book):
    def __init__(self, title, author, year, genre, format):
        super().__init__(title, author, year, genre)
        self.format = format 

    def display_info(self):
        return (f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Year: {self.year}\n"
                f"Genre: {self.genre}\n"
                f"Format: {self.format}")

ebook = EBook("1984", "Nawamwena Nazifa", 1949, "python", "PDF")
print(ebook.display_info())


#(iii)   
class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def get_title_and_author(self):
        return f"Title: {self.title}, Author: {self.author}"

my_book = Book("2002", "Nawamwena nazifa", 1949, "python")
print(my_book.get_title_and_author())
       
#(iv)
   #A class defines a set of attributes and methods that the objects created  will have.
   #An object is an instance of a class and the building blocks of object-oriented programming (OOP)


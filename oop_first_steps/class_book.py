class Book:
    def __init__(self, name:str, author:str, pages:int):
        self.name = name
        self.author = author
        self.pages = pages


mist = Book("The Mist", "King", 299)
print(mist.author)
print(mist.name)
print(mist.pages)

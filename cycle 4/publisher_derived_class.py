
class publisher:
    def __init__(self):
        self.value = "Inside Parent"

    def title(self):
        print(self.value)
        print("The fault in our stars")
    def author(self):
        print("AUTHOR OF THE BOOK::John Gren")

class book(publisher):
    def title(self):
        print("The fault in our stars")


class python(book):
    def price(self):
        print("Price of the book::300")

    def no_of_page(self):
        print("NO_OF_PAGES:250")

obj=python()
obj.title()
obj.author()
obj.price()
obj.no_of_page()
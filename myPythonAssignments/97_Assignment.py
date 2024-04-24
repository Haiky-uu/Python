# 97 read file book list and create class and functions for class book. Instantiate book object
# for every line.Find out total number of pages written by every author, number of books
# written by every author

class Book:

    def __init__(self):
        print('program')

    def books(self,b_id,b_name,b_author,b_pages,b_price):
        self.b_id = b_id
        self.b_name = b_name
        self.b_author = b_author
        self.b_pages = b_pages
        self.b_price = b_price
        #print(self.b_author,self.b_pages,self.b_name)

ls = []
with open('./books.txt') as f:
    for line in f:
        print(line)
        b_id, b_name, b_author, b_pages, b_price = line.strip().split(',')
        b = Book()
        b.books(int(b_id),b_name,b_author,int(b_pages),float(b_price))
        ls.append(b)
print(ls)
b1 = Book()

def author(ls:list):
    aut = {}
    for book in ls:
        if book.b_author in aut:
            aut[book.b_author][0]+=book.b_pages
            aut[book.b_author][1]+=1
        else:
            aut[book.b_author]=[book.b_pages,1]

    return aut

print(author(ls))


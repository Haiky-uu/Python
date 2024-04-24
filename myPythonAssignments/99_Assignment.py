# 99 read book file (create book class and functions oop) and store objects in a list

class Book:
    def __init__(self,b_id,b_name,b_author,b_pages,b_price):
        self.b_id = b_id
        self.b_name = b_name
        self.b_author = b_author
        self.b_pages = b_pages
        self.b_price = b_price


def read_store(file):
    ls = []
    with open(file) as f:
        for line in f:
            b_id,b_name,b_author,b_pages,b_price = line.strip().split(',')
            b1 = Book(b_id,b_name,b_author,b_pages,b_price)
            ls.append(b1)
    return ls

def main():
    print("Program")
    file = './books.txt'
    print(read_store(file))


if __name__ == '__main__':
    main()


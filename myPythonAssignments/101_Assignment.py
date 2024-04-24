# 101 read book file (create book class and functions oop) and store objects in a list
# and sort object list using book price

class Books:
    def __init__(self,b_id,b_name,b_author,b_pages,b_price):
        self.b_id = b_id
        self.b_name = b_name
        self.b_author = b_author
        self.b_pages = b_pages
        self.b_price = b_price


def read_file(file):
    ls = []


    with open(file) as f:
        for items in f:
            b_id, b_name, b_author, b_pages, b_price = items.strip().split(',')
            b1 = Books(b_id,b_name,b_author,b_pages,int(b_price))
            ls.append(b1)

    for i in ls:
        print(i.b_price)
    return ls


def sorting(ls):
    # Bubble sort

    n = len(ls)
    for i in range(n):
        for j in range(0, n-i-1):
            if ls[j].b_price > ls[j+1].b_price:
                ls[j], ls[j+1] = ls[j+1], ls[j]
    print("Sorted")
    # Print sorted prices
    for book in ls:
        print("Book Name: ",book.b_name,"Book_price: ",book.b_price)


def main():
    print("program")
    file = './books.txt'
    ls = read_file(file)
    sorting(ls)


if __name__ == '__main__':
    main()
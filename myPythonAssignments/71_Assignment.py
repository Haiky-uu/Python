# 71 read file book.txt store author name as key and list of books as value.
# Print author name and list of books written by that author as output


def addDict():
    books = {}
    for line in open('./books.txt'):
        book_id, book_name, author, page_no, book_price = line.strip().split(',')
        book_id = int(book_id)
        page_no = int(page_no)
        book_price = float(book_price)
        if author not in books:
            books[author] = [[book_name, book_id, page_no, book_price]]
        else:
            books[author].append([book_name, book_id, page_no, book_price])

    return books


def author(books):
    for k,v in books.items():
        #print('Author: ',k,'Book: ',v)
        for bookName in v:
            print("Author: ",k,'Book: ' ,bookName[0])


def main():
    books = addDict()
    author(books)


if __name__ == '__main__':
    main()

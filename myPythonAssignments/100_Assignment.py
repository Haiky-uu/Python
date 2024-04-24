# 100 read book file (create book class and functions oop) and store objects in a list and print
# memory ref and write them in a notebook

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
        for line in f:
            b_id, b_name, b_author, b_pages, b_price = line.strip().split(',')
            b1 = Books(b_id,b_name,b_author,b_pages,b_price)
            ls.append(b1)
    return ls


def write_file(ls):
    #print(ls[5].b_name)
    with open("./Ass100_memory_ref.csv",'a') as f:

        for item in ls:
            print(item)
            mem_add = (id(item))
            hex_add = (hex(id(item)))
            f.write("Object"+','+'Memory_add'+','+'Hex_Address'+'\n')
            f.write(str(item)+","+str(mem_add)+","+str(hex_add)+'\n')


def main():
    print("Program")
    file = './books.txt'
    ls = read_file(file)
    write_file(ls)


if __name__ == '__main__':
    main()

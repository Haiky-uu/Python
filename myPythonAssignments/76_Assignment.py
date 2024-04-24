
# 76 Read file product and print lines containing category = "Beverages"

def code(file):
    for line in open(file):
        #print(line)
        prod_id, desc, price, cat, qty = line.strip().split(',')
        if cat == 'Beverages':
            print(line)


def main():
    print('prog')
    file = './product.csv'
    code(file)


if __name__ == '__main__':
    main()

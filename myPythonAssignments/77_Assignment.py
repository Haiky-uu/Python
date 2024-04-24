# 77 read file product data and write all the lines containing category = "Condiments / Sauces" to another file

def prog(file):
   for line in open(file):
       #print(line)
       prod_id, desc, price, cat, qty = line.strip().split(',')
       if cat == 'Condiments / Sauces':
           with open('./Add_data_ass_77','a') as o:
               o.write(line)


def main():
    print('program')
    file = './product.csv'
    line = prog(file)


if __name__ == '__main__':
    main()
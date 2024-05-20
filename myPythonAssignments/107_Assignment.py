# read nse_daily_stock file (create class that stores symbol, date, closing price as attributes). Store objects in a
# list, implement algorithm to find peaks in the list (peak price) and print objects that are on the peak

from datetime import datetime

class Stock:

    def __init__(self,s_date,s_close):
        self.date = s_date
        self.close_price = s_close

def peak(stock_list):
    #print(stock_list)
    peaks = []
    valleys = []
    ascend = 0
    for i in range(len(stock_list)-1):
        if stock_list[i].close_price < stock_list[i+1].close_price+1:
            if ascend == 0:
                valleys.append(stock_list[i])
            ascend = 1
        else:
            if ascend == 1:
                peaks.append(stock_list[i])
            ascend = 0
    print(peaks)
    for obj in peaks:
       print(obj,":",obj.date,":",obj.close_price)


def main():
    stock = []
    stockObj = []
    print("Program")
    with open('./trident_stocks.csv') as f:
        next(f)
        for line in f:
            data = line.strip().split(',')
            date_ = datetime.strptime(data[0],"%d-%m-%Y").date()
            stock.append([date_, float(data[7])])

        # print(stock)
        for date,c_price in stock:
            s1 = Stock(date,c_price)
            stockObj.append(s1)

        peak(stockObj)


if __name__ == '__main__':
    main()
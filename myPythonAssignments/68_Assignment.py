# 68  Read country data file and find total population
# of every continent


def read():
    cnt =0
    d = {}
    for line in open('./countrydata.csv'):
        if cnt == 0:
            cnt+=1
            continue
        #print(line)
        c_id,country,continent,population,lifExpectancy,gdpPercapita = line.strip().split(',')
        #print(continent,population)
        population = float(population)
        #d[continent] = population
        if continent not in d.keys():
            d[continent] = population
        else:
            d[continent] += population

    return d

def printdict(dic):
    print(dic)
    for k,v in dic.items():
     print("Continent: ",k, "Population: ",v)


def main():
    dic = read()
    printdict(dic)

if __name__ == '__main__':
    main()


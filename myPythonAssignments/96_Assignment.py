# 96 read file country data and calculate average population by continent


def extract(file):
    cont_dic = {}
    with open(file) as f:
        next(f)
        for line in f:
            #print(line)
            id, country, continent, population, life_exp, gdp_per_capital = line.strip().split(',')
            population = float(population)
            if continent in cont_dic:
               cont_dic[continent][0]+=population
               cont_dic[continent][1]+=1

            else:
                cont_dic[continent] = [population,1]
    return cont_dic


def conti(cont_dic):
    for k,v in cont_dic.items():
        for items in v:
            avg_pop = v[0] / v[1]
            print("Continent = ",k,"Average pop = ",round(avg_pop, 2))
            break

def main():
    print('Welcome')
    file = './countrydata.csv'
    cont_dic = extract(file)
    conti(cont_dic)

if __name__ == '__main__':
    main()

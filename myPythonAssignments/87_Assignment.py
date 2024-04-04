# 87 read the file country data and find total population for continent
# using list and function

def fill(l1: list):
    with open('./countrydata.csv') as c:
        cnt = 0
        for line in c:
            if cnt == 0:
                cnt += 1
                continue
            # print(line)
            no, country, continent, pop, le, gdp = line.strip().split(',')
            pop = float(pop)
            l1.append(continent)
            l1.append(pop)

def find(l1: list, continent: list, population: list):
    for i in range(0, len(l1), 2):
        conti = l1[i]
        pop = l1[i+1]
        # print(conti,pop)
        if conti in continent:
            index = continent.index(conti)
            population[index] += pop
        else:
            continent.append(conti)
            population.append(pop)
    for i in range(len(continent)):
        print(f'continent: {continent[i]}, Total_population: {population[i]}')


continent  =[]
population = []
list1 = []
fill(list1)
# print(list1)
find(list1, continent, population)
# print(list2)

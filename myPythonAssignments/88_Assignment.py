# 88 read the file country data and find total
# population for continent using dictionary and function

def find(file: str):
    with open(file) as f:
        c_pop={}
        cnt = 0
        for line in f:
            if cnt == 0:
                cnt+=1
                continue
            no, country, conti, pop, le, gdp = line.strip().split(',')
            pop = float(pop)
            if conti in c_pop:
                c_pop[conti] += pop
            else:
                c_pop[conti] = pop
        return c_pop


def add(dict1: dict):
   for key,val in dict1.items():
       print(key,val)

c_dict = find('./countrydata.csv')
print(c_dict)
add(c_dict)




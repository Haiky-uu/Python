import pandas as pd
import config as cfg

df1 = pd.DataFrame([[2,4,6],[1,3,5]])
print(df1)
print(df1.columns)

df1 = pd.DataFrame([[2,4,6],[2,3,7]],columns=['age','height','weight'])
print(df1)
print(df1.columns)

df1 = pd.DataFrame([[2,5,6],[1,2,3]],index=['high','low'],columns=['age','height','weight'])
print(df1)

for col in df1.columns:
    print("columns",col)

dict_name = [{'Name':'Nishad','Age':22,'Height':7.4},{'Name':'kiran','Age':23,'Height':7.8},{'Name':'Ganesh','Age':22,'Height':7.2}]
df1 = pd.DataFrame(dict_name)
print(df1)

"""Csv files"""
# with header
path = './continentReln.csv'
df1 = pd.read_csv(path)
print(df1)
print(type(df1))
print(df1.columns)

# without header
path = './continentReln.csv'
df1 = pd.read_csv(path,header=None)
print(df1)
print("Column name by default header is none: ",df1.columns)
df1.columns=['id1','conti','new']
print("Column names after assigning columns names:",df1.columns)
print(df1)

print("\n")
path = r'./continentReln.csv'
df1=pd.read_csv(path,header=None,names=cfg.e_file_header1,usecols=[0,1,2])
print(df1)
print(df1.columns)




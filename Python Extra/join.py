import pandas

import pandas

cnDf = pandas.read_csv("continentReln.csv")
#print(cnDf)
#print(cnDf.head(3))
#print(cnDf.tail(2))

cDf = pandas.read_csv("countrydataReln.csv")
#print(cDf)
#print(cDf.head(8))
#print(cDf.tail(10))

dfJoinInner = pd.merge(cnDf,cDf, on='continent_id',how='inner')
print(dfJoinInner)

dfJoinLeft = pandas.merge(cnDf,cDf,on='continent_id', how='left')
print(dfJoinLeft)

dfJoinRight = pandas.merge(cnDf,cDf,on='continent_id',how='right')
print(dfJoinRight)

dfJoinOuter = pandas.merge(cnDf,cDf,on='continent_id',how='outer')
print(dfJoinOuter)
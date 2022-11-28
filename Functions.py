import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("/Users/nishkarsh/Programming/VS PYTHON/IP Project/Country_Medals_Converted.csv", sep=',')

x = ((5 * df['Gold']) + (3 * df['Silver']) + df['Bronze'])
df.insert(8, 'Points', x)

prevYear = df.loc[0,'Year']
rank = 1
for i in range (0,len(df.index)):
    if df.loc[i,'Year'] == prevYear:
        df.loc[i,'Rank'] = rank
        rank += 1
    else:
        prevYear = df.loc[i,'Year']
        rank = 1
        df.loc[i,'Rank'] = rank
        rank += 1

df = df.sort_values(by=['Year','Rank'],ascending=[False,True])
df = df.reset_index(drop=True)

Year_Array = np.unique(df['Year'].values)
Year_Array.sort()

Country_Array = pd.Series(index=Year_Array, dtype=pd.Int64Dtype)
for i in Year_Array:
    p = df[df['Year']==i]
    Country_Array.loc[i] = np.unique(p['Country_Name'].values)

AllCountries_List = []
for i in Country_Array:
    for j in range(0,len(i)):
        if i[j] not in AllCountries_List:
            AllCountries_List.append(i[j])
    
def Valid_Year(year):
    if year in Year_Array:
        return True
    else:
        return False
        
def First_Place(year):
    l = df[df['Year']==year]
    return df.loc[min(l.index)]

def Second_Place(year):
    l = df[df['Year']==year]
    l = l.drop(min(l.index))
    return df.loc[min(l.index)]

def Third_Place(year):
    l = df[df['Year']==year]
    l = l.drop(min(l.index))
    l = l.drop(min(l.index))
    return df.loc[min(l.index)]

def Rank(year,country):
    x = df[df['Year']==year]
    return int(x[x['Country_Name']==country]['Rank'].reset_index(drop=True)[0])

def Medals_Won(country,year):
    medals = df[df['Country_Name'] == country]
    medals = medals[medals['Year'] == year]
    total = medals['Gold']+medals['Silver']+medals['Bronze']
    total = total.reset_index(drop=True)
    return total[0]

def Point_LineGraph(country):
    x = df.loc[:,['Year','Country_Name','Points']]
    x.index = x['Year']
    x = x.drop(columns=['Year'])
    x = x.sort_index()
    plt.plot(x[x.loc[:,'Country_Name'] == country]['Points'])
    plt.xlabel('Year')
    plt.ylabel('Points')
    plt.xticks(np.arange(1894,2021,20))
    plt.show()
    
def Point_ScatterGraph(country):
    x = df.loc[:,['Year','Country_Name','Points']]
    x.index = x['Year']
    x = x.drop(columns=['Year'])
    x = x.sort_index()
    pointdata = x[x.loc[:,'Country_Name'] == country]['Points']
    plt.scatter(pointdata.index,pointdata.values)
    plt.show()
    
def MedalDist_PieChart(year):
    MedalData = pd.Series(index=Country_Array[year])
    for i in Country_Array[year]:
        MedalData.loc[i] = Medals_Won(i,year)
        
    top5 = []
    _labels = [None] * MedalData.size
    _explode = [0] * MedalData.size
    
    for i in Country_Array[year]:
        if Rank(year,i) in [1,2,3,4,5]:
            top5.append(i)
    
    for i in range(0,MedalData.index.size):
        if MedalData.index[i] in top5:
            _labels[i] = MedalData.index[i]
            _explode[i] = 0.1
    
    #print(MedalData)
    plt.figure(facecolor='white',figsize=(10,10))
    plt.pie(MedalData,labels=_labels,explode=_explode,)
    plt.show()
    
def TotalMedal_BarGraph(country):
    gold = sum(df[df.loc[:,'Country_Name'] == country]['Gold'])
    silver = sum(df[df.loc[:,'Country_Name'] == country]['Silver'])
    bronze = sum(df[df.loc[:,'Country_Name'] == country]['Bronze'])
    y = [gold,silver,bronze]
    plt.bar(['Gold','Silver','Bronze'],y,color=['Gold','Silver','#CD7F32'])
    plt.title('Medals Won by %s in Olympics (1894-2020)' %country)
    plt.ylabel('Medals Won')
    plt.show()
    
def YearWise_MedalBar(year):
    MedalData = pd.Series(index=Country_Array[year])
    for i in Country_Array[year]:
        MedalData.loc[i] = Medals_Won(i,year)
    
    top5 = []
    _ticks = [''] * MedalData.size
    
    for i in Country_Array[year]:
        if Rank(year,i) in [1,2,3,4,5]:
            top5.append(i)
            
    for i in range(0,MedalData.index.size):
        if MedalData.index[i] in top5:
            _ticks[i] = MedalData.index[i]
    
    plt.rcParams['figure.figsize'] = [15,8]
    plt.bar(MedalData.index,MedalData.values)
    #plt.xticks(ticks=_ticks,rotation='vertical')
    plt.xticks(_ticks)
    plt.show()
    
def Country_Info(country,year):
    x = df[df['Country_Name'] == country]
    x = x[x['Year']==year]
    return df.loc[x.index[0]]

def PrintData():
    return df
    
def Country_array(year):
    return Country_Array[year]

def Year_array():
    return Year_Array
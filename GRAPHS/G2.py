# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 10:12:00 2021

@author: HP
"""

import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt

df=pd.read_csv("covid_19_india.csv",parse_dates=["Date"])
df.columns
df.dtypes

for x in df.columns:
    print(x,df[x].isna().sum())
    
df['year']=df['Date'].dt.year
df['month']=df['Date'].dt.month

df=df.sort_values(by=['month'])
df.dtypes

def month(x):
    if x==1:
        return 'January'
    elif x==2:
        return 'Febraury'
    elif x==3:
        return 'March'
    elif x==4:
        return 'April'
    elif x==5:
        return 'May'
    elif x==6:
        return 'June'
    elif x==7:
        return 'July'
    elif x==8:
        return 'August'
    elif x==9:
        return 'September'
    elif x==10:
        return 'October'
    elif x==11:
        return 'November'
    elif x==12:
        return 'December'
    
df['month']=df['month'].apply(month)

c=input("Enter the State or Union Territory name: ")
y=int(input("Enter the year: "))
state_info= df[(df['State/UnionTerritory']==c) & ( df['year']==y)]
ax=sns.lineplot(
    data=state_info,
    x="month", y="Confirmed"
)
plt.xticks(rotation=70)
plt.tight_layout()
ax.set_title('No of confimed cases for '+c+' in '+str(y))

c=input("Enter the State or Union Territory name: ")
y=int(input("Enter the year: "))
state_info= df[(df['State/UnionTerritory']==c) & ( df['year']==y)]
ax=sns.lineplot(
    data=state_info,
    x="month", y="Cured"
)
plt.xticks(rotation=70)
plt.tight_layout()
ax.set_title('No of Cured cases for '+c+' in '+str(y))

c=input("Enter the State or Union Territory name: ")
y=int(input("Enter the year: "))
state_info= df[(df['State/UnionTerritory']==c) & ( df['year']==y)]
ax=sns.lineplot(
    data=state_info,
    x="month", y="Deaths"
)
plt.xticks(rotation=70)
plt.tight_layout()
ax.set_title('No of Deaths for '+c+' in '+str(y))


# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 11:27:11 2021

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
m1=int(input("Enter the from month: "))
m2=int(input("Enter the to month: "))

df=df[(df['month']>=m1) & (df['month']<=m2)]
state_info= df[(df['State/UnionTerritory']==c)]
state_info=state_info[state_info['year']==y]
    
ax=sns.lineplot(
    data=state_info,
    x="Date", y="Confirmed", hue="month"
)
plt.xticks(rotation=70)
plt.tight_layout()
ax.set_title('No of confimed cases for '+c)


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


c1=input("Enter the State or Union Territory name: ")
c2=input("Enter the State or Union Territory name: ")
c3=input("Enter the State or Union Territory name: ")
c4=input("Enter the State or Union Territory name: ")
c5=input("Enter the State or Union Territory name: ")
c6=input("Enter the State or Union Territory name: ")
c7=input("Enter the State or Union Territory name: ")
c8=input("Enter the State or Union Territory name: ")
c9=input("Enter the State or Union Territory name: ")
c10=input("Enter the State or Union Territory name: ")
y=int(input("Enter the year: "))

state_info= df[(df['State/UnionTerritory']==c1) | (df['State/UnionTerritory']==c2) | (df['State/UnionTerritory']==c3) | (df['State/UnionTerritory']==c4) | (df['State/UnionTerritory']==c5) | (df['State/UnionTerritory']==c6) | (df['State/UnionTerritory']==c7) | (df['State/UnionTerritory']==c8) | (df['State/UnionTerritory']==c9) | (df['State/UnionTerritory']==c10)]

state_info=state_info[state_info['year']==y]
    
ax=sns.lineplot(
    data=state_info,
    x="month", y="Confirmed", hue="State/UnionTerritory"
)

plt.tight_layout()
ax.set(ylim=(0))
ax.set(xlim=(0))
plt.xticks(rotation=70)
ax.set_title('No of cases for '+c1+','+c2+','+c3+','+c4+','+c5+','+c6+','+c7+','+c8+','+c9+' and '+c10+' for year '+str(y))

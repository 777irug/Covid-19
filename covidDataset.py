

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

#confirmed cases in india date-wise
#monthwise
c=input("Enter the State or Union Territory name: ")
state_info= df[df['State/UnionTerritory']==c]

ax=sns.lineplot(
    data=state_info,
    x="month", y="Confirmed", hue="year"
)
plt.xticks(rotation=70)
plt.tight_layout()
ax.set_title('No of confimed cases for '+c)

#cured
c=input("Enter the State or Union Territory name: ")
state_info= df[df['State/UnionTerritory']==c]

ax=sns.lineplot(
    data=state_info,
    x="month", y="Cured", hue="year"
)
plt.xticks(rotation=70)
plt.tight_layout()
ax.set_title('No of Cured cases for '+c)

#deaths
c=input("Enter the State or Union Territory name: ")
state_info= df[df['State/UnionTerritory']==c]

ax=sns.lineplot(
    data=state_info,
    x="month", y="Deaths", hue="year"
)
plt.xticks(rotation=70)
plt.tight_layout()
ax.set_title('No of Deaths for '+c)


#yearwise
c=input("Enter the State or Union Territory name: ")
y=int(input("Enter the year: "))
state_info= df[(df['State/UnionTerritory']==c) & ( df['year']==y)]
ax=sns.lineplot(
    data=state_info,
    x="month", y="Confirmed",hue="year", style="State/UnionTerritory",
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

ax=sns.lineplot(
    data=state_info,
    x="Date", y="Deaths"
)
plt.xticks(rotation=70)
plt.tight_layout()
ax.set_title('No of Deaths for '+c+' in '+str(y))

c=input("Enter the State or Union Territory name: ")
y=int(input("Enter the year: "))
m=input("Enter the month: ")
state_info= df[(df['State/UnionTerritory']==c) & ( df['year']==y) & (df['month']==m)]
ax=sns.lineplot(
    data=state_info,
    x="Date", y="Confirmed"
)
plt.xticks(rotation=70)
plt.tight_layout()
ax.set_title('No of confimed cases for '+c+' in '+str(m)+str(y))


c=input("Enter the State or Union Territory name: ")
y=int(input("Enter the year: "))
m=input("Enter the month: ")
state_info= df[(df['State/UnionTerritory']==c) & ( ['df['year']==y) : (df['month']==m)']]
ax=sns.lineplot(
    data=state_info,
    x="Date", y="Confirmed"
)
plt.xticks(rotation=70)
plt.tight_layout()
ax.set_title('No of confimed cases for '+c+' in '+str(m)+str(y))



#all

c=input("Enter the State/UnionTerritory: ")
country=df[df['State/UnionTerritory']==c]

ax=sns.lineplot(
    data=country,
    x="month", y="Confirmed", hue='year',
    
)




#Death




ax=sns.lineplot(
    data=country,
    x="month", y="Deaths",hue='year',
    
)

ax=sns.lineplot(
    data=country,
    x="month", y="Cured",hue='year',
    
)
ax.set_title('No of all cases for '+c)

plt.xticks(rotation=70)
plt.tight_layout()





state=df[df['State/UnionTerritory']=='Punjab']
state=state.sort_values('Date')
state=state.groupby('Date')['Confirmed'].sum().reset_index()
state=state.set_index('Date')
y = state['Confirmed'].resample('MS').mean()
y[:'2020']
y.plot(figsize=(15, 6))
plt.show()


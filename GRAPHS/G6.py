
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



state_info= df[(df['State/UnionTerritory']==c1) | (df['State/UnionTerritory']==c2)]


    
ax=sns.lineplot(
    data=state_info,
    x="month", y="Confirmed", hue="State/UnionTerritory",style="year"
)

plt.xticks(rotation=70)
plt.legend(bbox_to_anchor=(0.6, 1), loc=2, borderaxespad=0)

ax.set_title('No of cases for '+c1+','+c2+', for year '+str())

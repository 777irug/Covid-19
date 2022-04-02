import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
matplotlib.rcParams['axes.labelsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 8
matplotlib.rcParams['ytick.labelsize'] = 12
matplotlib.rcParams['text.color'] = 'k'
        # visualization
covid=pd.read_csv('covid_19_india.csv')

covid["Date"]=pd.to_datetime(covid["Date"])
datewise=covid.groupby(["Date"]).agg({"Confirmed":'sum',"Cured":'sum',"Deaths":'sum'})
datewise["Days Since"]=datewise.index-datewise.index.min()

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression,Ridge,Lasso
from sklearn.metrics import mean_squared_error,r2_score
import plotly.graph_objects as go



train_ml=datewise.iloc[:int(datewise.shape[0]*0.95)]
valid_ml=datewise.iloc[int(datewise.shape[0]*0.95):]
model_scores=[]
poly = PolynomialFeatures(degree = 8)
train_poly=poly.fit_transform(np.array(train_ml["Days Since"]).reshape(-1,1))
valid_poly=poly.fit_transform(np.array(valid_ml["Days Since"]).reshape(-1,1))
y=train_ml["Confirmed"]
linreg=LinearRegression(normalize=True)
linreg.fit(train_poly,y)
prediction_poly=linreg.predict(valid_poly)
rmse_poly=np.sqrt(mean_squared_error(valid_ml["Deaths"],prediction_poly))
model_scores.append(rmse_poly)

print("Root Mean Squared Error for Polynomial Regression: ",rmse_poly)
comp_data=poly.fit_transform(np.array(datewise["Days Since"]).reshape(-1,1))
plt.figure(figsize=(11,6))
predictions_poly=linreg.predict(comp_data)
fig=go.Figure()
fig.add_trace(go.Scatter(x=datewise.index, y=datewise["Deaths"],
        mode='lines+markers',name="Train Data for Deaths Cases"))
fig.add_trace(go.Scatter(x=datewise.index, y=predictions_poly,
                            mode='lines',name="Polynomial Regression Best Fit",
                            line=dict(color='black', dash='dot')))
fig.update_layout(title="Confirmed,Cured and Death Cases Polynomial Regression Prediction in Millions",
                        xaxis_title="Date",yaxis_title="Confirmed,Recovered and Death Cases",
                        legend=dict(x=0,y=1,traceorder="normal"))

fig.add_trace(go.Scatter(x=datewise.index, y=datewise["Confirmed"],
                    mode='lines+markers',name="Train Data for Confirmed Cases"))
fig.add_trace(go.Scatter(x=datewise.index, y=predictions_poly,
                            mode='lines',name="Polynomial Regression Best Fit",
                            line=dict(color='black', dash='dot')))
        # fig.update_layout(title="Confirmed Cases Polynomial Regression Prediction",
        #                 xaxis_title="Date",yaxis_title="Confirmed Cases",
        #                 legend=dict(x=0,y=1,traceorder="normal"))


fig.add_trace(go.Scatter(x=datewise.index, y=datewise["Cured"],
                            mode='lines+markers',name="Train Data for Cured Cases"))
fig.add_trace(go.Scatter(x=datewise.index, y=predictions_poly,
                            mode='lines',name="Polynomial Regression Best Fit",
                            line=dict(color='black', dash='dot')))
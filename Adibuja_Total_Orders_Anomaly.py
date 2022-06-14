# -*- coding: utf-8 -*-
# In[ ]:
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'


import streamlit as st
st.title('Anomaly Detection')

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime
import pandas as pd
import plotly.express as px
from fbprophet import Prophet

#!pip install fbprophet
@st.cache(allow_output_mutation=True, suppress_st_warning=True)#for streamlit


mpl.rcParams['figure.figsize'] = (10, 8)
mpl.rcParams['axes.grid'] = False

url = 'https://github.com/vikaskftpl/streamlit/blob/main/Total_Order_Amount_9June22.csv?raw=true'
df = pd.read_csv(url,index_col=0)

df['createdon']=pd.to_datetime(df['createdon']) #converted 'createdon' to 'datetime' data type

df=df.set_index('createdon').resample("D").mean() #Hourly (H), Daily (D), Monthly (M)

#st.download_report('Download Report', text_comb)
if st.button('Generate Report'):#for streamlit
    fig = px.line(df.reset_index(), x='createdon', y='OrderAmount', title='Order Trend')

    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(count=2, label="3y", step="year", stepmode="backward"),
                dict(count=3, label="5y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )
    #fig.show()
    st.write('', fig.show())#for streamlit


    #from fbprophet import Prophet

    Adibuja_df=df.reset_index()[['createdon','OrderAmount']].rename({'createdon':'ds','OrderAmount':'y'}, axis='columns') #Column name MUST be 'ds' and 'y' ONLY

    train=Adibuja_df[(Adibuja_df['ds'] >= '2020-08-1') & (Adibuja_df['ds'] <= '2021-12-31')]
    test=Adibuja_df[(Adibuja_df['ds'] > '2021-12-31')]

    #print(test.shape)
    st.write('', test.shape)

    m = Prophet(seasonality_mode='multiplicative', daily_seasonality=True, interval_width=0.95)

    m.fit(train)

    future = m.make_future_dataframe(periods=159,freq='D') #keep 'periods as per size of 'Test data e.g. 3838 rows × 2 columns'. Also check 'freq' as "H" or not 

    forecast = m.predict(future)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail() #yhat is 'Actual predicted value'

    results=pd.concat([Adibuja_df.set_index('ds')['y'],forecast.set_index('ds')[['yhat', 'yhat_lower', 'yhat_upper']]],axis=1)
    fig1 = m.plot(forecast)
    #print(fig1)
    st.write('',fig1)


    comp=m.plot_components(forecast)
    #print(comp)
    st.write('', comp)

    results['error'] = results['y'] - results['yhat']

    results["uncertainty"] = results['yhat_upper'] - results['yhat_lower']

    results[results['error'].abs() >  1.5*results['uncertainty']] #IMP As per Business, change 1.5, as per data centered around

    results['anomaly'] = results.apply(lambda x: 'Yes' if(np.abs(x['error']) >  1.5*x['uncertainty']) else 'No', axis=1)

    fig = px.scatter(results.reset_index(), x='ds', y='y', color='anomaly', title='Adibuja Demand')


    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(count=2, label="3y", step="year", stepmode="backward"),
                dict(count=3, label="5y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )
    #print(fig.show())
    st.write('', fig.show())

else:    pass

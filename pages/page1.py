import streamlit as st 
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px 
import seaborn as sns
import matplotlib.pyplot as plt
import base64


df=pd.read_csv('Marketwise_Price_Arrival_05-01-2026_02-23-10_PM.csv')
df.rename(columns={'Unnamed: 0':'Group','Unnamed: 1':'Crop','Unnamed: 2':'MSP','Unnamed: 3':'PRICE 3/1/26','Marketwise Price & Arrival Report (03-01-2026)':'PRICE 2/1/26','Unnamed: 5':'PRICE 1/1/26','Unnamed: 6':'ARRIVAL 3/1/26','Unnamed: 7':'ARRIVAL 2/1/26','Unnamed: 8':'ARRIVAL 1/1/26'},inplace=True)
df.drop([0,1],inplace=True,axis=0)
df
res_index= df.loc[:,'Group',].value_counts().index
with st.sidebar:
    selected_res= st.selectbox(label='Group', options=res_index)

df_selected= df[df.loc[:,'Group']==selected_res]
print(df_selected.columns)
df_selected=df_selected.sort_values(by='MSP',ascending=False)
st.write(df_selected)

ch=px.pie(df_selected,names='Crop',values='PRICE 3/1/26',title='price in rupees')
st.plotly_chart(ch)
ch1=px.pie(df_selected,names='Crop',values='ARRIVAL 3/1/26',title='in metric tonnes')
st.plotly_chart(ch1)
ch2=px.bar_polar(df_selected,r='PRICE 3/1/26',theta='ARRIVAL 3/1/26',color='MSP')
st.plotly_chart(ch2)


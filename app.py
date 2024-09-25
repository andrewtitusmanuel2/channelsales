import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Wholesale Customer Data")
data=pd.read_csv('Wholesale_customers_data.csv')
with st.expander('Show Data'):
    st.dataframe(data)

regions=['Ahmedabad','Bangalore','Chennai']
option1=st.sidebar.selectbox('Select Region',[1,2,3],format_func=lambda x:regions[x-1])

df = data[data["Region"]==option1]
#st.write(df)

option2=st.sidebar.selectbox('Select Channel', [1,2])
df1 = df[df['Channel'] == option2]
#st.write(df1)

col1,col2,col3 = st.columns(3)
with col1:
    col1.metric('Total Fresh',value=round(df1['Fresh'].sum()))
with col2:
    col2.metric('Total Milk',value=round(df1['Milk'].sum()))
with col3:
    col3.metric('Total Grocery',value=round(df1['Grocery'].sum()))
with col1:
    col1.metric('Total Frozen',value=round(df1['Frozen'].sum()))
with col2:
    col2.metric('Total Detergents',value=round(df1['Detergents_Paper'].sum()))
with col3:
    col3.metric('Total Delicassen',value=round(df1['Delicassen'].sum()))

totals = [
    df1['Fresh'].sum(), 
    df1['Milk'].sum(), 
    df1['Grocery'].sum(), 
    df1['Frozen'].sum(), 
    df1['Detergents_Paper'].sum(), 
    df1['Delicassen'].sum()]

fig=px.bar(x=['Fresh', 'Milk', 'Grocery','Frozen','Detergents_Paper','Delicassen'],y=totals,title="Sales",labels={'x': 'Categories', 'y': 'Total Sales'})

st.plotly_chart(fig)

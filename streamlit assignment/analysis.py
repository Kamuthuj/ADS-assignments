import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st

df1=pd.read_csv("Vgsales1.csv")

st.title("Game sales analysis.")
st.write("The analysis below is used to show the different sales of games in different parts of the continets over time.")

st.write("Classifying games based on Genre and their global sales.")
df1.groupby("Genre")["Global_Sales"].sum().reset_index().sort_values(by="Global_Sales",ascending=False).head()
net_sales=px.bar(df1,x="Genre",y="Global_Sales",color="Genre")
st.plotly_chart(net_sales)
st.write("Categorizing best selling games based on continent")

col1,col2= st.columns(2)
with col1:
    st.subheader("NA top seller.")
    fig=px.bar(df1,x="Genre",y="NA_Sales",color="Genre")
    st.plotly_chart(fig)
with col2:
    st.subheader("EU top seller.")
    fig=px.bar(df1,x="Genre",y="EU_Sales",color="Genre")
    st.plotly_chart(fig)

col3,col4=st.columns(2)
with col3:
    st.subheader("JP top seller")
    fig=px.bar(df1,x="Genre",y="JP_Sales",color="Genre")
    st.plotly_chart(fig)

with col4:
    st.subheader("Other continents")
    fig=px.bar(df1,x="Genre",y="Other_Sales",color="Genre")
    st.plotly_chart(fig)

st.sidebar.write("TOP INSIGHTS.")
selection=st.sidebar.selectbox("Select One",["Top 10 game seller globally","Top 10 platforms","Top 10 years of sales"])

if selection=="Top 10 game seller globally":
    st.write("Top 10 performing games globally")
    fig=df1.groupby("Genre")["Global_Sales"].sum().reset_index().sort_values(by="Global_Sales",ascending=False).head(10)
    st.dataframe(fig)
elif selection == "Top 10 platforms":
    st.write("Top 10 platforms")
    fig=df1.groupby("Platform")["Global_Sales"].sum().reset_index().sort_values(by="Global_Sales",ascending=False).head(10)
    st.dataframe(fig)
else:
    st.write("Top 10 years of sales")
    fig=df1.groupby("Year")["Global_Sales"].sum().reset_index().sort_values(by="Global_Sales",ascending=False).head(10)
    st.dataframe(fig)

st.write("The above gives visualizations of performances of game sales based on different things such as Sales,Genre and also Years where there were most and least sales.")

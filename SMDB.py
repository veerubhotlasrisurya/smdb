import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.express as px
import plotly.graph_objects as go
import datetime as datetime



st.title("Stock Dashboard")

with st.expander("Select Stock"):
    ticker = st.text_input("Ticker")
    ques = st.radio("Do you want to show Maximum Period",("Yes","No"))
    if ques == "Yes":
        maxperiod = max
    else:
        sdate= st.date_input("Start Date")
        edate= st.date_input("End Date")
if ques == "Yes":
    data = yf.download(ticker,period = max)
else:
    data = yf.download(ticker, start= sdate, end = edate)

st.subheader("Stock Chart of " +ticker)
candlestick = go.Candlestick(
                            x=data.index,
                            open=data['Open'],
                            high=data['High'],
                            low=data['Low'],
                            close=data['Close']
                            )

fig = go.Figure(data=[candlestick])

st.plotly_chart(fig)
st.subheader("Price Movements")
st.dataframe(data.tail(7))


st.cache_data
def convert_df(data):
   return data.to_csv(index=True).encode('utf-8')


csv = convert_df(data)

st.download_button(
   "Download CSV",
   csv,
   "file.csv",
   "text/csv",
   key='download-csv'
)

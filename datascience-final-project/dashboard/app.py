import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Sales Data Dashboard")
df = pd.read_csv("data/sales_data.csv")

st.subheader("Dataset Preview")
st.write(df)

st.subheader("Sales Trend")
fig, ax = plt.subplots()
ax.plot(df["Date"], df["Sales"])
st.pyplot(fig)

st.subheader("Top Products")
fig2, ax2 = plt.subplots()
df.groupby("Product")["Revenue"].sum().plot(kind="bar", ax=ax2)
st.pyplot(fig2)
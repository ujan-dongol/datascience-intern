import streamlit as st
import pandas as pd
import plotly.express as px
import os
st.title("YouTube Data Dashboard")

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(BASE_DIR, "data", "youtube_data.csv")

df = pd.read_csv(file_path)

st.subheader("Dataset Overview")
st.write(df)

total_views = df["views"].sum()
total_likes = df["likes"].sum()
st.metric("Total Views", total_views)
st.metric("Total Likes", total_likes)

# Views by video
fig1 = px.bar(df,
              x="video_title",
              y="views",
              title="Views by Video")

st.plotly_chart(fig1)

# Likes vs Views
fig2 = px.scatter(df,
                  x="views",
                  y="likes",
                  size="comments",
                  hover_name="video_title",
                  title="Views vs Likes")

st.plotly_chart(fig2)

# Upload trend
df["date"] = pd.to_datetime(df["date"])

fig3 = px.line(df,
               x="date",
               y="views",
               title="Views Trend Over Time")

st.plotly_chart(fig3)

selected_video = st.sidebar.selectbox("Select Video", df["video_title"])
filtered_df = df[df["video_title"] == selected_video]
st.write(filtered_df)

fig1 = px.bar(df, x="video_title", y="views", title="Views by Video", template="plotly_dark")
 
import streamlit as st
import lorem
import pandas as pd

df = pd.read_csv("data.csv")

st.set_page_config(layout="wide")

st.title("The Best Company")
st.write(lorem.paragraph())
st.subheader("Our Team")

col1,col2,col3 = st.columns(3)

with col1:
    for index,row in df[:4].iterrows():
        st.subheader(row["first name"].title() + " " + row["last name"].title())
        st.write(row["role"].title())
        st.image(f"images/{index+1}.png")
with col2:
    for index,row in df[4:8].iterrows():
        st.subheader(row["first name"].title() + " " + row["last name"].title())
        st.write(row["role"].title())
        st.image(f"images/{index+1}.png")
with col3:
    for index,row in df[8:].iterrows():
        st.subheader(row["first name"].title() + " " + row["last name"].title())
        st.write(row["role"].title())
        st.image(f"images/{index+1}.png")


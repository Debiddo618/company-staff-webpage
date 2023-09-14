import streamlit as st
import pandas as pd

df = pd.read_csv("data.csv")

st.set_page_config(layout="wide")

st.title("The Best Company")
st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam hendrerit nisi sed sollicitudin pellentesque. Nunc posuere purus rhoncus pulvinar aliquam. Ut aliquet tristique nisl vitae volutpat. Nulla aliquet porttitor venenatis. Donec a dui et dui fringilla consectetur id nec massa. Aliquam erat volutpat. Sed ut dui ut lacus dictum fermentum vel tincidunt neque. Sed sed lacinia lectus. Duis sit amet sodales felis. Duis nunc eros, mattis at dui ac, convallis semper risus. In adipiscing ultrices tellus, in suscipit massa vehicula eu.")
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


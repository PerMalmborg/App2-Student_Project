import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("The Best Company")
content = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod 
tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit 
in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui 
officia deserunt mollit anim id est laborum."""
st.markdown(content)
st.header("Our Team")

col1, empty_col1, col2, empty_col2, col3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=",")

#Variable checking how many rows in CSV
total_rows = len(df)
base, remainder = divmod(total_rows,3)
col1_nr = base + (1 if remainder > 0 else 0)
col2_nr = base + (1 if remainder > 1 else 0) + col1_nr


with col1:
    for index, row in df[:col1_nr].iterrows():
        full_name = f"{row['first name']} {row['last name']}"
        st.header(full_name.title())
        st.markdown(row['role'])
        st.image("images/" + row['image'])

with col2:
    for index, row in df[col1_nr:col2_nr].iterrows():
        full_name = f"{row['first name']} {row['last name']}"
        st.header(full_name.title())
        st.markdown(row['role'])
        st.image("images/" + row['image'])

with col3:
    for index, row in df[col2_nr:].iterrows():
        full_name = f"{row['first name']} {row['last name']}"
        st.header(full_name.title())
        st.markdown(row['role'])
        st.image("images/" + row['image'])

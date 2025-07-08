import streamlit as st
import pandas
st.set_page_config(layout="wide")

st.header("company project")
content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. " \
"Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat." \
" Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur." \
" Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"
st.write(content)

st.header("OUR TEAM")
col1, col2, col3 = st.columns(3)
# reading the csv data 
df = pandas.read_csv(r"C:\Users\Arun JH\Desktop\vaibhavi-proj\company_pro\venv\data (2).csv")

with col1:
     for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images (2)/" + row["image"])
       

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images (2)/" + row["image"])
with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images (2)/" + row["image"])  
              

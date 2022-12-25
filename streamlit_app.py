import streamlit as st
import pandas as pd

# st.title('This is my first program in github')
st.header('Breakfast menu of Royal Hotel')
st.text('Poha and Masala Tea')
st.text('Samosa and Kachori')
st.text('Edli and Sambhar') 
my_fruits_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
st.dataframe(my_fruits_list)



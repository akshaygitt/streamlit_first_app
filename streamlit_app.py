import streamlit as st
import pandas as pd

# st.title('This is my first program in github')
st.header('Breakfast menu of Royal Hotel')
st.text('Poha and Masala Tea')
st.text('Samosa and Kachori')
st.text('Edli and Sambhar') 
st.title('Here we are taking data from amazon s3 bucket') 
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruit_selected = st.multiselect("Pick any fruits from this list: ", list(my_fruit_list.index),["Orange","Pineapple","Banana"])
fruit_show = my_fruit_list.loc[fruit_selected]
st.dataframe(fruit_show)



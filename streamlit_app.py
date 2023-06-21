import streamlit
import pandas

streamlit.title("Pop's Diner")
streamlit.header("Menu")
streamlit.text("Avacado Toast 🥑🍞")
streamlit.text("Chicken Sandwich 🐔")
streamlit.text("Toamto Soup 🥣")
streamlit.text("Greek Salad 🥗")
streamlit.text("Ramen 🍜")

streamlit.header("🍏🍊 Make Your Own Smoothie 🍌🍉")
my_fruit_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

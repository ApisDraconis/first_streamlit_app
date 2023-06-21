import streamlit
import pandas

streamlit.title("Pop's Diner")
streamlit.header("Menu")
streamlit.text("Avacado Toast 🥑🍞")
streamlit.text("Chicken Sandwich 🐔")
streamlit.text("Toamto Soup 🥣")
streamlit.text("Greek Salad 🥗")
streamlit.text("Ramen 🍜")

my_fruits_csv = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruits_csv)

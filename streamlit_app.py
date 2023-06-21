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
my_fruits_csv = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruits_csv = my_fruits_csv.set_index("Fruit")

streamlit.multi_select("Picked some Fruits: ", list(my_fruits_csv.index))
streamlit.dataframe(my_fruits_csv)

import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


streamlit.title("Pop's Diner")
streamlit.header("Menu")
streamlit.text("Avacado Toast 🥑🍞")
streamlit.text("Chicken Sandwich 🐔")
streamlit.text("Toamto Soup 🥣")
streamlit.text("Greek Salad 🥗")
streamlit.text("Ramen 🍜")

streamlit.header("🍏🍊 Make Your Own Smoothie 🍌🍉")
my_fruit_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt") # reading the csv file and storing it in a variable
my_fruit_list = my_fruit_list.set_index('Fruit') # setting the fruit(name) as the index

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries']) #streamlit multiselect option/ adding the selected fruit(name) to a list
fruits_to_show = my_fruit_list.loc[fruits_selected]  #used for showing the selected fruits alone
streamlit.dataframe(fruits_to_show) #revamping the retrieved result set with streamlit


# Define the function to get data from Fruityvice API
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice) # getting result set from api 
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json()) # converting the result set tojson format
    return fruityvice_normalized
# New section to display Fruityvice API response
streamlit.header('Fruityvice Fruit Advice!')
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?', 'kiwi') # input
    if not fruit_choice: #if no input
        streamlit.error("Please select a fruit to get information.")
    else:
        back_from_function = get_fruityvice_data(fruit_choice) #if input is present, pass the fruit choice into the function
        streamlit.dataframe(back_from_function)
except Exception as e:
    streamlit.error("An error occurred: " + str(e))
      
      
# Snowflake-related
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * FROM fruit_load_list")  # selecting everything from fruit load list
        return my_cur.fetchall()

# Main section
streamlit.header("View Our Fruit List - Add Your Favourites")

# Add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list() #calling the fruit load function
    my_cnx.close()
    streamlit.dataframe(my_data_rows)

# Allow the end user to add a fruit to the list
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("INSERT INTO fruit_load_list VALUES ('" + new_fruit + "')") #inserting the new fruit
    return "Thanks for adding " + new_fruit

# Main section
add_my_fruit = streamlit.text_input('What fruit would you like to add?')

if streamlit.button('Add a Fruit to the List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_my_fruit) # function called here
    streamlit.text(back_from_function)




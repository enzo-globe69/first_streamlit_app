import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Almusal Menu')
streamlit.text('🥣 Aligue Sinangag with Tinapa Flakes')
streamlit.text('🥗 Kamote, Kangkong, at Boba Milk Tea')
streamlit.text('🥚 Nilagang itlog galing sa lakwatserong manok')
streamlit.text('🥑🍞 Tustadong Avocado')

streamlit.header('🍌🥭 Gawa kayo ng sariling niyonh Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

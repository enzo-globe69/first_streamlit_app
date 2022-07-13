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
streamlit.dataframe(my_fruit_list)

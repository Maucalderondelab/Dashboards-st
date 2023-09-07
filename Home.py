# To run this aplication we have to run this code in the terminal
# streamlit run app.py  

import streamlit as st
import pandas as pd
import numpy as np

# Packages for streamlit
import folium 
from streamlit_folium import folium_static
import plotly.express as px


st.set_page_config(page_title = "Dashboards",
                   layout='wide', 
                   initial_sidebar_state='expanded',
                   menu_items={ 'About': "https://www.linkedin.com/in/mcalderondelab/"}
                   
                   )

st.header('Dashboards')
st.subheader('Introduction')
st.markdown('Welcome to my interactive dashboards!! I am showcaising various data visualization styles and layouts created using Streamlit. Each page highlights diverse data presentations techniques ')
st.subheader('The different 3 layouts')
markdown_text = """
* **Dashboard1:** Explore a playground of graphical diversity with twoo sub-tabs, each offering data visualizations like pie and area charts.

* **Dashboard2:** Dive into an array of captivating chart styles, including donut charts, histograms, and meticulously designed layouts.

* **Dashboard3:** Experience clean and straightforward data visualization with an interactive histogram, allowing exploration of data for different years.
"""

st.markdown(markdown_text)
def generate_popup_content(link, name):
    return f'<a href="{link}" target="_blank">{name}</a>'


col1, col2 = st.columns([3,1])

with col1:
    with st.container():
  
        bolivia_boundary = 'https://raw.githubusercontent.com/johan/world.geo.json/master/countries/BOL.geo.json'
        map_data = folium.Map(location=[-16.2902, -63.5887], zoom_start=4.5, tiles='CartoDB positron')
        folium.GeoJson(
        bolivia_boundary,
        name='Bolivia',
        style_function=lambda feature: {
        'fillColor': 'orange',
        'color': 'orange',
        'weight': 2,
        'fillOpacity': 0.3
            }).add_to(map_data)
            # Add markers or shapes to the map
        # Add markers with hyperlinks to the map
        folium.Marker([-15.830572,-68.566876 ], popup=generate_popup_content('https://github.com/Maucalderondelab', 'My github')).add_to(map_data)
        folium.Marker([-16.631915,-67.789988 ], popup=generate_popup_content('https://www.linkedin.com/in/mcalderondelab/', 'My linkedin')).add_to(map_data)
                    # Display the folium map using streamlit-folium
        folium_static(map_data, height=380)
with col2:
    st.markdown("<h3 style='color: black; font-size: 20px;'>This map just shows my hometown and if you want you can visit my github or my linkedin :) </h3>", unsafe_allow_html=True)
    st.markdown('Btw all the data is is generated randomly at the time each page is loaded.')   
#


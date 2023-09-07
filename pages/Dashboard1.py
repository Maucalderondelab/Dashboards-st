import pandas as pd 
import numpy as np
#For Streamlit
import streamlit as st
import plotly.express as px
from my_module import store_graph_df, month_name, year_range, specific_data
from my_module import today


st.set_page_config(page_title = "Dashboard 1",
                     layout='wide', 
                     initial_sidebar_state='collapsed',
                     menu_items={ 'About': "https://www.linkedin.com/in/mcalderondelab/"}
                   )

st.title('Dashboard 1')
tab_titles = [
   "Metrics 1",
   "Metrics 2"
   ]
tabs = st.tabs(tab_titles)

chart_width = 350
chart_height = 350

years = [2023, 2022]

# Include the CSS styles
with open('style.css') as f:
    css_styles = f'<style>{f.read()}</style>'
st.markdown(css_styles, unsafe_allow_html=True)
######################################################################################################################################################################
######################################################################################################################################################################
# Filtramos el tipo de dato por año y mes
year_name  = int(today.strftime('%Y'))
desired_years = year_range(2022, 2023)
desired_year = year_name
actual_year  = int(today.strftime('%Y'))
actual_month = int(today.strftime('%m'))
desired_months = list(range(1, 13))
desired_month_names = [month_name(x-(actual_month-12)) for x in desired_months]
num_months = 12
num_data = 6

with tabs[0]:
   data_array = np.random.rand(num_months, num_data) * 5
   columns = ['Data A', 'Data B', 'Data C', 'Data D', 'Data E', 'Data F']
   month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August','September','October','November','December']
   final1_df, graph1_df = store_graph_df(data_array, columns)
   st.subheader('')
   
   col1, col2, col3 = st.columns([0.3,0.3,0.4])
   with col1: 
      pie_A = px.pie(final1_df[actual_month], names='Data', values = 'Weight [kg]',
                  color_discrete_sequence=px.colors.sequential.RdBu)
      pie_A.update_layout(title_text=f'Data for {month_name(actual_month-(actual_month-1))} {year_name}',width=chart_width, height=chart_height)
      st.plotly_chart(pie_A)
   with col2:
      pie_B = px.pie(final1_df[actual_month-1], names='Data', values = 'Weight [kg]',
                  color_discrete_sequence=px.colors.sequential.RdBu)
      pie_B.update_layout(title_text=f'Data for {month_name(actual_month-(actual_month-2))} {year_name}', width=chart_width, height=chart_height)
      st.plotly_chart(pie_B)
   with col3:
      st.write(f'<span style="color:black;"><b> The data in {month_name(1)} compared to the previous month</b></span>', unsafe_allow_html=True)

      actual_month_A = round(specific_data(graph1_df,specific=columns[0],specific_mes=month_name(1)),2)
      actual_month_B = round(specific_data(graph1_df,specific=columns[1],specific_mes=month_name(1)),2)
      actual_month_C = round(specific_data(graph1_df,specific=columns[2],specific_mes=month_name(1)),2)
      actual_month_D = round(specific_data(graph1_df,specific=columns[3],specific_mes=month_name(1)),2)
      actual_month_E = round(specific_data(graph1_df,specific=columns[4],specific_mes=month_name(1)),2)
      actual_month_F = round(specific_data(graph1_df,specific=columns[5],specific_mes=month_name(1)),2)

      previous_month_A = round(specific_data(graph1_df,specific=columns[0],specific_mes=month_name(2)),2)
      previous_month_B = round(specific_data(graph1_df,specific=columns[1],specific_mes=month_name(2)),2)
      previous_month_C = round(specific_data(graph1_df,specific=columns[2],specific_mes=month_name(2)),2)
      previous_month_D = round(specific_data(graph1_df,specific=columns[3],specific_mes=month_name(2)),2)
      previous_month_E = round(specific_data(graph1_df,specific=columns[4],specific_mes=month_name(2)),2)
      previous_month_F = round(specific_data(graph1_df,specific=columns[5],specific_mes=month_name(2)),2)
      
      delta_A= float(actual_month_A)-float(previous_month_A)
      delta_B= float(actual_month_B)-float(previous_month_B)
      delta_C= float(actual_month_C)-float(previous_month_C)
      delta_D= float(actual_month_D)-float(previous_month_D)
      delta_E= float(actual_month_E)-float(previous_month_E)
      delta_F= float(actual_month_F)-float(previous_month_F)
         
      col1, col2, col3 = st.columns(3)
      with col1:
         st.metric(label=f"{columns[0]}", value=actual_month_A, delta=round(delta_A,2))
      with col2:
         st.metric(label=f"{columns[1]}", value=previous_month_B, delta=round(delta_B,2))
      with col3:
         st.metric(label=f"{columns[2]}", value=actual_month_C, delta=round(delta_C,2))
      col1, col2, col3 = st.columns(3)   
      with col1:
         st.metric(label=f"{columns[3]}", value=actual_month_D, delta=round(delta_D,2))
      with col2:
         st.metric(label=f"{columns[4]}", value=actual_month_E, delta=round(delta_E,2))
      with col3:
         st.metric(label=f"{columns[5]}", value=actual_month_F, delta=round(delta_F,2))
       
   hist_A = px.area(graph1_df, x= 'Month', y ='Weight [kg]', color = 'Data',
                     color_discrete_sequence=px.colors.sequential.RdBu)

   col1, col2 = st.columns([1, 2])

   with col1:
      st.dataframe(graph1_df,width=4000, height=600)
   with col2:
      selected_year_1 = st.selectbox('Select Year', years)
      hist_A.update_layout(title_text=f'Anual Data {selected_year_1}',width=950, height=450)
      st.plotly_chart(hist_A)  


######################################################################################################################################################################
######################################################################################################################################################################
with tabs[1]:
   data_array = np.random.rand(num_months, num_data) * 3
   columns = ['Data A', 'Data B', 'Data C', 'Data D', 'Data E', 'Data F']
   month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August','September','October','November','December']  
   final2_df, graph2_df = store_graph_df(data_array, columns)
   st.subheader('')
   
   col1, col2, col3 = st.columns([0.3,0.3,0.4])
   with col1: 
      pie_C = px.pie(final2_df[actual_month], names='Data', values = 'Weight [kg]',
            color_discrete_sequence= px.colors.sequential.Viridis)
      pie_C.update_layout(title_text=f'Data for {month_name(actual_month-(actual_month-1))} {year_name}',width=chart_width, height=chart_height)
      st.plotly_chart(pie_C)   
   with col2:
      pie_D = px.pie(final2_df[actual_month-2], names='Data', values = 'Weight [kg]',
            color_discrete_sequence= px.colors.sequential.Viridis)
      pie_D.update_layout(title_text=f'Data for {month_name(actual_month-(actual_month-2))} {year_name}',width=chart_width, height=chart_height)
      st.plotly_chart(pie_D)
   with col3:
      st.write(f'<span style="color:black;"><b>The data in {month_name(1)} compared to the previous month</b></span>', unsafe_allow_html=True)
      actual_month_A = round(specific_data(graph1_df,specific=columns[0],specific_mes=month_name(1)),2)
      actual_month_B = round(specific_data(graph1_df,specific=columns[1],specific_mes=month_name(1)),2)
      actual_month_C = round(specific_data(graph1_df,specific=columns[2],specific_mes=month_name(1)),2)
      actual_month_D = round(specific_data(graph1_df,specific=columns[3],specific_mes=month_name(1)),2)
      actual_month_E = round(specific_data(graph1_df,specific=columns[4],specific_mes=month_name(1)),2)
      actual_month_F = round(specific_data(graph1_df,specific=columns[5],specific_mes=month_name(1)),2)

      previous_month_A = round(specific_data(graph1_df,specific=columns[0],specific_mes=month_name(2)),2)
      previous_month_B = round(specific_data(graph1_df,specific=columns[1],specific_mes=month_name(2)),2)
      previous_month_C = round(specific_data(graph1_df,specific=columns[2],specific_mes=month_name(2)),2)
      previous_month_D = round(specific_data(graph1_df,specific=columns[3],specific_mes=month_name(2)),2)
      previous_month_E = round(specific_data(graph1_df,specific=columns[4],specific_mes=month_name(2)),2)
      previous_month_F = round(specific_data(graph1_df,specific=columns[5],specific_mes=month_name(2)),2)
      
      delta_A= float(actual_month_A)-float(previous_month_A)
      delta_B= float(actual_month_B)-float(previous_month_B)
      delta_C= float(actual_month_C)-float(previous_month_C)
      delta_D= float(actual_month_D)-float(previous_month_D)
      delta_E= float(actual_month_E)-float(previous_month_E)
      delta_F= float(actual_month_F)-float(previous_month_F)
         
      col1, col2, col3 = st.columns(3)
      with col1:
         st.metric(label=f"{columns[0]}", value=actual_month_A, delta=round(delta_A,2))
      with col2:
         st.metric(label=f"{columns[1]}", value=previous_month_B, delta=round(delta_B,2))
      with col3:
         st.metric(label=f"{columns[2]}", value=actual_month_C, delta=round(delta_C,2))
      col1, col2, col3 = st.columns(3)   
      with col1:
         st.metric(label=f"{columns[3]}", value=actual_month_D, delta=round(delta_D,2))
      with col2:
         st.metric(label=f"{columns[4]}", value=actual_month_E, delta=round(delta_E,2))
      with col3:
         st.metric(label=f"{columns[5]}", value=actual_month_F, delta=round(delta_F,2))

   hist_B = px.area(graph2_df, x='Month', y = 'Weight [kg]', color = 'Data',
             color_discrete_sequence= px.colors.sequential.Viridis)
   col1, col2 = st.columns([1, 2])
   with col1:
      st.dataframe(graph2_df,width=4000, height=600)
   with col2:
      selected_year_2 = st.selectbox('Select Year ', years)
      hist_B.update_layout(title_text=f'Anual data {selected_year_2}',width=950, height=450)
      st.plotly_chart(hist_B)      


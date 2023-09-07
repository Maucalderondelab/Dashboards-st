import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
from my_module import month_name, year_range, filter_year_month
from my_module import today
import plotly.graph_objects as go


st.set_page_config(page_title = "Dahsboard 2",
                   layout='wide', 
                   initial_sidebar_state='collapsed',
                   menu_items={ 'About': "https://www.linkedin.com/in/mcalderondelab/"}
                   )

st.title('Dashboard 2')
tab_titles = [
   'Metrics 1'
    ]
tabs = st.tabs(tab_titles)

chart_width = 380
chart_height = 400
# let's create the dataframe for the test

# Define the years and months

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August','September','October','November','December']  

# Create an empty list to store data for each row
data = []

# Loop through years and months to generate random data
for year in (list(range(2019, 2024))):
    for month in months:
        row = {
            'Year': year,
            'Month': month,
            'Data AA': np.random.randint(1000, 5000),
            'Data AB': np.random.randint(500, 2000)
        }
        data.append(row)

# Create the DataFrame
data = pd.DataFrame(data)


####################################################################################################################################################################
####################################################################################################################################################################
# Filtramos el tipo de dato por año y mes
year_name  = int(today.strftime('%Y'))
desired_years = year_range(2022, 2023)
desired_year = year_name
actual_year  = int(today.strftime('%Y'))
actual_month = int(today.strftime('%m'))

desired_months = list(range(1, 13))
# Convert the desired month numbers to month names
desired_month_names = [month_name(x-(actual_month-12)) for x in desired_months]
####################################################################################################################################################################
#################################################################################################################################################################### 
AA_actualmonth = filter_year_month(data, desired_years=[desired_year], desired_month_names=[month_name(1)], columns=['Year', 'Month','Data AA', 'Data AB'])
AA_pastlmonth = filter_year_month(data, desired_years=[desired_year], desired_month_names=[month_name(2)], columns=['Year', 'Month','Data AA', 'Data AB'])

AA_2019 = filter_year_month(data, desired_years=[2019], desired_month_names=desired_month_names, columns=['Year', 'Month','Data AA', 'Data AB'])
AA_2020 = filter_year_month(data, desired_years=[2020], desired_month_names=desired_month_names, columns=['Year', 'Month','Data AA', 'Data AB'])
AA_2021 = filter_year_month(data, desired_years=[2021], desired_month_names=desired_month_names, columns=['Year', 'Month','Data AA', 'Data AB'])
AA_2022 = filter_year_month(data, desired_years=[2022], desired_month_names=desired_month_names, columns=['Year', 'Month','Data AA', 'Data AB'])
AA_2023 = filter_year_month(data, desired_years=[desired_year], desired_month_names=desired_month_names, columns=['Year', 'Month','Data AA', 'Data AB'])


with tabs[0]:
    years_AA = [2023,2022,2021,2020,2019]
    year_filtered_data = {
        2023: AA_2023[(AA_2023 != 0).all(axis=1)],
        2022: AA_2022[(AA_2022 != 0).all(axis=1)],
        2021: AA_2021[(AA_2021 != 0).all(axis=1)],
        2020: AA_2020[(AA_2020 != 0).all(axis=1)],
        2019: AA_2019[(AA_2019 != 0).all(axis=1)],
    }

    year_figs = {}
    for year, year_df in year_filtered_data.items():
        year_figs[year] = px.bar(
            year_df,
            x='Date',
            y=['Data AA', 'Data AB'],
            text_auto=True,
            color_discrete_map={'Data AA': '#F0FFFF','Data AB': '#8c393c'}
        )
        year_figs[year].update_layout(
            title_text=f'Anual Data for ({year})',
            width=1400,
            height=500
        )

    selected_year = st.selectbox('Select year', years_AA)
    st.plotly_chart(year_figs[selected_year])
    col1, col2, col3 = st.columns(3)
    with col1:
        pie_ele = pd.DataFrame({
            'columns': ['Data AA', 'Data AB'],
            'values': [AA_actualmonth['Data AA'].sum(), AA_actualmonth['Data AB'].sum()]
            })
        donut_chart = go.Figure(go.Pie(
            labels=pie_ele['columns'],
            values=pie_ele['values'],
            marker=dict(colors=['#F0FFFF','#8c393c']),
            hole=0.3
        ))
        donut_chart.update_layout(
            title_text=f'Comparison between Data AA and Data AB {month_name(1)}',
            width=chart_width, height=chart_height
        )
        st.plotly_chart(donut_chart)

    with col2:
        pie_ele = pd.DataFrame({
            'columns': ['Data AA', 'Data AB'],
            'values': [AA_pastlmonth['Data AA'].sum(), AA_pastlmonth['Data AB'].sum()]
            })
        donut_chart = go.Figure(go.Pie(
            labels=pie_ele['columns'],
            values=pie_ele['values'],
            marker=dict(colors=['#F0FFFF','#8c393c']),
            hole=0.3
        ))
        donut_chart.update_layout(
            title_text=f'Comparison between Data AA and Data AB {month_name(2)}',
            width=chart_width, height=chart_height
        )
        st.plotly_chart(donut_chart)

    with col3:
      st.write('Visualize the data for the las two months')
      df_combined =pd.concat([AA_actualmonth, AA_pastlmonth])
      st.dataframe(df_combined, width=600, height=100)


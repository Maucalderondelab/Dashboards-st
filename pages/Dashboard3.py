import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
from my_module import month_name, year_range, filter_year_month
from my_module import today


st.set_page_config(page_title = "Dashboard 3",
                   layout='wide', 
                   initial_sidebar_state='collapsed',
                   menu_items={ 'About': "https://www.linkedin.com/in/mcalderondelab/"}
                   )

# Sidebar for selecting the year
st.title('Dashboard 3')

with open('style.css') as f:
    css_styles = f'<style>{f.read()}</style>'
st.markdown(css_styles, unsafe_allow_html=True)
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
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August','September','October','November','December']

####################################################################################################################################################################
#################################################################################################################################################################### 

data = []
# Loop through years and months to generate random data
for year in (list(range(2019, 2024))):
    for month in months:
        row = {
            'Year': year,
            'Month': month,
            'Data CC': np.random.uniform(1,10),
            'Data CD': np.random.uniform(1,10)
        }
        data.append(row)
df_comb = pd.DataFrame(data)

CC_2019 = filter_year_month(df_comb, desired_years=[2019], desired_month_names=desired_month_names, columns=['Year', 'Month','Data CC','Data CD'])
CC_2020 = filter_year_month(df_comb, desired_years=[2020], desired_month_names=desired_month_names, columns=['Year', 'Month','Data CC','Data CD'])
CC_2021 = filter_year_month(df_comb, desired_years=[2021], desired_month_names=desired_month_names, columns=['Year', 'Month','Data CC','Data CD'])
CC_2022 = filter_year_month(df_comb, desired_years=[2022], desired_month_names=desired_month_names, columns=['Year', 'Month','Data CC','Data CD'])
CC_2023 = filter_year_month(df_comb, desired_years=[2023], desired_month_names=desired_month_names, columns=['Year', 'Month','Data CC','Data CD'])

years_CC = [2023,2022,2021,2020,2019]
selected_year = st.selectbox('Select year for', years_CC)

col1, col2 = st.columns([0.7, 0.3])

year_filtered_data = {
        2023: CC_2023[(CC_2023 != 0).all(axis=1)],
        2022: CC_2022[(CC_2022 != 0).all(axis=1)],
        2021: CC_2021[(CC_2021 != 0).all(axis=1)],
        2020: CC_2020[(CC_2020 != 0).all(axis=1)],
        2019: CC_2019[(CC_2019 != 0).all(axis=1)]
        }
with col1:
    year_figs = {}
    for year, year_df in year_filtered_data.items():
        year_figs[year] = px.bar(
            year_df,
            x='Date',
            y=['Data CC', 'Data CD'],
            text_auto=True,
            color_discrete_map={'Data CC':'#E6C7C2', 'Data CD':'#8c393c'}
            )
         
        year_figs[year].update_layout(
            title_text=f'Anual data for ({year})',
            width=950,
            height=500
            )
    st.plotly_chart(year_figs[selected_year])

with col2:
    
    st.write(f'Data in the year ({selected_year}):') 
    selected_year_df = year_filtered_data[selected_year] 

    st.dataframe(selected_year_df, width =400, height =200 )
      
    # Select the value for a specific date
    specific_date = f'{selected_year} {month_name(1)}'
    previous_month_date = f'{selected_year} {month_name(2)}'

    col1 ,col2 = st.columns(2)
    with col1:
        value_actualmonth = round(selected_year_df.loc[selected_year_df['Date'] ==specific_date , 'Data CC'].values[0],2)
        value_previousmonth = round(selected_year_df.loc[selected_year_df['Date'] ==previous_month_date , 'Data CC'].values[0],2)
        delta = float(value_actualmonth) - float(value_previousmonth)
        
        st.metric(label=f"Metric Data CC {month_name(1)}", value=value_actualmonth, delta=round(delta,2))
    with col2:
        value_actualmonth = round(selected_year_df.loc[selected_year_df['Date'] ==specific_date , 'Data CD'].values[0],2)
        value_previousmonth = round(selected_year_df.loc[selected_year_df['Date'] ==previous_month_date , 'Data CD'].values[0],2)
        delta = float(value_actualmonth) - float(value_previousmonth)
        
        st.metric(label=f"Metric Data CD {month_name(1)}", value=value_actualmonth, delta=round(delta,2))

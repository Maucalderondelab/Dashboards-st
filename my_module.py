# In this notebook we keep all the functions that are usefull.

# Typical function to work on python
import pandas as pd 
# Functions for the date and time
from datetime import date

#####################################################################################################################################################################
#####################################################################################################################################################################
#                                                                            DATE
#####################################################################################################################################################################
#####################################################################################################################################################################
today = date.today()

months = ['January', 'February', 'March', 'April', 
          'May', 'June', 'July', 'August',
          'September','October','November','December'
]

month_mapping = {
    1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio',
    7: 'Julio', 8: 'Agosto', 9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'
}

def month_name (x):
  actual_month = today.strftime("%m")
  month = months[int(actual_month)-x] 
  return month

def year_range(start_year, end_year):
    return list(range(start_year, end_year + 1))


def store_graph_df(residuos_sums, columns):
  stored_dataframes = {}  # Dictionary to store the DataFrames
  for i, sums in enumerate(residuos_sums):
    df = pd.DataFrame({
          'Data': columns,
          'Weight [kg]': sums,
          'Month': month_name(i + 1)
        })
    stored_dataframes[i] = df

  for i in range(len(stored_dataframes)-1):
    if i == 0:
      graph_df = pd.concat([stored_dataframes[i+1], stored_dataframes[i]], ignore_index=True)
      aux = graph_df
    else:
      graph_df = pd.concat([stored_dataframes[i+1],aux], ignore_index=True)
      aux = graph_df
  graphic_dataframes = graph_df
  return stored_dataframes, graphic_dataframes

# function to select specific data.
def specific_data(df,specific, specific_mes):
            aux_df = pd.DataFrame(df)
            filer_by_month_and_desecho = aux_df[(aux_df['Data'] == specific) & (aux_df['Month'] == specific_mes)]
            final_value = filer_by_month_and_desecho['Weight [kg]']
            return final_value

# Filter the dataframe based on desired years and month names
def filter_year_month(df, desired_years, desired_month_names,columns):
    
    filtered_df = df[(df['Año'].isin(desired_years)) & (df['Mes'].isin(desired_month_names))][columns]

    # Convert 'Año' column to string
    filtered_df['Año'] = filtered_df['Año'].astype(int)
    filtered_df['Año'] = filtered_df['Año'].astype(str)
    # Create a new column combining 'Año' and 'Mes'
    filtered_df['Fecha'] = filtered_df['Año'] + ' ' + filtered_df['Mes']

    # Rename the new column
    filtered_df = filtered_df.rename(columns={'Fecha': 'Fecha'})

    # Drop 'Año' and 'Mes' columns
    filtered_df = filtered_df.drop(labels=['Año', 'Mes'], axis=1)

    # Reorder columns, putting 'Fecha' at the beginning
    filtered_df = filtered_df[['Fecha'] + [col for col in filtered_df.columns if col != 'Fecha']]

    return filtered_df

#####################################################################################################################################################################
#####################################################################################################################################################################
#                                                                   AGUA      
# 
#   Funciones importantes para limpiar los datos de agua. 
#   Estas funciones nos ayudaran a ordenar los datos y tener todo listo al momento de graficar.
#####################################################################################################################################################################
#####################################################################################################################################################################

def filter_year_month(df, desired_years, desired_month_names,columns):
    # Filter the dataframe based on desired years and month names
    filtered_df = df[(df['Year'].isin(desired_years)) & (df['Month'].isin(desired_month_names))][columns]

    # Convert 'Año' column to string
    filtered_df['Year'] = filtered_df['Year'].astype(int)
    filtered_df['Year'] = filtered_df['Year'].astype(str)
    # Create a new column combining 'Año' and 'Mes'
    filtered_df['Date'] = filtered_df['Year'] + ' ' + filtered_df['Month']

    # Rename the new column
    filtered_df = filtered_df.rename(columns={'Date': 'Date'})

    # Drop 'Año' and 'Mes' columns
    filtered_df = filtered_df.drop(labels=['Year', 'Month'], axis=1)

    # Reorder columns, putting 'Fecha' at the beginning
    filtered_df = filtered_df[['Date'] + [col for col in filtered_df.columns if col != 'Date']]

    return filtered_df


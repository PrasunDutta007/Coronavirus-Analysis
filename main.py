import pandas as pd
import requests

#Step 1: Data Collection
url = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Asia'
req = requests.get(url)
data_list = pd.read_html(req.text)

#Step 2: Data Cleaning
target_df = data_list[4]
#1) Changing Column Names
target_df.columns = ['Country', 'Total Cases', 'Active Cases', 'Total Deaths', 'Total Recoveries', 'Col 6']
#2) Removing Unwanted Columns
target_df = target_df[['Country', 'Total Cases', 'Active Cases', 'Total Deaths', 'Total Recoveries']]
#3) Removing Extra Rows
last_index = target_df.index[-1]
target_df = target_df.drop([last_index])
#4)  Extra Value [Unknown] in Column 3
target_df['Active Cases'] = target_df['Active Cases'].str.replace('Unknown','0')
#5) Wrong Datatypes
target_df['Total Cases'] = pd.to_numeric(target_df['Total Cases'])
target_df['Active Cases'] = pd.to_numeric(target_df['Active Cases'])
target_df['Total Deaths'] = pd.to_numeric(target_df['Total Deaths'])
target_df['Total Recoveries'] = pd.to_numeric(target_df['Total Recoveries'])

#Step 3: Export the Data
target_df.to_excel(r'covid19_dataset.xlsx') 
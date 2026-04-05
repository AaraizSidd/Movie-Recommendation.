# Importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans


customer_data = pd.read_csv('IMDB-Movie-Data.csv')
# Display the first 5 rows of the dataset
print(customer_data.head(10))

print(customer_data.shape)

print("Number of rows:", customer_data.shape[0])
print("Number of columns:", customer_data.shape[1])

print("Any missing values?",customer_data.isnull().values.any())

print(customer_data.isnull().sum())

sns.heatmap(customer_data.isnull())
plt.show()

per_missing = customer_data.isnull().sum() * 100 / len(customer_data)
print(per_missing)
customer_data = customer_data.dropna(axis=0)

dup_customer_data= customer_data.duplicated().any()

print("Any duplicate rows?", dup_customer_data)

customer_data = customer_data.drop_duplicates() 
print("Shape after removing missing values and duplicates:", customer_data.shape)

print(customer_data.describe(include='all'))

print(customer_data.columns)

customer_data[customer_data['Runtime (Minutes)'] >= 180]

print(customer_data.columns)

customer_data.groupby('Year') ['Votes'].mean().sort_values(ascending=False) 

sns.barplot(x='Year', y='Votes', data=customer_data)
plt.title('Average Votes per Year')
plt.show()

customer_data.groupby('Year') ['Revenue (Millions)'].mean().sort_values(ascending=False) 

sns.barplot(x='Year', y='Revenue (Millions)', data=customer_data)
plt.title('Average Revenue per Year')
plt.show() 

print(customer_data.columns)

customer_data.groupby('Director') ['Rating'].mean().sort_values(ascending=False)

print(customer_data.columns)

top10_ = customer_data.nlargest(10, 'Runtime (Minutes)') ['Title','Runtime (Minutes)'].set_index('Title')

print(top10_)

#sns.barplot(x='Runtime (Minutes)', y=top10_.len.index, sudata=top10_len, palette='mako')
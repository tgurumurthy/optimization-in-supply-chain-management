import pandas as pd
data = pd.read_csv(r'C:/Users/RISHI YADAV/Desktop/Machine Downtime.csv')
data.dtypes
import numpy as np
import pandas as pd
# Data Exploration
print(data.head())
print(data.info())

# Summary Statistics
dada= data.describe()

# Handling Missing Values
print(data.isnull().sum())
data_cleaned = data.dropna()
data_imputed = data.fillna(data.mean())  # Replace NaN values with mean




# Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Example: Scatter plot
sns.scatterplot(x='Hydraulic_Pressure(bar)', y='Coolant_Pressure(bar)', data=data)
plt.show()

# Time Series Analysis
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

# Example: Plotting time series data
data['Hydraulic_Pressure(bar)'].plot(figsize=(12, 6), title='Hydraulic Pressure Over Time')
plt.show()

# Correlation Analysis
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()
data_cleaned = data.dropna()
data_imputed = data.fillna(data.mean())  # Replace NaN values with mean
# Example: Impute missing values in specific columns
columns_to_impute = ['Hydraulic_Pressure(bar)', 'Coolant_Pressure(bar)', 'Torque(Nm)']
for column in columns_to_impute:
    data[column].fillna(data[column].mean(), inplace=True)
data_filled = data.fillna(method='ffill')


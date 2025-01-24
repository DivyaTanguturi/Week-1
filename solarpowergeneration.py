import pandas as pd
import numpy as np
import seaborn as sns

#Load the dataset
df=pd.read_csv('C:/Users/geeth/OneDrive/Desktop/predicting Solar power output/solarpowergeneration.csv')

#Display the first few rows of the dataset
df.head()
df.tail()
df.head(10)

#to check the total number of rows and columns
df.shape

#Display summary
df.describe()

#check the information of the dataset
df.info()

#Check for the missing values
df.isnull().sum()

#Check dulpicate values
df.duplicated().sum()

import matplotlib.pyplot as plt
#plot distibution of power
plt.figure(figsize=(10,6))
sns.histplot(df['generated_power_kw'],bins=30,kde=True)
plt.title('Distribution of Generated Power(kW)')
plt.xlabel('Generated Power(kW)')
plt.ylabel('Frequency')
plt.show()



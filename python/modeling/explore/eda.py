import os
import sys
#sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))  #relative path reference packages
sys.path.append("/absolute/path/to/prometheus/python/")
import library.exploration
import matplotlib.pyplot as plt
import pandas as pd
from pandas.tools.plotting import scatter_matrix

file = "/path/to/my_file.csv"
df = pd.read_csv(file, sep=', ')

df.head(5) # print first 5 rows
df.describe() # get summary of numeric values
df.dtypes # print data types of cols

df.groupby(['class']).describe() # get summary of levels within a cat var

#-----------------------------------------
# Type Casting
#-----------------------------------------
df['date1'] = pd.to_datetime(df['date1'])
df[['col2','col3']] = df[['col2','col3']].apply(pd.to_numeric)

#-----------------------------------------
# Transformations
#-----------------------------------------
(df['date1'] - df['date2']).astype('timedelta64[h]') # num of hours between dates
df['hour'] = df['date1'].hour
df['day'] = df['date1].weekday
df['day_of_year'] = df['date1].dayofyear

#-----------------------------------------
# Exploratory Plots
#-----------------------------------------
pd.options.display.mpl_style = 'default' # Change display style 

# Plot scatter-plot matrix with kernal-density smoothing
scatter_matrix(df, alpha=0.2, figsize=(6, 6), diagonal='kde')

# Plot histograms of the variables in df
plt.figure()
df.diff().hist(color='k', alpha=0.5, bins=50)

# Plot all vars grouped by the response var "class"
df.groupby(['class']).hist()

# Plot the distn of variable "var1" by the response 
data.groupby(['class']).var1.hist(alpha=0.4)

# plot boxplots for each variable
df.boxplot()

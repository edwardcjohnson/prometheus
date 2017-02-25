# pip install pandas-summary

# dfs.columns_stats: counts, uniques, missing, missing_perc, and type per column
# dsf.columns_types: a count of the types of columns
# dfs[column]: more in depth summary of the column
# summary(): extends the describe() function with the values with columns_stats

from pandas_summary import DataFrameSummary

dfs = DataFrameSummary(df)

dfs.columns_types

dfs.columns_stats

dfs['col1']

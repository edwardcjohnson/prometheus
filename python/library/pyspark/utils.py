from functools import reduce
from pyspark.sql import DataFrame

def unionAll(*dfs):
  return reduce(DataFrame.unionAll, dfs)
  

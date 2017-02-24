#!/usr/bin/env python

import datetime as dt
import numpy as np
import os
from pyspark.sql import HiveContext, Row
from pyspark.sql.functions import from_unixtime, unix_timestamp, min, max
import pandas as pd
import subprocess
import sys
from functools import reduce
from pyspark.sql import DataFrame

def unionAll(*dfs):
  return reduce(DataFrame.unionAll, dfs)
  
def get_min_max_dates(spark_df, col_name):
    """Check the min and max values for a date column.
    
    Args:
        spark_df: a spark data frame
        col_name: a string representing a timestamp 
                  type column in dataframe.
    Returns:
        A spark data frame with columns 'min', and 
        'max' representing the min and max dates in 
        the data frame
    """
    return spark_df.withColumn(
        col_name, unix_timestamp(col_name)).agg(
        from_unixtime(min(col_name)).alias("min"),
        from_unixtime(max(col_name)).alias("max"))
  
class Filter(object):
    """Class to filter values in a spark dataframe
    
    Attributes:
        dataframe: A spark data frame.
        column_name: A string representing the column
                     that will be the basis for the filter
    """
    
    def __init__(self, dataframe, column_name):
        self.df = dataframe
        self.col = column_name
    
    def less_or_eq(self, value):
        mask = self.df[self.col] <= value
        return self.df.where(mask)
    
    def greater_or_eq(self, value):
        mask = self.df[self.col] >= value
        return self.df.where(mask)
    
    def greater(self, value):
        mask = self.df[self.col] > value
        return self.df.where(mask)
    
    def less(self, value):
        mask = self.df[self.col] < value
        return self.df.where(mask)
    
    def equal(self, value):
        mask = self.df[self.col] == value
        return self.df.where(mask)

    def not_equal(self, value):
        mask = self.df[self.col] != value
        return self.df.where(mask)
    
    def between(self, *values):
        mask = ((self.df[self.col] > values[0]) &
                (self.df[self.col] < values[1]))
        return self.df.where(mask)

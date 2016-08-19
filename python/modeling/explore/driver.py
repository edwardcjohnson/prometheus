import os
import sys
#sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))  #relative path reference packages
sys.path.append("/absolute/path/to/prometheus/python/")
import library.exploration
import pandas as pd

file = "/path/to/my_file.csv"
df = pd.read_csv(file, sep=', ')

df.describe() # get summary of numeric values

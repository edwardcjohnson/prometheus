#!/usr/bin/env python3

"""driver.py: 
    
    The file can be run by executing the following
    from the command line:
    spark-submit --master yarn driver.py
"""

import os
import sys
sys.path.append(os.environ["PROMETHEUS_HOME"]) # in .bashrc put: export PROMETHEUS_HOME=/work/repos/prometheus/

from datetime import datetime
import logging
import pandas as pd
import python.library.utilities.helpers as utils
from python.library.utilities.hadoop_helpers import Filter
from pyspark import SparkContext, SparkConf
from pyspark.sql import HiveContext
from pyspark.sql.types import DateType

def main(param1, param2):

	logging.basicConfig(filename='driver.log',
		filemode='w',format='%(levelname)s:%(message)s', level=logging.INFO)

	utils.check_kerberos_ticket()

	logging.info(utils.banner("Welcome to My App's log"))
	logging.info(utils.banner("Start Time: {0}".format(str(datetime.now()))))

	conf = (SparkConf()
		.setAppName("My Application")
		.set("spark.executor.memory", "2g")
		.set("spark.driver.memory", "2g"))
	sc = SparkContext(conf = conf)
	sqlContext = HiveContext(sc)
  
  
  #-------------------------
  # Functionality starts here
  #-------------------------
  
  # pyspark stuff....
  
  #-------------------------
  # Functionality ends
  #-------------------------
  logging.info(utils.banner("End Time: {0}".format(str(datetime.now()))))
  
if __name__ == "__main__":
    main(p1, p2)
